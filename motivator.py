import requests


def get_quote_of_the_day(category):

    url = "https://quotes.rest/qod?language=en&category={}".format(category)
    res = requests.get(url=url)
    dict_data = res.json()
    quote = (dict_data['contents']['quotes'][0]['quote'])
    return quote

quote = get_quote_of_the_day(category="inspire")
print (quote)