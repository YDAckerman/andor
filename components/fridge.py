from src.db.db import db_submit, db_submit_many, db_extract
from src.db.sql import delete_words, insert_word, get_words


def get_magnets():
    return db_extract(get_words, {})


def update_magnets(data):
    db_submit(delete_words, {})
    db_submit_many(insert_word, data)
    pass
