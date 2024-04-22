import pandas as pd
import numpy as np

class City:
    """
    City class to hold information about each location
    """
    def __init__(self, name, x, y, pop):
        """
        Initialization method for a City class

        Parameters
        ----------
        name : str
            The name of the City
        
        x : int | float
            The x coordinate of the city on a cartesian coordinate plane

        y : int | float
            The y coordinate of the city on a cartesian coordinate plane
        
        pop : int
            The population of the city
        """
        self.name = name
        self.x = x
        self.y = y
        self.pop = pop
    
    def __repr__(self) -> str:
        return f"{self.name}"

def _convert_to_2dcartesian(latitude, longitude):
    """
    function to convert latitude and longitude to cartesian coordinates
    """
    R = 6371
    lat_rad, lon_rad = np.deg2rad(latitude), np.deg2rad(longitude)
    x = np.cos(lat_rad) * np.cos(lon_rad)
    y = np.cos(lat_rad) * np.sin(lon_rad)
    return (x,y)

def prep_data(data = "data/de.csv", pop_limit=0):
    """
    Function to prepare the data to be used for hierarchical clustering

    Parameters
    ----------
    data : str
        path to the data to be read
    
    pop_limit : int (optional)
        the minimum amount of population that is supposed to be used when parsing the data
    
    Returns
    -------
    city_list : list
        a list of all the cities that were read from the CSV as a City class
    """
    df = pd.read_csv(data).fillna(0)
    city_list = []
    for _, row in df.iterrows():
        lat, lon = float(row["lat"]), float(row["lng"])
        pop = int(row["population"])
        if pop >= pop_limit:
            city = City(row["city"], lat, lon, pop)
            city_list.append(city)
    return city_list
