def kopaytma (*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma = kopaytma*son
    return kopaytma

def baholar(ismlar):
    baholar = {}
    while(ismlar):
        ism = ismlar.pop()
        baho = input(f"Talaba {ism}ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar;