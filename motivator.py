import requests

url = "https://quotes.rest/qod?language=en"
res = requests.get(url=url)
print (res)
data = res.json()
print(type(data))
#print(data['contents']['quotes'][0]['quote'])

dict_data = data

print (dict_data)

#print (dict_data['contents']['quotes'][0]['quote'])