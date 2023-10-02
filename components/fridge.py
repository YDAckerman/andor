from src.db.db import db_submit, db_submit_many, db_extract
from src.db.sql import delete_words, insert_word, get_words


def get_magnets():
    return db_extract(get_words, {})


def update_magnets(data):

    def to_dict(k, v):
        word = k.split("_")[0]
        top, left = v.split("_")
        return {'word': word, 'top': top, 'left': left}

    new_words = [to_dict(k, v) for k, v in data]

    db_submit(delete_words, {})
    db_submit_many(insert_word, new_words)

    pass
