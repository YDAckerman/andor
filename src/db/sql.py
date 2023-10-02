

schema = """

DROP TABLE IF EXISTS messages;

CREATE TABLE messages (
  time TEXT,
  sender TEXT,
  email TEXT,
  message TEXT,
);

DROP TABLE IF EXISTS magnets;

CREATE TABLE magnets (
  word TEXT,
  top REAL,
  left REAL
);

"""

insert_message = """

INSERT INTO messages (time, sender, email, message)
VALUES (:time, :sender, :email, :message);

"""

delete_words = """

DELETE FROM magnets;

"""

insert_word = """

INSERT INTO magnets (word, top, left)
VALUES (:word, :top, :left);

"""

get_words = """

SELECT rowid, word, top, left FROM magnets;

"""

count_messages = """

SELECT COUNT(*) FROM messages;

"""
