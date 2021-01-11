import json, requests, os

class Histogram(object):

    def __init__(self, data):
        self.data = data

    
    def getHistogram(self):
        hist = {"top_areas": {}, "price": {}, "prop_type": {}, "beds": {}, "baths": {}, 
                "year_built": {}, "neighborhood_name": {}, "postal_code": {}, 
                "property_count": 0
                }


        # get top 3 areas lat and long by zip


        for home in self.data["properties"]:
            if 'prop_type' in home.keys():
                if home['prop_type'] in hist['prop_type']:
                    hist['prop_type'][home['prop_type']] += 1
                else:
                    hist["prop_type"][home['prop_type']] = 1

            if 'beds' in home.keys():
                if home['beds'] in hist["beds"]:
                    hist["beds"][home['beds']] += 1
                else:
                    hist["beds"][home['beds']] = 1

            if 'baths' in home.keys():
                if home['baths'] in hist['baths']:
                    hist['baths'][home['baths']] += 1
                else:
                    hist['baths'][home['baths']] = 1

            if 'year_built' in home.keys():
                if home['year_built'] in hist['year_built']:
                    hist['year_built'][home['year_built']] += 1
                else:
                    hist['year_built'][home['year_built']] = 1

            if 'neighborhood_name' in home['address'].keys():
                if home['address']['neighborhood_name'] in hist['neighborhood_name']:
                    hist['neighborhood_name'][home['address']['neighborhood_name']] += 1
                else:
                    hist['neighborhood_name'][home['address']['neighborhood_name']] = 1

            if 'postal_code' in home['address'].keys():
                if home['address']['postal_code'] in hist['postal_code']:
                    hist['postal_code'][home['address']['postal_code']] += 1
                else:
                    hist['postal_code'][home['address']['postal_code']] = 1
            
            if 'price' in home.keys():
                if home['price'] in hist['price']:
                    hist['price'][home['price']] += 1
                else:
                    if not bool(hist['price']):
                        hist['price'][home['price']] = 1
                    else:
                        for price in sorted(hist['price'].keys()):
                            if home['price'] > price + 5000 or home['price'] < price - 5000:
                                hist['price'][home['price']] = 1
                            else:
                                hist['price'][price] += 1

            hist['property_count'] += 1


        # prices = sorted(hist['price'].keys())

        sort_codes = sorted(hist['postal_code'].items(), key=lambda x: x[1], reverse=True)

        count = 0
        for code in sort_codes:
            code_result = self.autoComplete(code[0])
            result = code_result["autocomplete"][0]
            hist["top_areas"][result["postal_code"]] = {"lat": result["centroid"]["lat"], "lng": result["centroid"]["lon"]}
            if count == 3:
                break
            count += 1


        return hist

    def autoComplete(self, query):

        url = "https://realtor.p.rapidapi.com/locations/auto-complete"

        querystring = {"input": query}

        headers = {
            'x-rapidapi-host': "realtor.p.rapidapi.com",
            'x-rapidapi-key': os.getenv('rapid_key'),
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        # print(response.text)
        return response.json()