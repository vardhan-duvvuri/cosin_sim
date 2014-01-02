from math import sqrt


def dot_product(v1, v2):
   
    return sum(a * b for a, b in zip(v1, v2))


def magnitude(vector):
   
    return sqrt(dot_product(vector, vector))


def similarity(v1, v2):
   
    return dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))
