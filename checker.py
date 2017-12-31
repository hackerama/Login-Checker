import requests

list = open('lista.txt', 'r').readlines()
print list
list = [line.replace('\n', '') for line in list]
print list

for line in list:
    newline = line.split(':')
    payload = {'username' : newline[0], 'password' : newline[1]}
    req = requests.post('http://localhost/pycheecker/welcome.php', data=payload).text
    if 'Autenticado.' in req:
        print('Autenticado ==> {}|{}'.format(newline[0], newline[1]))
    else:
        print('Combinacao errada ==> {}'.format(newline[0]))


print ('Finalizado')
