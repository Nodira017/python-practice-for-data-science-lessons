from datetime import date

print('hijhv')


def count_age(birthdate):
    """to calculate age by birthdate"""
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    print(f"Age is equal to {age}")


def number_range(min, max, range):
    sonlar = [min]
    while(min<max):
        sonlar.append(min+range)
        min=min+range
    return sonlar

print(number_range(3, 15, 4))

count_age(date(2000, 1, 28))

"""talabalarga baho qo'yish"""
def baholar(ismlar):
    baholar = {}
    while(ismlar):
        ism = ismlar.pop()
        baho = input(f"Talaba {ism}ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar;

talabalar = ['Nodira', 'Sevinch', 'Muxlisa', 'Dildora']
print(baholar(talabalar[:]))   # [:] belgisi obyektni copy qiladi.
print(talabalar)

"""Moslashuvchan funksiyalar *args - tuple, **kwargs - lug'at"""

def kopaytma (*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma = kopaytma*son
    return kopaytma

print(kopaytma(1, 2, 3))

def student_data (firstname, surname, **data):
    return {
        'firstname': firstname,
        'surname': surname,
        **data
    }

print(student_data("Nodira", "Egamberdiyeva", kursi=3, yili=2000))

