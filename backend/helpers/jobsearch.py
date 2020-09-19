import re
import requests
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from helpers.genericHelper import GenericHelper
import time

wnl = WordNetLemmatizer()


class JobSearch:
    all_jobs = []
    words_list_from_indeed = []
    wordcount = {}

    maxPageCount = 2

    def insertData(self, company=None, words=None):
        print("hello")

    def _get_jobs_raw_from_indeed(self, page_number, job):
        url = "https://ie.indeed.com/jobs?q={{ROLE}}&l={{LOCATION}}" + "&start={{START}}"
        url = url.replace("{{ROLE}}", job).replace("{{LOCATION}}", "Dublin")
        url = url.replace("{{START}}", str(page_number))
        all_jobs_result = requests.get(url)
        return BeautifulSoup(all_jobs_result.content, "html.parser")

    def _find_indeed_job_divs(self, page_number, job):
        all_jobs_soup = self._get_jobs_raw_from_indeed(page_number, job)
        return self.helper.remove_duplicates_in_dict(all_jobs_soup.find_all('a'))

    def find_indeed(self, job):
        page_number = 0
        while page_number < self.maxPageCount:
            indeed_all_jobs = self._find_indeed_job_divs(page_number, job)

            for indeed_job in indeed_all_jobs:
                if ('href' in indeed_job.attrs):
                    if 'jk' in indeed_job.attrs['href']:
                        result = requests.get(
                            f"https://ie.indeed.com/viewjob?{indeed_job.attrs['href'].strip('/rclk')}")
                        inner_html = BeautifulSoup(result.content, "html.parser")

                        try:
                            words = inner_html.find_all("div", {"id": re.compile(r"jobDescriptionText")})[0].text
                            company = \
                            inner_html.find_all("div", {"class": re.compile(r"jobsearch-InlineCompanyRating")})[0].contents[0].text
                            job_title = (inner_html.find_all("h1", {"class": re.compile(r"JobInfoHeader")})[0].text)

                            job_info = {
                                'company': company,
                                'role': job,
                                'words': words,
                                'title': job_title,
                                'wordFrequency': {}  # init an array, equal to the amount of words with 0.
                            }
                            self.all_jobs.append(job_info)
                        except Exception as e:
                            print(f"Exception occured when trying to parse Job! {e}")
                page_number += 1

    def get_word_count_in(self, job):

        ignore_words = ['this','have','has', 'from', 'that', 'these', 'those', 'with', 'will', 'their', 'help', 'when', 'without',
                        'work', 'your', 'including','about']

        job['words'] = word_tokenize(re.sub(r'\W+', ' ', job['words'].lower()).strip())

        for word in job['words']:
            if word in ignore_words:
                job['words'].remove(word)
            elif len(word) > 3:
                word = wnl.lemmatize(word)
                # Handle the two different scenarios of incrementing
                if word in job['wordFrequency']:
                    job['wordFrequency'][word] += 1
                else:
                    job['wordFrequency'][word] = 1

                if word in self.wordcount:
                    self.wordcount[word] += 1
                else:
                    self.words_list_from_indeed.append(word)
                    self.wordcount[word] = 1
            else:
                job['words'].remove(word)

        self.all_jobs[self.all_jobs.index(job)]['words'] = job['words']

    def calculate_information_from_job(self):
        for job in self.all_jobs:
            self.get_word_count_in(job)

    def search(self):
        start = time.time()
        self.find_indeed(self.job)
        self.calculate_information_from_job()
        labels = list(({k: v for k, v in sorted(self.wordcount.items(), reverse=True, key=lambda x: x[1])}).keys())
        data = list(({k: v for k, v in sorted(self.wordcount.items(), reverse=True, key=lambda x: x[1])}).values())

        return_data = {
        'labels': labels[:15],
        'datasets': [{
            'data': data[:15]
        }]}
        end = time.time()
        return return_data

    def __init__(self, job):
        self.helper = GenericHelper()
        self.job = job
