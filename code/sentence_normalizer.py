import string

from nltk import word_tokenize

from code.word_normalizer import WordNormalizer


class SentenceNormalizer:
    """
    Class for normalizing one sentence
    """
    def __init__(self):
        self.word_normalizer = WordNormalizer()
        self.stop_words = self.get_stop_words()

    @staticmethod
    def get_stop_words() -> list:
        """
        Returns stop-words list
        """
        with open('data/stop_words.txt', 'r') as f:
            return [word.replace('\n', '') for word in f.readlines()]

    @staticmethod
    def tokenize_sentence_with_punctuation(sentence: str) -> list:
        """
        Returns tokenized sentence (doesn't delete the punctuation)
        """
        return [sent for sent in word_tokenize(sentence)]

    def tokenize_sentence_without_punctuation(self, sentence: str, stop_words_ignore=False) -> list:
        """
        Returns tokenized sentence (deletes the punctuation)
        """
        tokenized_sentence = self.tokenize_sentence_with_punctuation(sentence)
        if not stop_words_ignore:
            return [token for token in tokenized_sentence if token not in string.punctuation]
        else:
            return [token for token in tokenized_sentence if token not in string.punctuation
                    and token.lower() not in self.stop_words]

    @staticmethod
    def __join_to_string(tokenized_sentence: list) -> str:
        """
        Joins tokenized sentence list to string
        """
        normalized_string = str()
        for token in tokenized_sentence:
            if token not in string.punctuation:
                normalized_string += ' ' + token
            else:
                normalized_string += token

        return normalized_string[1:]

    def __stemming_sentence(self, tokenized_sentence: list) -> list:
        """
        Normalizes every word in tokenized sentence list by stemming
        """
        return [self.word_normalizer.stemming(token) for token in tokenized_sentence]

    def __lemmatize_sentence(self, tokenized_sentence: list):
        """
        Normalizes every word in tokenized sentence list by lemmatisation
        """
        return [self.word_normalizer.lemmatise(token) for token in tokenized_sentence]

    def normalize_sentence(
            self,
            sentence: str,
            method='lemma',
            del_punctuation=True,
            split=False,
            stop_words_ignore=False
    ) -> string or list:

        """
        Returns a normalized sentence
        """

        if del_punctuation:
            tokenized_sentence = self.tokenize_sentence_without_punctuation(sentence, stop_words_ignore)
        else:
            tokenized_sentence = self.tokenize_sentence_with_punctuation(sentence, stop_words_ignore)

        if method == 'lemma':
            normalized_sentence = self.__lemmatize_sentence(tokenized_sentence)
        elif method == 'stemm':
            normalized_sentence = self.__stemming_sentence(tokenized_sentence)
        elif method == 'empty':
            normalized_sentence = tokenized_sentence
        else:
            raise KeyError('Unknown method. Use only "lemma" or "stemm"')

        if split:
            return normalized_sentence

        else:
            return self.__join_to_string(normalized_sentence)

