from typing import List
from src.db.db import db_extract
from src.db.sql import search_wordles

def word_search(word) -> List[str]:
    return db_extract(search_wordles, {'word': word})
