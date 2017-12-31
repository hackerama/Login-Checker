#/usr/bin/python

import requests

payload  = { 'username' : 'egregora.team@gmail.com', 'password' : '@nolimits42'}
req = requests.post('https://adm.force.com/parceirosdirecionalengenharia/login', data=payload).text 

print req
