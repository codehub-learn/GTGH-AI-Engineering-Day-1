# Character encoding/decoding and embedding using classes for modularity and reuse

import numpy as np

class CharEncoderDecoder:
    # Initializes encoder and decoder dictionaries from input text
    def __init__(self, text):
        self.chars = sorted(set(text))
        self.encoder = {ch: i for i, ch in enumerate(self.chars)}
        self.decoder = {i: ch for i, ch in enumerate(self.chars)}

    # Encodes text into list of integer IDs
    def encode(self, text):
        return [self.encoder[ch] for ch in text]

    # Decodes list of IDs back into text
    def decode(self, ids):
        return "".join([self.decoder[i] for i in ids])


class CharEmbedding:
    # Initializes random embedding matrix for given vocab size and dimension
    def __init__(self, vocab_size, embedding_dim=2):
        self.embedding_dim = embedding_dim
        self.embedding_matrix = np.random.rand(vocab_size, embedding_dim)

    # Returns embedding vectors for given list of IDs
    def embed(self, ids):
        return [self.embedding_matrix[idx] for idx in ids]


if __name__ == "__main__":
    # Main execution: reads text, encodes it, embeds it, and prints first 10 vectors
    filename = "data/input.txt"  # Change if needed
    embedding_dim = 2

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    encoder_decoder = CharEncoderDecoder(text)
    ids = encoder_decoder.encode(text)

    embedding = CharEmbedding(len(encoder_decoder.chars), embedding_dim)
    embedded_vectors = embedding.embed(ids)

    print(f"Embedded vectors (first 10):\n {embedded_vectors[:10]}")
