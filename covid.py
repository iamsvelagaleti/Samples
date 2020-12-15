import requests
from bs4 import BeautifulSoup

def lambda_caller():
    response = {}
    response['statusCode'], response['headers'], response['body'] = 200, {}, {}
    response['headers']['Content-Type'] = 'application/json'
    
    url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
    html = BeautifulSoup(requests.get(url).text, 'html5lib')

    for index, each in enumerate(html.find_all('tr')[1:]):
        each = each.find_all('td')
        response['body'][index+1] = {
            'country' : each[0].text,
            'cases' : each[1].text,
            'deaths' : each[2].text,
            'continent' : each[3].text
        }
    return response
