import sqlite3
import random

delete_from_magnets = """

DELETE FROM magnets;

"""

upsert_word_sql = """

INSERT INTO magnets (word, top, left)
VALUES (:word, :top, :left);

"""

# Original word list: https://magneticpoetrymnl.com/pages/starter-kit-word-list

BOUND_TOP = 1000
BOUND_LEFT = 1000

MAGNETS = [
    "&", "a", "a", "a", "about", "above", "act", "again", "age", "air",
    "all", "alone", "always", "am", "an", "an", "and", "and", "and",
    "and", "angry", "are", "are", "as", "as", "ask",
    "at", "at", "away", "artificial", "bad", "be", "be", "beauty", "bed",
    "been", "begin", "being", "believe", "belong", "bitter", "blank",
    "blue", "break", "bring", "burn", "burst", "beefcake",
    "board", "but", "but", "by", "by", "call", "cutting",
    "can", "cosmic", "change", "capital", "city", "clock",
    "cold", "come", "could", "cry", "curse", "d", "deep",
    "chain", "catan", "deity",
    "did", "die", "different", "dirty", "do", "dog", "door", "dream",
    "drink", "drive", "dry", "e", "easy", "eat", "ed", "ed", "empty",
    "end", "er", "es", "es", "est", "ever", "eye", "face", "family",
    "far", "feel", "fight", "find", "fire", "fix", "for", "for",
    "forever", "forget", "forgive", "friend", "from", "from", "ful",
    "funny", "garden", "gas", "get", "girl", "give", "go", "gone",
    "game",
    "good", "hair", "hand", "happen", "happiness", "happy", "hard", "has",
    "has", "have", "have", "he", "he", "heart", "heavy", "help", "her",
    "honey",
    "her", "here", "high", "him", "him", "his", "his", "hold", "hope",
    "hour", "how", "hungry", "I", "I", "I", "I", "ism", "ism",
    "if", "in", "in",
    "intelligence",
    "in", "ing", "ing", "ing", "is", "is", "it", "it", "keep", "kill",
    "keto",
    "bite", "block", "ken", "know", "late", "laugh", "lazy", "learn", "less",
    "let", "letter", "life", "like", "like", "listen", "little", "live",
    "lock", "lone", "long", "look", "love", "ly", "ly", "mad", "make",
    "man", "matter", "me", "me", "mean", "meet", "mind", "minute", "miss",
    "mixtape", "money", "moon", "morning", "move", "movie", "music", "must",
    "morbid",
    "my", "my", "name", "near", "need", "never", "new", "next", "night",
    "no", "not", "not", "nothing", "now", "number", "of", "of", "okay",
    "old", "on", "on", "one", "or", "or", "our", "out", "over", "own",
    "page", "people", "play", "please", "pretty",
    "put", "question", "quick", "r", "r", "rain", "re", "read",
    "ready", "reason", "red", "right", "road", "room", "rough", "run", "s",
    "s", "s", "s", "sad", "safe", "said", "same", "save", "say", "see",
    "seek", "shadow", "she", "she", "short", "should", "show", "sick",
    "social",
    "silence", "sit", "skin", "sky", "sleep", "slow", "small", "smell",
    "so", "some", "song", "sorry", "start", "stay", "still", "stop",
    "struggle",
    "stomp",
    "story",
    "sugar", "summer", "sun", "sure", "sweet", "table", "take", "talk",
    "tear", "tell", "thank", "the", "the", "the", "their", "there", "these",
    "they", "they", "thing", "think", "those", "thought", "through", "time",
    "twilight", "than", "than",
    "to", "to", "today", "try", "us", "use", "very",
    "wait", "walk", "want", "warm", "was", "was", "water", "way", "we",
    "week", "well", "were", "wet", "what", "when", "white", "who", "why",
    "will", "will", "window", "wish", "with", "with", "wonder", "word",
    "work", "would", "write", "y", "y", "yet", "you", "you", "you", "young",
    "your", "your"
]


def main():

    conn = sqlite3.connect(database="andor.db")
    cur = conn.cursor()

    cur.execute(delete_from_magnets)

    data = [{'word': magnet,
             'top': random.randint(0, BOUND_TOP),
             'left': random.randint(0, BOUND_LEFT)
             } for magnet in MAGNETS]
    cur.executemany(upsert_word_sql, data)

    conn.commit()
    conn.close()


if __name__ == '__main__':

    main()
