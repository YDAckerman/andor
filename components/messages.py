from src.db.db import db_submit
from src.db.sql import insert_message
from datetime import datetime


def record_message(data):

    db_submit(insert_message, {
        'time': datetime.timestamp(datetime.now()),
        'sender': data.get('name'),
        'email': data.get('email'),
        'message': data.get('msg')
    })

    pass
