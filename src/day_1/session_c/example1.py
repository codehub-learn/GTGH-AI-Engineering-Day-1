# Discussing logging 
# Refactored from session_b/example2.py to use logging for better traceability

import logging
from day_1.utilities.logger import setup_logging
from day_1.utilities.logger_setup import setup_logger
import numpy as np


def read_file_to_string(filename):
    logging.info(f"Reading file: {filename}")
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    logging.debug(f"File content length: {len(content)}")
    return content


def create_char_dicts(text):
    chars = sorted(set(text))
    logging.debug(f"{len(chars)} unique characters")
    encoder = {ch: i for i, ch in enumerate(chars)}
    decoder = {i: ch for i, ch in enumerate(chars)}
    logging.debug(f"Unique chars: {chars}")
    return encoder, decoder


def text_to_ids(text, encoder):
    logging.info("Converting text to tokens and returns their ids")
    ids = [encoder[ch] for ch in text]
    return ids


def create_embedding_matrix(vocab_size, embedding_dim):
    logging.info(
        f"Creating embedding matrix: vocab_size={vocab_size}, embedding_dim={embedding_dim}"
    )
    matrix = np.random.rand(vocab_size, embedding_dim)
    return matrix


if __name__ == "__main__":
    # setup_logging()
    setup_logger()
    filename = "data/input.txt"
    embedding_dim = 2
    text = read_file_to_string(filename)
    encoder, decoder = create_char_dicts(text)
    embeddings_ids = text_to_ids(text, encoder)
    embedding_matrix = create_embedding_matrix(len(encoder), embedding_dim)
    embedded_vectors = [embedding_matrix[idx] for idx in embeddings_ids]
