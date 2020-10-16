import pymorphy2
from nltk import stem


class WordNormalizer:
    """
    Class for normalizing one word
    """
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
        self.stem = stem.SnowballStemmer('russian')

    def lemmatise(self, word: str) -> str:
        """
        Returns a normalized word
        """
        return self.morph.parse(word)[0].normal_form

    def stemming(self, word: str) -> str:
        """
        Return a stem from word
        """
        return self.stem.stem(word)
