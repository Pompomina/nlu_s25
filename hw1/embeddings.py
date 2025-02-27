"""
Code for Problem 1 of HW 1.
"""
from typing import Iterable

import numpy as np


class Embeddings:
    """
    Problem 1b: Complete the implementation of this class based on the
    docstrings and the usage examples in the problem set.

    This class represents a container that holds a collection of words
    and their corresponding word embeddings.
    """

    def __init__(self, words: Iterable[str], vectors: np.ndarray):
        """
        Initializes an Embeddings object directly from a list of words
        and their embeddings.

        :param words: A list of words
        :param vectors: A 2D array of shape (len(words), embedding_size)
            where for each i, vectors[i] is the embedding for words[i]
        """
        self.words = list(words)
        self.indices = {w: i for i, w in enumerate(words)}
        self.vectors = vectors

    def __len__(self):
        return len(self.words)

    def __contains__(self, word: str) -> bool:
        return word in self.words

    def __getitem__(self, words: Iterable[str]) -> np.ndarray:
        """
        Retrieves embeddings for a list of words.

        :param words: A list of words
        :return: A 2D array of shape (len(words), embedding_size) where
            for each i, the ith row is the embedding for words[i]
        """
        return self.vectors[self.indices[words]] if isinstance(words, str) else self.vectors[[self.indices[word] for word in words if word in self.indices]]
        # raise NotImplementedError("Problem 1b has not been completed yet!")

    @classmethod
    def from_file(cls, filename: str) -> "Embeddings":
        """
        Initializes an Embeddings object from a .txt file containing
        word embeddings in GloVe format.

        :param filename: The name of the file containing the embeddings
        :return: An Embeddings object containing the loaded embeddings
        """
        # reads all lines of the file into a list
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # parses the lines to extract words and their corresponding embeddings
        words, vectors = zip(*[(line.split()[0], np.fromstring(" ".join(line.split()[1:]), sep=" ")) for line in lines])

        # embedding object
        return cls(words, np.vstack(vectors))

        # raise NotImplementedError("Problem 1b has not been completed yet!")