# -*- coding: utf-8 -*-
"""This is the entry point of the program."""

from .languages import LANGUAGES
import string

# languages = [{'name':"spanish",'common_words':'['el',...]}, {'name':"english",...}]

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    
    # remove any punctuation and convert input text to lowercase
    clean_text = text.translate(None, string.punctuation)
    clean_text = clean_text.lower()
    text_words = clean_text.split()
    
    # use sets to find the shared unique words between the input text and language lists
    word_set = set(text_words)

    # initialize high_score, this will be used to find the highest scoring language
    # the name of the high-scoring language will be stored in matching_language
    high_score = -1
    matching_language = 'None'
    for language in languages:
        language_words = language['common_words']
        language_set = set(language_words)
        
        # take the set intersection to get the common words between input and language list
        common_set = word_set & language_set
        
        # update the language to be returned, if the current language scores higher than high_score
        if len(common_set) > high_score:
            matching_language = language['name']
            high_score = len(common_set)
    
    return matching_language
        
# if __name__ == '__main__':
#     text = """
#             Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
#             Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
#             der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
#             erzielte. Inzwischen hat Messi als einziger Spieler mehr als 300
#             Erstligatore erzielt und ist damit Rekordtorschütze
#             der Primera División.
#         """
#     detect_language(text,LANGUAGES)  