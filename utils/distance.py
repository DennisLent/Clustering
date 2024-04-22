import numpy as np
from data.data_gen import City

def distance2d(a: City, b: City) -> float:
    """
    Calculate the cartesian distance between two points in 2d
    points are (x,y)
    """
    return np.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def distance3d(a: City, b: City) -> float:
    """
    Calculate the cartesian distance between two points in 3d
    points are (x,y,z)
    """
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2]**2 - b[2]**2))