from typing import Dict
import requests
import re
from bs4 import BeautifulSoup
import sqlite3

DELETE_FROM_WORDLES = """

DELETE FROM wordles;

"""

UPSERT_WORDLES = """

INSERT INTO wordles (number, date, word)
VALUES (:num, :date, :word);

"""


class WordBot:

    url = "https://wordfinder.yourdictionary.com/wordle/answers/"
    # url = "https://www.techradar.com/news/past-wordle-answers"

    def __init__(self):
        self.wordles = None

    def get_wordles(self):

        raw_resp = requests.get(self.url)
        soup = BeautifulSoup(raw_resp.text, 'html.parser')
        tds = soup.find_all('td')
        results = [self.rm_whitespace(e.get_text())
                   for e in tds]

        self.wordles = [self.to_dict(results[i:i+3])
                        for i in range(3, len(results)-2, 3)]

    def add_all(self, cur):
        cur.executemany(UPSERT_WORDLES, self.wordles)

    def has_wordles(self):
        return len(self.wordles) > 800

    @staticmethod
    def rm_whitespace(s: str) -> str:
        return re.sub('[\n\t]', '', s)

    @staticmethod
    def to_dict(wordle) -> Dict[str, str]:

        return {'num': wordle[1],
                'date': wordle[0],
                'word': wordle[2]}

    @staticmethod
    def delete_all(cur):
        cur.execute(DELETE_FROM_WORDLES)


if __name__ == '__main__':

    print("Prepping WordBot")
    bot = WordBot()
    print("Getting Wordles")
    bot.get_wordles()

    if bot.has_wordles():

        
        conn = sqlite3.connect(database="../../instance/andor.db")
        cur = conn.cursor()

        # reset
        print("Resetting Wordles table")
        bot.delete_all(cur)
        print("Inserting Wordles")
        bot.add_all(cur)

        conn.commit()
        conn.close()
