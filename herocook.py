import requests
url = 'http://api.forismatic.com/api/1.0/?method=getQuote&format=text&language=ru'
resp = requests.get(url)
print(resp)
print(resp.text)

