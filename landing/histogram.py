import json, requests

class Histogram(object):

    def __init__(self, data):
        self.data = data

    
    def getHistogram(self):
        hist = {"top_areas": {}, "price": {}, "prop_type": {}, "beds": {}, "baths": {}, 
                "year_built": {}, "neighborhood_name": {}, "postal_code": {}, 
                "property_count": 0
                }
