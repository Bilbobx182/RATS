import re

import nltk
import requests
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import helpers

wnl = WordNetLemmatizer()


class Job_Words_Main():
    words_list_from_indeed = []
    wordcount = {}

    def is_word_noun(self, word):
        word_tags = nltk.pos_tag([word])
        for word_list in word_tags:
            for classification in word_list:
                if 'NN' in classification:
                    return True
        return False

    def find_indeed(self, job):

        page_number = 0
        
        while page_number < self.config['page_count']:
            url = "https://ie.indeed.com/jobs?q={{ROLE}}&l={{LOCATION}}" + "&start={{START}}"
            url = url.replace("{{ROLE}}", job).replace("{{LOCATION}}", "Dublin")
            url = url.replace("{{START}}", str(page_number))
            all_jobs_result = requests.get(url)
            all_jobs_soup = BeautifulSoup(all_jobs_result.content, "html.parser")

            # TODO implement dupe protection
            for title in all_jobs_soup.find_all('a', {"class": "jobtitle turnstileLink"}):
                if 'company' in title.attrs['href']:
                    print(f"SEARCHING : https://ie.indeed.com{title.attrs['href']}")
                    result = requests.get(f"https://ie.indeed.com{title.attrs['href']}")
                    inner_html = BeautifulSoup(result.content, "html.parser")
                    for item in inner_html.find_all("div", {"id": re.compile(r"jobDescriptionText")}):
                        self.words_list_from_indeed.append(item.text)
                        print(item.text)
            page_number += 1

    def get_word_count_in(self):
        for line in self.words_list_from_indeed:
            for word in word_tokenize(re.sub(r'\W+', ' ', line.lower()).strip()):
                if len(word) > 2:
                    word = wnl.lemmatize(word)
                if self.is_word_noun(word):
                    if word in self.wordcount:
                        self.wordcount[word] += 1
                    else:
                        self.wordcount[word] = 1

    def __init__(self):
        self.config = helpers.get_json("config.json")
        print("Starting!")
        for job in self.config['jobs']:
            self.find_indeed(job)
            self.get_word_count_in()

        for item in {k: v for k, v in sorted(self.wordcount.items(), reverse=True, key=lambda x: x[1])}:
            print(item + "," + str(self.wordcount[item]))


jw = Job_Words_Main()
