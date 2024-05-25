
devs = ["java", "php", "python", "golang"]
print(devs)     #oxirgi elemetni chiqaradi
devs.append("c") #oxirgi elemetni chiqaradi
print(devs)
#devs.insert(0, 123)
print(devs)
#del devs[len(devs)-1]   #indexga ko'ra elementni o'chiradi
print(devs)
#devs.remove("php")  #qiymatga ko'ra birinchi elementni o'chiradi
print(devs)
#devs.pop()      #oxirgi elementni o'chiradi va qaytaradi
#devs.pop(0)     #indexsdagi elementni o'chiradi va qaytaradi
devs.sort()
print(devs)  #ro'yxatni saralaydi
devs.sort(reverse=True)
print(devs)  #ro'yxatni teskari saralaydi
print(sorted(devs, reverse=True))
devs.reverse()      #qiymatlarni joylashuvini teskari qilib qo'yadi
print(devs)
sonlar = list(range(12, 17))  #erilgan oraliqda butun sonlar listini beradi
print(sonlar)
toqSonlar = list(range(1, 17, 2))       #bu yerda 2 ga har bir sonni ortirib beradi
print(toqSonlar)
print(max(toqSonlar))
print(min(toqSonlar))
print(sum(toqSonlar))

print(devs[0:2])        #berilgan index oralig'idagi elementlarni oladi
print(devs[:2])
print(devs[0:])
newDev = devs[:]        #devs listidan nusxa olish

tupleExp = ('du', 'se', 'cho', 'pa', 'ju', 'sha', 'ya')     #tuple o'zgartitib bo'lmaydigan ro'xat
tupleDevs = tuple(devs[:3])     #typeni tuple ga o'zgartirish
print(tupleDevs)

for dev in devs:
    print(dev, 'mening eg sevimli dasturlash tilim')

#dostlar = []
#for n in range(3):
#    dostlar.append(input(f"{n+1}. Do'stingizning ismini kiriting \n"))

#print(dostlar)


#numberOfInd = input(f"Bugun nechta odam bilan ko'rishdingiz? \n")
#people=[]

#for n in range(int(numberOfInd)):
 #   people.append(input(f"{n+1}-ko'rishgan odamingiz \n"))

#print(f"Bugungi ko'rishgan odamlaringiz ro'yxati \n {people}")

#login = input('Loginni kiriting \n')
#print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?") if login.lower()=="admin" else print(f"Xush kelibsiz, {login}!")

print(True or False)
print(True and False)
print("java" in devs)
if devs:
    print('bosh emas')
else:
    print("bosh")

#num = int(input('sonni kiriting'))

#for n in range(2, 11):
#    if num%n==0:print(f"{num} soni {n} ga bo'linadi")

talaba = {'name': 'Nodira'}
talaba['age'] = 23
print(talaba)
#del talaba['age']
#print(talaba)

for attr, item in talaba.items():
    print(attr)
    print(item)

print(talaba.get('attr', 'Bunday attribut mavjud emas'))
print(talaba.keys())

names = ['Nodira', 'Malika']

for key, value in talaba.items():
    if value in names:
        print(f"{value} ro'yxatda mavjud")

print(talaba.values())
print(sorted(talaba))       #sort by key
talaba['sertifikatlar_soni'] = 23
print(set(talaba.values()))

toys = {'car', 'car'}  #create set

print(toys)

talaba2=talaba.copy()
talaba2['age'] = 18
print(talaba2)
print(talaba)

talabalar = [talaba, talaba2]

i=0

for talaba in talabalar:
    i+=1
    print(f"{i}-talabaning ismi {talaba['name']}, yoshi {talaba['age']}da")

print(talabalar[0]['age'])

while toys:
    print(toys.pop())


