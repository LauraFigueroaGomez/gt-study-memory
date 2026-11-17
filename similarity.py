import numpy as np 

def cosine_similarity(a,b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    if a.shape != b.shape:
        raise ValueError("Vectors must have the same number of dimensions")
    
    dot_product = np.dot(a, b)

    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cannot compare a zero vector")
    
    return dot_product / (magnitude_a * magnitude_b)