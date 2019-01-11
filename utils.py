from nltk.corpus import stopwords
from nltk import PorterStemmer
import re
import string

ps = PorterStemmer()
eng_stopwords = stopwords.words('english')
punctuations = string.punctuation


def text_len(text: str):
    """count the number of characters in a text"""
    return len(text) - text.count(" ") if len(text.strip()) else 0 


def count_punct(text: str, proportion=True):
    """count the number of punctuations in a text 
    set proportion=True to return count as ratio of number of
    characters in the text"""
    if not len(text.strip()): 
            return None
    result = sum([1 for char in text if char in punctuations])
    return round(result / text_len(text), 3) if proportion else result


def count_cap(text: str, proportion=True):
    """count the number of upper case letters in a text
    set proportion=True to return count as ratio of number of 
    non punctuated characters in the text"""
    if not len(text.strip()): 
            return None
    result = sum([1 for char in text if char.isupper() and 
                  char not in punctuations])
    return round(result / text_len(text), 3) if proportion else result


def clean_text(text: str, as_list=True):
    if not len(text.strip()): 
            return [] if as_list else ""
    text = "".join([char.lower() for char in text 
                    if char not in punctuations]).strip()
    tokens = re.split(r"\W+", text)
    result = [ps.stem(word) for word in tokens if word not in eng_stopwords]
    return result if as_list else " ".join(result)