# Basic Python syntax and operations

# Creating a simple character-level embedding from a text file

import numpy as np


filename = "data/input.txt"

# Read the text file
with open(filename, "r", encoding="utf-8") as f:
    text = f.read()
print(f"File content length: {len(text)}")

# Create character encoder and decoder
chars = sorted(set(text))
encoder = {ch: i for i, ch in enumerate(chars)}
decoder = {i: ch for i, ch in enumerate(chars)}
print(f"{len(chars)} Unique chars:\n{chars}")
print("-" * 30)

# Convert text to tokens and their IDs
ids = [encoder[ch] for ch in text]
print(f"First 10 ids: {ids[:10]}")
print("-" * 30)

# Define embedding dimension
embedding_dim = 2

# Create an embedding matrix
embedding_matrix = np.random.rand(len(encoder), embedding_dim)
print(f"Embedding matrix shape: {embedding_matrix.shape}")
print("-" * 30)

# Convert character IDs to embedded vectors
embedded_vectors = [embedding_matrix[idx] for idx in ids]
print(f"Embedding Martix: {embedded_vectors[:10]}")
print("-" * 30)

print(f"Encoder: {encoder}")
print("-" * 30)

print(f"Decoder: {decoder}")
print("-" * 30)

print(f"Embedded vectors (first 10): {embedded_vectors[:10]}")
