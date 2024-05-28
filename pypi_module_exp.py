# pypi modules

#googletrans - used to translate texts
# intall command for googletrans: pip install googletrans==3.1.0a0
import requests
from googletrans import Translator
translator = Translator()
matn = "Nodira juda yaxshi qiz"
translated_text = translator.translate(matn, dest='ru')

print(translated_text.origin)
print(translated_text.text)
print(translated_text.src)

#BeautifulSoup - working with html text, used to extract data from webpages

from bs4 import BeautifulSoup

r = requests.get('https://kun.uz/news/list')
soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_='news-title')
print(news[0].text)
i=1
for new in news:
    print(f'{i}. {translator.translate(new.text, dest='ko').text}')
    i=i+1


#opencv - module for image recognition
#fuzzywuzzy - so'zlar to'plamidan berilgan so'zga eng o'xshash so'zni topib beradi, ikki so'zdan o'xshashlik foizini topadi...
#wxPython - grafik interfeys yaratish uchun ishlatiladi, crossPlatformali, wxFormBuilder tool orqali grafik ko'rinishida interfeysni yaratib kodni copy qilib olish mumkin



