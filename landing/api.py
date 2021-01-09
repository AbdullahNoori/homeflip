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
        'x-rapidapi-key': "ae42631858mshd5ba8affbe71f55p14f928jsncb2c824de7d1",
        'x-rapidapi-host': "realtor.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    return data   

def listForSale(city, statecode):

    url = "https://realtor.p.rapidapi.com/properties/v2/list-for-sale"

    querystring = {
            # "beds_min":"3",
            # "sort":"price_low",
            # "postal_code":"",
            # "prop_type":"single_family%2Cmulti_family",
            # "baths_min":"2",
            # "radius":"5",
            "city": city,
            "limit":"200",
            "offset":"0",
            "state_code":statecode
            }

    headers = {
        'x-rapidapi-host': "realtor.p.rapidapi.com",
        'x-rapidapi-key': os.getenv('rapid_key')
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    return data   

