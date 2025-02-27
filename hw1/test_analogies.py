"""
Code for Problems 2 and 3 of HW 1.
"""
from typing import Dict, List, Tuple

import numpy as np

from embeddings import Embeddings


def cosine_sim(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Problem 3b: Implement this function.

    Computes the cosine similarity between two matrices of row vectors.

    :param x: A 2D array of shape (m, embedding_size)
    :param y: A 2D array of shape (n, embedding_size)
    :return: An array of shape (m, n), where the entry in row i and
        column j is the cosine similarity between x[i] and y[j]
    """
    # Normalize the vectors
    x_norm = x / np.linalg.norm(x, axis=1, keepdims=True)
    y_norm = y / np.linalg.norm(y, axis=1, keepdims=True)

    # Compute cosine similarity
    return np.dot(x_norm, y_norm.T)

    # raise NotImplementedError("Problem 3b has not been completed yet!")


def get_closest_words(embeddings: Embeddings, vectors: np.ndarray,
                      k: int = 1) -> List[List[str]]:
    """
    Problem 3c: Implement this function.

    Finds the top k words whose embeddings are closest to a given vector
    in terms of cosine similarity.

    :param embeddings: A set of word embeddings
    :param vectors: A 2D array of shape (m, embedding_size)
    :param k: The number of closest words to find for each vector
    :return: A list of m lists of words, where the ith list contains the
        k words that are closest to vectors[i] in the embedding space,
        not necessarily in order
    """
    sims = cosine_sim(vectors, embeddings.vectors)  # Compute cosine similarity

    # Get indices of the top-k closest words (descending similarity order)
    top_k_indices = np.argsort(-sims, axis=1)[:, :k]

    # Convert indices to words
    closest_words = [[embeddings.words[idx] for idx in row] for row in top_k_indices]

    # Sort each list lexicographically if cosine similarities are identical
    for i in range(len(closest_words)):
        closest_words[i].sort(key=lambda word: (sims[i, embeddings.indices[word]], word), reverse=True)

    return closest_words
    '''
    similarities = cosine_sim(vectors, embeddings.vectors)
    closest_words = []
    for i in range(len(vectors)):
        top_k_indices = np.argsort(-similarities[i])[:k]
        row_words = [embeddings.words[idx] for idx in top_k_indices]
        closest_words.append(row_words)
    return closest_words

    '''

    # raise NotImplementedError("Problem 3c has not been completed yet!")

# This type alias represents the format that the testing data should be
# deserialized into. An analogy is a tuple of 4 strings, and an
# AnalogiesDataset is a dict that maps a relation type to the list of
# analogies under that relation type.
AnalogiesDataset = Dict[str, List[Tuple[str, str, str, str]]]


def load_analogies(filename: str) -> AnalogiesDataset:
    """
    Problem 2b: Implement this function.

    Loads testing data for 3CosAdd from a .txt file and deserializes it
    into the AnalogiesData format.

    :param filename: The name of the file containing the testing data
    :return: An AnalogiesDataset containing the data in the file. The
        format of the data is described in the problem set and in the
        docstring for the AnalogiesDataset type alias
    """
    analogies = {}  # Dictionary to store relation type
    current_relation = None  # Keeps track of the current relation type

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().lower()
            if not line:
                continue
            # If the line starts with ":"， new relation type
            if line.startswith(":"):
                current_relation = line[1:].strip()  # Remove ":" and extra spaces
                analogies[current_relation] = []  # Initialize list for this relation type
            else:
                # analogy line with four words otherwise
                '''
                w1, w2, w3, w4 = map(str.lower, line.split())
                dataset[current_relation].append((w1, w2, w3, w4))
                '''
                words = line.split()
                if len(words) == 4:
                    analogies[current_relation].append(tuple(words))
    return analogies

# raise NotImplementedError("Problem 2b has not been completed yet!")


def run_analogy_test(embeddings: Embeddings, test_data: AnalogiesDataset,
                     k: int = 1) -> Dict[str, float]:
    """
    Problem 3d: Implement this function.

    Runs the 3CosAdd test for a set of embeddings and analogy questions.

    :param embeddings: The embeddings to be evaluated using 3CosAdd
    :param test_data: The set of analogies with which to compute analogy
        question accuracy
    :param k: The "lenience" with which accuracy will be computed. An
        analogy question will be considered to have been answered
        correctly as long as the target word is within the top k closest
        words to the target vector, even if it is not the closest word
    :return: The results of the 3CosAdd test, in the format of a dict
        that maps each relation type to the analogy question accuracy
        attained by embeddings on analogies from that relation type
    """

    return {
        relation: sum(
            w4 in get_closest_words(embeddings, [embeddings[w2] - embeddings[w1] + embeddings[w3]], k=k)[0]
            for w1, w2, w3, w4 in analogies if all(w in embeddings for w in (w1, w2, w3, w4))
        ) / len(analogies) if analogies else 0.0
        for relation, analogies in test_data.items()
    }
# raise NotImplementedError("Problem 3d has not been completed yet!")