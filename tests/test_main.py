# -*- coding: utf-8 -*-
import unittest

from language_detector import detect_language


class TestLanguageDetector(unittest.TestCase):

    def setUp(self):
        self.languages = [
            {
                'name': 'Spanish',
                'common_words': [
                    'el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'ser', 'se',
                    'no', 'haber', 'por', 'con', 'su', 'para', 'como', 'estar',
                    'tener', 'le', 'lo', 'lo', 'todo', 'pero', 'más', 'hacer',
                    'o', 'poder', 'decir', 'este', 'ir', 'otro', 'ese', 'la',
                    'si', 'me', 'ya', 'ver', 'porque', 'dar', 'cuando', 'él',
                    'muy', 'sin', 'vez', 'mucho', 'saber', 'qué', 'sobre',
                    'mi', 'alguno', 'mismo', 'yo', 'también', 'hasta'
                ]
            },
            {
                'name': 'German',
                'common_words': [
                    'das', 'ist', 'du', 'ich', 'nicht', 'die', 'es', 'und',
                    'der', 'was', 'wir', 'zu', 'ein', 'er', 'in', 'sie', 'mir',
                    'mit', 'ja', 'wie', 'den', 'auf', 'mich', 'dass', 'so',
                    'hier', 'eine', 'wenn', 'hat', 'all', 'sind', 'von',
                    'dich', 'war', 'haben', 'für', 'an', 'habe', 'da', 'nein',
                    'bin', 'noch', 'dir', 'uns', 'sich', 'nur',
                    'einen', 'kann', 'dem'
                ]
            },
            {
                'name': 'English',
                'common_words': ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 
                    'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 
                    'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 
                    'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 
                    'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 
                    'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 
                    'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 
                    'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 
                    'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 
                    'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 
                    'day', 'most', 'us'
                ]
            }
        ]

    def test_detect_language_spanish(self):
        text = """
            Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
            conocido como Leo Messi, es un futbolista argentino11 que juega
            como delantero en el Fútbol Club Barcelona y en la selección
            argentina, de la que es capitán. Considerado con frecuencia el
            mejor jugador del mundo y calificado en el ámbito deportivo como el
            más grande de todos los tiempos, Messi es el único futbolista en la
            historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de
            ellos en forma consecutiva– y el primero en
            recibir tres Botas de Oro.
        """
        result = detect_language(text, self.languages)
        self.assertEqual(result, 'Spanish')

    def test_detect_language_german(self):
        text = """
            Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
            Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
            der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
            erzielte. Inzwischen hat Messi als einziger Spieler mehr als 300
            Erstligatore erzielt und ist damit Rekordtorschütze
            der Primera División.
        """
        result = detect_language(text, self.languages)
        self.assertEqual(result, 'German')

    def test_detect_language_mixed_languages(self):
        text = """
            # spanish
            Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
            conocido como Leo Messi, es un futbolista argentino11 que juega
            como delantero en el Fútbol Club Barcelona y en la selección
            argentina, de la que es capitán.

            # german
            Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
            Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
            der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
            erzielte.
        """
        result = detect_language(text, self.languages)
        self.assertEqual(result, 'Spanish')

    def test_detect_language_ambiguous(self):
        text = """
            A giant dog chased seven cats.
        """
        result = detect_language(text, self.languages)
        self.assertEqual(result, {'Spanish', 'English'})


if __name__ == '__main__':
    unittest.main()  