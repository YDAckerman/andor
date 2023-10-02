import sqlite3
import random

DELETE_FROM_MAGNETS = """

DELETE FROM magnets;

"""

UPSERT_WORD = """

INSERT INTO magnets (word, top, left)
VALUES (:word, :top, :left);

"""

# Original word list: https://magneticpoetrymnl.com/pages/starter-kit-word-list

BOUND_TOP = 1000
BOUND_LEFT = 1000

MAGNETS = [

    "a",
    "a", "a", "about", "above", "act", "again", "age", "air",
    "all", "alone", "always", "am", "an", "an", "and", "and", "and",
    "and", "angry", "are", "are", "as", "as", "ask",
    "at", "at", "away", "arch", "art",

    "b",
    "bad", "be", "be", "be", "beauty", "bed", "boy", "bro",
    "been", "begin", "being", "believe", "belong", "bitter", "block",
    "break", "bring", "burn", "burst", "beefcake", "boba",
    "board", "but", "but", "by", "by", "bit", "byte", "block", "base",

    "c",
    "call", "cutting", "cook",
    "can", "cosmic", "change", "capital", "city", "clock",
    "cold", "come", "could", "cry", "d", "deep",
    "chain", "catan", "coin",

    "d",
    "deity", "did", "different", "dirty", "do", "do", "do",
    "dog", "door", "dream",
    "drink", "drive", "dry", "data", "dis", "dust", "dessert",
    "desert", "deep",

    "e",
    "easy", "eat", "ed", "ed", "empty", "equine",
    "end", "er", "es", "es", "est", "ever", "eye", "empire",

    "f",
    "face", "family",
    "far", "feel", "fight", "find", "fire", "fix", "for", "for",
    "forever", "forget", "forgive", "friend", "from", "from", "ful",
    "funny", "flower", "frog",

    "g",
    "garden", "gas", "get", "give", "go", "gone",
    "game", "good", "girl", "ghost",

    "h",
    "hand", "happen", "happiness", "happy", "hard", "has",
    "has", "have", "have", "heart", "heavy", "help",
    "here", "high", "him", "his", "hold", "hope", "hot",
    "hour", "how", "hungry", "hyper", "how", "human",

    "i",
    "I", "I", "i", "ist", "ist", "ism", "ism",
    "if", "in", "in", "in",
    "in", "ing", "ing", "is", "is", "it", "it",

    "j",
    "just", "just",

    "k",
    "keep", "keto", "ken", "know",

    "l"
    "late", "laugh", "less",
    "let", "letter", "life", "like", "like", "listen", "little", "live",
    "lock", "lone", "long", "look", "love", "ly", "ly",

    "m"
    "mad", "make", "make", "maximal", "metal", "merch",
    "man", "matter", "me", "me", "mean", "meet", "mind", "minute", "miss",
    "mixtape", "money", "moon", "morning", "move", "music", "must",
    "my", "my", "modern", "my",

    "n",
    "name", "near", "need", "never", "new", "next", "night",
    "no", "not", "not", "nothing", "now", "number",

    "o",
    "of", "of", "okay", "ocean", "our",
    "old", "on", "on", "one", "or", "or", "our", "out", "over", "own",

    "p",
    "page", "people", "play", "please", "pretty",
    "put", "post", "primitive", "power", "pastiche",

    "q",
    "question", "quantum",

    "r",
    "r", "rain", "re", "read", "rococo", "river",
    "ready", "reason", "red", "right", "road", "room", "rough", "run",

    "s",
    "s", "s", "s", "sad", "safe", "said", "same", "save", "say", "see",
    "seek", "shadow", "short", "should", "show", "sick",
    "social", "scene", "set",
    "silence", "sit", "skin", "sky", "sleep", "slow", "small", "smell",
    "so", "some", "song", "sorry", "start", "stay", "still", "stop",
    "struggle", "sun", "stars", "stone", "secret",
    "story", "system", "sheep",
    "sugar", "sure", "sweet",

    "t",
    "table", "take", "talk", "tawny", "tribute",
    "tear", "tell", "thank", "the", "the", "the", "their", "there", "these",
    "they", "they", "thing", "think", "those", "thought", "through", "time",
    "twilight", "than", "than", "trial",
    "to", "to", "today", "try",

    "u",
    "us", "use", "under",

    "v",
    "very", "vibe", "vibe", "vibe", "vampire", "village",

    "w",
    "wait", "walk", "want", "warm", "was", "was", "water", "way", "we",
    "week", "well", "were", "wet", "what", "when", "white", "who", "why",
    "will", "will", "window", "wish", "with", "with", "wonder", "word",
    "work", "would", "write",

    "x",

    "y",
    "y", "yet", "you", "you", "you", "young",
    "your", "your",

    "z"
]


def to_dict(word):

    return {'word': word,
            'top': random.randint(0, BOUND_TOP),
            'left': random.randint(0, BOUND_LEFT)}


def add_all(cur, magnets):

    data = [to_dict(magnet) for magnet in magnets]
    cur.executemany(UPSERT_WORD, data)


def delete_all(cur):

    cur.execute(DELETE_FROM_MAGNETS)


def main():

    conn = sqlite3.connect(database="andor.db")
    cur = conn.cursor()

    # reset
    delete_all(cur)
    add_all(cur, MAGNETS)

    conn.commit()
    conn.close()


if __name__ == '__main__':

    main()
