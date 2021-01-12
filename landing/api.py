import requests, os
from dotenv import load_dotenv
load_dotenv()


def autoComplete(query):

        url = "https://realtor.p.rapidapi.com/locations/auto-complete"

        querystring = {"input": query}

        headers = {
            'x-rapidapi-host': "realtor.p.rapidapi.com",
            'x-rapidapi-key': os.getenv('rapid_key')
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        
        data = response.json()
        autoAddress = data['autocomplete'][0]
        address = {}
        if autoAddress:

            address['city'] = autoAddress['city']
            address['state_code'] = autoAddress['state_code']
            address['centriod'] = autoAddress['centroid']


        return address

def soldProperties(city, statecode):
    url = "https://realtor.p.rapidapi.com/properties/v2/list-sold"

    querystring = {"sort":"sold_date","city": city ,"offset":"0","state_code": statecode,"limit":"200"}

    headers = {
        'x-rapidapi-host': "realtor.p.rapidapi.com",
        'x-rapidapi-key': os.getenv('soldproperties')
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    
    return data

def propertyDetail(property_id):
    url = "https://realtor.p.rapidapi.com/properties/v2/detail"

    querystring = {"property_id": property_id}

    headers = {
        'x-rapidapi-key': os.getenv('soldproperties'),
        'x-rapidapi-host': "realtor.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    return data   

def listForSale(data, limit=50):

    url = "https://realtor.p.rapidapi.com/properties/v2/list-for-sale"

    # if int(data['price_max']) < 10:
    #     data['price_min'] = 10000000000
    # if int(data['baths_min']) == 0:
    #     data['price_min'] = 10
    # if int(data['baths_min']) == 0:
    #     data['baths_min'] = 10
    
    try:
        querystring = {
                "beds_min":data['beds_min'],
                "sort":data['sort'],
                "baths_min":data['baths_min'],
                "radius":data['radius'],
                "price_min": data['price_min'],
                "price_max": data['price_max'],
                "prop_type": data['prop_type'],
                # "is_pending": data['pending'],
                "city": data['fullAddress']['city'],
                "limit":data['limit'],
                "offset":"0",
                "state_code":data['fullAddress']['state_code']
                }

    except :
        querystring = {
                # "is_pending": data['pending'],
                "city": data['fullAddress']['city'],
                "limit":limit,
                "offset":"0",
                "state_code":data['fullAddress']['state_code']
                }

    headers = {
        'x-rapidapi-host': "realtor.p.rapidapi.com",
        'x-rapidapi-key': os.getenv('rapid_key')
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    return data   

