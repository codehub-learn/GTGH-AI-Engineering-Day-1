# Discussing functions for character encoding/decoding and embedding
# Refactored from example1.py to use functions for better modularity
# Reads a text file, creates character dictionaries, and generates embeddings

# import all necessary libraries
import numpy as np


# Define a function called 'read_file_to_string' that takes a filename as an argument and returns its entire content as a string.
def read_file_to_string(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


# Define a function 'create_encoder_decoder' that takes the text as an argument and returns two dictionaries: 'encoder' and 'decoder'. 
def create_encoder_decoder(text):
    chars = sorted(set(text))
    encoder = {ch: i for i, ch in enumerate(chars)}
    decoder = {i: ch for i, ch in enumerate(chars)}
    return encoder, decoder


# Define a function 'text_to_ids' that takes the text and an encoder dictionary. It should return a list of integers.
def text_to_ids(text, encoder):
    return [encoder[ch] for ch in text]


# Define a function 'create_embedding_matrix'. It takes the vocabulary size and the desired embedding dimension. It returns a numpy matrix with random values. 
def create_embedding_matrix(vocab_size, embedding_dim):
    # creates an embedding matrix with random values
    return np.random.rand(vocab_size, embedding_dim)


# Start the main execution block of the script with 'if __name__ == "__main__":'
if __name__ == "__main__":

    filename = "data/input.txt"
    embedding_dim = 2  # the dimension of the embeddings
    text = read_file_to_string(filename)
    encoder, decoder = create_encoder_decoder(text)
    embeddings_ids = text_to_ids(text, encoder)
    embedding_matrix = create_embedding_matrix(len(encoder), embedding_dim)
    embedded_vectors = [embedding_matrix[idx] for idx in embeddings_ids]

    print("Embedded vectors (πρώτα 10):\n", embedded_vectors[:10])
