import datetime
import json
import re
from pprint import pprint
import requests

#datetime
hozir = datetime.datetime.now()
print(hozir)
print(hozir.date())
print(hozir.year)
print(hozir.month)
print(hozir.day)
print(hozir.time())
print(hozir.hour)
print(hozir.minute)
print(hozir.second)
print(hozir.second)

sevinch_opa_birth = datetime.date(2024, 7, 28)
today = datetime.date.today()
kun = sevinch_opa_birth-today

print(f'Tugilgan kunga {kun.days} kun qoldi')

#pprint
filename = 'talaba.json'
with open(filename) as f:       #get file
    talaba = json.load(f)       #read file
pprint(talaba)

r = requests.get('https://api.github.com')      #get request
pprint(r.json())

#regex
word1 = 'Nodira'
word2 = 'Malika'
word3 = 'Namuna'

temp = '^N....a$'
print(re.match(temp, word1))
print(re.match(temp, word2))
print(re.match(temp, word3))

#iHateRegex - website for regex templates

text = "Python.hi@gmail.com dasturlash tili yildan-yilga      test@dsf.uz ommalashib bormoqda. test@gmail.com Bunga birinchi navbatda Pythonning sodda va n.egamberdiyeva@gmail.com tushunarli sintaksi sabab bo'lsa, ikkinchi va ehtimol eng ko'zga ko'ringan sabab bu Pythonning keng qamrovli kutubxonalar to'plamidir. "
email_temp = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

print(re.findall(email_temp, text))     #return array of matched words

password_temp = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
while True:
    pwrd = input('Enter password: ')
    if re.match(password_temp, pwrd):
        print(pwrd)
        break
    else:
        print('Minimum eight characters, at least one upper case English letter, one lower case English letter, one number and one special character')









