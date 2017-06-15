import requests
resp = requests.get('http://localhost:8005/echo/Mothra')
if resp.status_code == 200:
	print('It worked! That almost never happens!')
else:
	 print('Argh, got this:', resp.text)
