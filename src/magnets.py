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
    "a", "a", "a", "about", "above", "act", "again", "age", "air",
    "all", "alone", "always", "am", "an", "an", "and", "and", "and",
    "and", "angry", "are", "are", "as", "as", "ask",
    "at", "at", "away", "arch", "art",

    "bad", "be", "be", "beauty", "bed", "boy",
    "been", "begin", "being", "believe", "belong", "bitter", "block",
    "break", "bring", "burn", "burst", "beefcake",
    "board", "but", "but", "by", "by", "bit", "byte", "block", "base",

    "call", "cutting", "cook",
    "can", "cosmic", "change", "capital", "city", "clock",
    "cold", "come", "could", "cry", "d", "deep",
    "chain", "catan", "coin",

    "deity", "did", "different", "dirty", "do", "dog", "door", "dream",
    "drink", "drive", "dry", "data", "distributed", "dust", "dessert",
    "desert", "deep",

    "e", "easy", "eat", "ed", "ed", "empty", "equine",
    "end", "er", "es", "es", "est", "ever", "eye", "empire",

    "face", "family",
    "far", "feel", "fight", "find", "fire", "fix", "for", "for",
    "forever", "forget", "forgive", "friend", "from", "from", "ful",
    "funny", "flower", "frog",

    "garden", "gas", "get", "give", "go", "gone",
    "game", "good", "girl",

    "hand", "happen", "happiness", "happy", "hard", "has",
    "has", "have", "have", "heart", "heavy", "help",
    "here", "high", "him", "his", "hold", "hope", "hot",
    "hour", "how", "hungry", "hyper", "how", "human",

    "I", "I", "i", "i", "ist", "ist", "ism", "ism",
    "if", "in", "in", "in",
    "in", "ing", "ing", "is", "is", "it", "it",

    "just", "just",

    "keep", "keto", "ken", "know",

    "late", "laugh", "less",
    "let", "letter", "life", "like", "like", "listen", "little", "live",
    "lock", "lone", "long", "look", "love", "ly", "ly",

    "mad", "make", "maximal", "metal", "merch", 
    "man", "matter", "me", "me", "mean", "meet", "mind", "minute", "miss",
    "mixtape", "money", "moon", "morning", "move", "music", "must",
    "my", "my", "modern", "my",

    "name", "near", "need", "never", "new", "next", "night",
    "no", "not", "not", "nothing", "now", "number",

    "of", "of", "okay", "ocean", "our",
    "old", "on", "on", "one", "or", "or", "our", "out", "over", "own",


    "page", "people", "play", "please", "pretty",
    "put", "post", "primitive", "power", "pastiche",

    "question", "quantum",

    "r", "r", "rain", "re", "read", "rococo",
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

    "table", "take", "talk", "tawny",
    "tear", "tell", "thank", "the", "the", "the", "their", "there", "these",
    "they", "they", "thing", "think", "those", "thought", "through", "time",
    "twilight", "than", "than", "trial",
    "to", "to", "today", "try",

    "us", "use", "under",

    "very", "vibe", "vibe", "vibe", "vampire", "village",

    "wait", "walk", "want", "warm", "was", "was", "water", "way", "we",
    "week", "well", "were", "wet", "what", "when", "white", "who", "why",
    "will", "will", "window", "wish", "with", "with", "wonder", "word",
    "work", "would", "write",

    "y", "y", "yet", "you", "you", "you", "young",
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
