# -*- coding: utf-8 -*-
"""This is the entry point of the program."""

from .languages import LANGUAGES
import string
import collections

# languages = [{'name':"spanish",'common_words':'['el',...]}, {'name':"english",...}]

def detect_language(text, languages):
    """Returns the detected language of given text."""
    
    # remove any punctuation and convert input text to lowercase
    clean_text = text.translate(None, string.punctuation)
    clean_text = clean_text.lower()
    text_words = clean_text.split()
    
    # we will use sets to find the shared unique words between the input text and language lists
    word_set = set(text_words)
    
    # use a dict with key = # matching words and value = set of language names
    # this is used to return the highest scoring language(s) at the end
    score_dict = collections.defaultdict(set)
    
    for language in languages:
        language_words = language['common_words']
        # both the input text and language list will be lowercase for comparison
        language_words = [word.lower() for word in language_words]
        language_set = set(language_words)
        
        # take the set intersection to get the common words between input and language list
        common_set = word_set & language_set
        
        score_dict[len(common_set)].add(language['name'])
    
    # get the set of languages that had the top score
    top_languages = score_dict[max(score_dict)]
    
    # if there is a single language with the best score, return that name as a string
    if len(top_languages) == 1:
        return next(iter(top_languages))
    
    # in case of a tie with multiple languages, return a set of language names    
    return top_languages
        
# if __name__ == '__main__':
#     text = """
#             Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
#             Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
#             der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
#             erzielte. Inzwischen hat Messi als einziger Spieler mehr als 300
#             Erstligatore erzielt und ist damit Rekordtorschütze
#             der Primera División.
#         """
#     text = """
#         A giant dog chased seven cats.
#         """
#     detect_language(text,LANGUAGES)  