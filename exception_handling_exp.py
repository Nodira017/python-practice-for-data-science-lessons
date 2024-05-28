import json

# handle exception
try:
   yosh = int (input('Yoshingizni kiriting: '))
except:
    print('Yoshingizni butun sonlarda kiritishingiz kerak!' + '\n')
    try:
        yosh = int(input('Yoshingizni qayta kiriting: '))
    except ValueError:
        print('yoshingizni 2 qayta notogri kiritganingiz sabab dastur toxtaildi')
        exit()      #stop running (same as return in java)
else:
    print(f'Siz {2024 - yosh}-yilsiz;)\n')

# read file exception
filename = 'data.txt'
try:
    with open(filename) as f:
        file = f.read()
except FileNotFoundError:
    print(f'{filename} is not found')

# read json files exception
filenames = ['talaba.json', 'talaba0.json', 'talaba1.json']
for filename in filenames:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        pass # keyingi qadamga o'tish
    else:
        print(talaba['ism'])

# using break
while True:
    try:
        yosh = int(input('Yoshingizni kiriting: '))
    except:
        print('Yoshingizni butun sonlarda kiritishingiz kerak!' + '\n')
    else:
        print(f'Siz {2024 - yosh}-yilsiz;)\n')
        break






