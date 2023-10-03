from src.db.db import db_submit_many, db_extract
from src.db.sql import insert_words, get_words


def get_magnets():
    return db_extract(get_words, {})


def update_magnets(data):

    def to_dict(k, v):
        word, row_id = k.split("_")
        top, left = v.split("_")
        return {'id': row_id, 'word': word, 'top': top, 'left': left}

    new_words = [to_dict(k, v) for k, v in data]

    print(new_words)
    db_submit_many(insert_words, new_words)

    pass
