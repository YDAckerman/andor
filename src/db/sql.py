

schema = """

DROP TABLE IF EXISTS messages;

CREATE TABLE messages (
  time TEXT,
  sender TEXT,
  email TEXT,
  message TEXT,
  read INT
);

DROP TABLE IF EXISTS magnets;

CREATE TABLE magnets (
  word TEXT,
  top REAL,
  left REAL
);

DROP TABLE IF EXISTS wordles;

CREATE TABLE wordles (
  number REAL,
  date TEXT,
  word TEXT
);

"""

insert_message = """

INSERT INTO messages (time, sender, email, message, read)
VALUES (:time, :sender, :email, :message, 0);

"""

delete_words = """

DELETE FROM magnets;

"""

search_wordles = """

SELECT number FROM wordles WHERE word = :word;

"""

insert_words = """

INSERT INTO magnets (rowid, word, top, left)
VALUES (:id, :word, :top, :left)
ON CONFLICT(rowid) DO
UPDATE SET top = excluded.top, left = excluded.left;

"""

get_words = """

SELECT rowid, word, top, left FROM magnets;

"""

count_messages = """

SELECT COUNT(*) FROM messages;

"""
