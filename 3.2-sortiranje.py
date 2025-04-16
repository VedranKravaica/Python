import random
a=random.randint(11,65)
b=random.randint(11,65)
c=random.randint(11,65)
print('Izvučeni su brojevi: ',a, b, c)
if a<b and a<c:
    if b<c:
        print('Brojevi po veličini su: ',a,b,c)
    else:
        print('Brojevi po veličini su: ',a,c,b)
elif b<a and b<c:
    if a<c:
        print('Brojevi po veličini su: ',b,a,c)
    else:
        print('Brojevi po veličini su: ',b,c,a)
else:
    if a<b:
        print('Brojevi po veličini su: ',c,a,b)
    else:
        print('Brojevi po veličini su: ',c,b,a)
