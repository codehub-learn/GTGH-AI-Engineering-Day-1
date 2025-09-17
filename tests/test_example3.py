import pytest
from day_1.example3 import CharEncoderDecoder, CharEmbedding
import numpy as np


# 1. Simple test for a function (CharEncoderDecoder.encode)
def test_encode_simple():
    text = "abcabc"
    encoder_decoder = CharEncoderDecoder(text)
    ids = encoder_decoder.encode(text)
    assert ids == [0, 1, 2, 0, 1, 2]

# 2. Test with fixture for encoder/decoder
@pytest.fixture
def encoder_decoder_fixture():
    text = "hello"
    return CharEncoderDecoder(text)

def test_encode_with_fixture(encoder_decoder_fixture):
    ids = encoder_decoder_fixture.encode("hello")
    assert isinstance(ids, list)
    assert all(isinstance(i, int) for i in ids)

# 3. Integration test for reading file and embedding (using tmp_path)
def test_integration_read_and_embed(tmp_path):
    # Create a temporary file
    d = tmp_path / "sub"
    d.mkdir()
    file_path = d / "test.txt"
    file_content = "test"
    file_path.write_text(file_content, encoding='utf-8')

    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    encoder_decoder = CharEncoderDecoder(text)
    ids = encoder_decoder.encode(text)
    embedding = CharEmbedding(len(encoder_decoder.chars), 2)
    embedded_vectors = embedding.embed(ids)
    assert len(embedded_vectors) == len(text)
    assert np.array(embedded_vectors).shape[1] == 2
