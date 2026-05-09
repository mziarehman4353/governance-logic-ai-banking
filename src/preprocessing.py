
import pandas as pd
import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"[^a-z\s]", "", text)

    words = [
        w for w in text.split()
        if w not in stop_words
    ]

    return " ".join(words)
