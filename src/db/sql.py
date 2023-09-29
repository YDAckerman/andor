

schema = """

DROP TABLE IF EXISTS messages;

CREATE TABLE messages (
  time TEXT,
  sender TEXT,
  email TEXT,
  message TEXT,
  approved INT
);

"""

insert_message = """

INSERT INTO messages
VALUES (%(sender)s, %(email)s, %(message)s);

"""

count_messages = """

SELECT COUNT(*) FROM messages;

"""
