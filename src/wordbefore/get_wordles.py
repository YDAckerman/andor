import requests
import re
from bs4 import BeautifulSoup
import sqlite3


class WordBot:

    # url = "https://wordfinder.yourdictionary.com/wordle/answers/"
    url = "https://www.techradar.com/news/past-wordle-answers"

    def __init__(self):
        self.wordles = None

    def get_wordles(self):

        raw_resp = requests.get(self.url)
        soup = BeautifulSoup(raw_resp.text, 'html.parser')
        tds = soup.find_all('span', class_=re.compile('c[0-9]'))
        results = [self.rm_whitespace(e.get_text()) for e in tds]

        self.wordles = [results[i:i+3] for i in range(3, len(results) - 20, 3)]

    @staticmethod
    def rm_whitespace(s: str) -> str:
        return re.sub('\s', '', s)


if __name__ == '__main__':

    bot = WordBot()
    bot.get_wordles()

    conn = sqlite3.connect(database="andor.db")
    cur = conn.cursor()

