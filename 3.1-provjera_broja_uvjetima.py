import random
a=random.randint(1,1000)
if a<=100:
    print('Broj je manji od 100')
elif a>500:
    print('Broj je veći od 500')
elif 100<=a<=300:
    print('Broj je unutar intervala 100 i 300')
else:
    print('Generiran je broj: ',a)
print('Broj je: ',a)
