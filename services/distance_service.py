from math import sqrt

def calculate_distance(start,end):
    return sqrt(
        (end[0] - start[0])**2 +
        (end[1] - start[1])**2
    )