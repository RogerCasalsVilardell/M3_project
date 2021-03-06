import numpy as np

def histogram_intersection_kernel(a, b):
    K = np.empty(shape=(a.shape[0], b.shape[0]), dtype=np.float32)
    for i in range(a.shape[0]):
        K[i] = np.sum(np.minimum(a[i], b), axis=1)
    return K

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)