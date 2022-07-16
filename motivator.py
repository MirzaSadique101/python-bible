from nis import match
import requests
from twillio_conn import send_whatsapp_text,client


def get_quote_of_the_day(category):

    url = "https://quotes.rest/qod?language=en&category={}".format(category)
    res = requests.get(url=url)
    status = res.status_code
    dict_data = res.json()
    if status == 200:
        quote = (dict_data['contents']['quotes'][0]['quote'])
            
    elif status == 400:
            quote = (dict_data['error']['message'])
    else:
        print("Sorry, could not get the status code")
    return quote

quote = get_quote_of_the_day(category="inspire")
send_whatsapp_text(client,quote)