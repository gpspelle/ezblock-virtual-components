import json
import requests
import pandas as pd
import os

class GPS():
    def __init__(self, coordinates_source='https://api.3geonames.org/.json?randomland=yes'): 
        res = requests.get(coordinates_source).json()
        self.coordinates = { "lat": res['nearest']['latt'], "lng": res['nearest']['longt'] }

    def get_coordinates(self):
        return self.coordinates

# Usage example of a geolocalizer
# localizer = GPS()
# lat, long = localizer.get_coordinates()
# print(lat, lng)
