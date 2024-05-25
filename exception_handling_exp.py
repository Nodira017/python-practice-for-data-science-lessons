
try:
   yosh = int (input('Yoshingizni kiriting: '))
except:
    print('Yoshingizni butun sonlarda kiritishingiz kerak!' + '\n')
    try:
        yosh = int(input('Yoshingizni qayta kiriting: '))
    except:
        print('yoshingizni 2 qayta notogri kiritganingiz sabab dastur toxtaildi')
        exit()      #stop running (same as return in java)
print(f'Siz {2024-yosh}-yilsiz;)')
