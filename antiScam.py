import requests
import os
import random

random.seed = (os.urandom(1024))

url = raw_input("Enter fake form url's : ")
times = int(raw_input("How many times : "))

for i in range(1, times+1):
	number =  random.randint(1000000000, 9999999999)
	code = random.randint(100000, 999999)

	requests.post(url, allow_redirects=False, data={
		'id': number,
	 	'pw': code,
        'submit': 'Envoyer'
 	})

	print '%s - Sending id: (%s) and password: (%s)' % (i, number, code)
