import pytest

from similarity import cosine_similarity

def test_identical_vectors_have_similarity_one():
    assert cosine_similarity([1,0], [1,0]) == pytest.approx(1)

def test_perpendicular_vectors_have_similarity_zero():
    assert cosine_similarity([1,0], [0,1]) == pytest.approx(0)

def test_longer_vector_in_the_same_direction_stays_one():
    assert cosine_similarity([2, 0], [5,0]) == pytest.approx(1)

def test_zero_vector_raises():
    with pytest.raises(ValueError):
        cosine_similarity([0,0], [1,0])