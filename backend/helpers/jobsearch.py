import re

import nltk
import requests
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from backend.helpers.genericHelper import GenericHelper
import os

wnl = WordNetLemmatizer()


class JobSearch:
    all_jobs = []
    words_list_from_indeed = []
    wordcount = {}

    maxPageCount = 2


    def insertData(self, company=None, words=None):
        print("hello")

    def is_word_noun(self, word):
        # TODO Refactor this! Too many loops will negatively impact performance
        word_tags = nltk.pos_tag([word])
        for word_list in word_tags:
            for classification in word_list:
                if 'NN' in classification:
                    return True
        return False

    def _get_jobs_raw_from_indeed(self, page_number, job):
        url = "https://ie.indeed.com/jobs?q={{ROLE}}&l={{LOCATION}}" + "&start={{START}}"
        url = url.replace("{{ROLE}}", job).replace("{{LOCATION}}", "Dublin")
        url = url.replace("{{START}}", str(page_number))
        all_jobs_result = requests.get(url)
        return BeautifulSoup(all_jobs_result.content, "html.parser")

    def _find_indeed_job_divs(self, page_number, job):
        all_jobs_soup = self._get_jobs_raw_from_indeed(page_number, job)
        return self.helper.remove_duplicates_in_dict(all_jobs_soup.find_all('a', {"class": "jobtitle turnstileLink"}))

    def find_indeed(self, job):
        page_number = 0
        while page_number < self.maxPageCount:
            indeed_all_jobs = self._find_indeed_job_divs(page_number, job)

            for indeed_job in indeed_all_jobs:
                if 'company' in indeed_job.attrs['href']:
                    result = requests.get(f"https://ie.indeed.com{indeed_job.attrs['href']}")
                    inner_html = BeautifulSoup(result.content, "html.parser")

                    words = inner_html.find_all("div", {"id": re.compile(r"jobDescriptionText")})[0].text

                    job_info = {
                        'company': indeed_job.attrs['href'].split("/")[2],
                        'role': job,
                        'words' : words,
                        'wordFrequency': {}  # init an array, equal to the amount of words with 0.
                    }
                    self.all_jobs.append(job_info)
            page_number += 1

    def get_word_count_in(self,job):

            job['words'] =  word_tokenize(re.sub(r'\W+', ' ', job['words'].lower()).strip())
            for word in job['words']:
                if len(word) > 2 and (self.is_word_noun(word)):
                    word = wnl.lemmatize(word)
                    if word in job['wordFrequency']:
                       job['wordFrequency'][word] += 1
                       self.wordcount[word] += 1
                    else:
                        self.words_list_from_indeed.append(word)
                        self.wordcount[word] = 1
                        job['wordFrequency'][word] = 1
                else:
                    # We want to remove any < 2 letter words.
                    # That way we don't need to go over it later and remove them then.
                    print(f"REMOVING: {word}")
                    job['words'].remove(word)


            self.all_jobs[self.all_jobs.index(job)]['words'] = job['words']


    def __init__(self, job):
        self.helper = GenericHelper()
        self.job = job

    def calculate_information_from_job(self):
        for job in self.all_jobs:
            self.get_word_count_in(job)
            labels = list(({k: v for k, v in sorted(self.wordcount.items(), reverse=True, key=lambda x: x[1])}).keys())
            data = list(({k: v for k, v in sorted(self.wordcount.items(), reverse=True, key=lambda x: x[1])}).values())
            print(f"{data} \n, {labels} \n : Done")

    def search(self):
        self.find_indeed(self.job)
        self.calculate_information_from_job()

        return "hello"
