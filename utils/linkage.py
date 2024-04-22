from utils.distance import distance2d
import numpy as np

def complete_linkage(a: list, b: list, dim: int = 2) -> float:
    """
    Complete linkage 
    By default dimension = 2
    """
    maximum_distance = -np.inf
    for a_element in a:
        for b_elment in b:
            distance = distance2d(a_element, b_elment)
            if distance > maximum_distance:
                maximum_distance = distance
    return maximum_distance

def single_linkage(a: list, b: list, dim: int = 2) -> float:
    """
    Single linkage
    By default dimension = 2
    """
    minimum_distance = np.inf
    for a_element in a:
        for b_element in b:
            distance = distance2d(a_element, b_element)
            if distance < minimum_distance:
                minimum_distance = distance
    return minimum_distance

def average_linkage(a: list, b: list, dim: int = 2) -> float:
    """
    Average linkage
    By default dimension = 2
    """
    total_distance = 0
    for a_element in a:
        for b_element in b:
            distance = distance2d(a_element, b_element)
            total_distance += distance
    average_distance = total_distance / (len(a)*len(b))
    return average_distance
            