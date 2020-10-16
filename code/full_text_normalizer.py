from typing import Union

from nltk import sent_tokenize
from sklearn.base import BaseEstimator, TransformerMixin

from code.sentence_normalizer import SentenceNormalizer


class FullTextNormalizer(BaseEstimator, TransformerMixin):
    """
    Text normalization transformer
    """
    def __init__(self):
        self.sentence_normalizer = SentenceNormalizer()

    def fit_transform(self, X: Union[list, str], **fit_params):
        """
        Returns transformed text
        """
        return self.__normalize_text(text=X, **fit_params)

    @staticmethod
    def __split_to_sentences(text: str):
        """
        Returns splitted text
        """
        return [sent for sent in sent_tokenize(text)]

    def __split_and_normalize(
            self,
            text: Union[list, str],
            method: str,
            del_punctuation: bool,
            split_words: bool,
            stop_words_ignore: bool
    ) -> list:
        """
        Returns a list with normalized sentences
        """
        return [
            self.sentence_normalizer.normalize_sentence(
                sentence, method, del_punctuation, split_words, stop_words_ignore
            ) for sentence in self.__split_to_sentences(text)
        ]

    def normalize_text(
            self,
            text: Union[list, str],
            method='lemma',
            del_punctuation=True,
            split_words=False,
            split_sentences=False,
            stop_words_ignore=False,
            split_docs=False
    ) -> list:
        """
        Returns a normalized text
        """
        if isinstance(text, str):
            normalized_sentences = self.__split_and_normalize(text, method, del_punctuation, split_words, stop_words_ignore)

        elif isinstance(text, list):
            normalized_sentences = []
            for part_text in text:
                part_normalized_sentences = self.__split_and_normalize(part_text, method, del_punctuation, split_words, stop_words_ignore)

                if split_sentences:
                    normalized_sentences.append(part_normalized_sentences)
                else:
                    normalized_sentences.append(' '.join(part_normalized_sentences))

        else:
            raise TypeError('Unknown text type. Use strings or lists only')

        if not split_docs:
            joined_docs_texts = []
            for doc in normalized_sentences:
                for sentence in doc:
                    joined_docs_texts.append(sentence)

            return joined_docs_texts

        else:
            return normalized_sentences
