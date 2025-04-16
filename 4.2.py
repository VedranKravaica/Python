a=float(input('Upišite prvi realan broj: '))
b=float(input('Upišite drugi realan broj: '))
c=float(input('Upišite treći realan broj: '))
while a!=0 and b!=0 and c!=0:
    while a+b<c and a+c<b and b+c<a:
        print('Učitane stranice ne tvore trokut')
        a=float(input('Upišite prvi realan broj: '))
        b=float(input('Upišite drugi realan broj: '))
        c=float(input('Upišite treći realan broj: '))
    print('Učitane su stranice trokuta: {0:.2f} {1:.2f} {2:.2f}'.format(a, b, c))
    i=0
    j=0
    x=0
    if a+b>=c and b+c>=a and a+c>=b:
        i+=1
        x+=i
    if a==b:
            print('Trokut je istokračan')
            print('Opseg trokuta je {.2f}'.format(a*b+c))
            j+=1
            x+=j
    elif b==c:
            print('Trokut je istokračan')
            print('Opseg trokuta je {.2f}'.format(c*b+a))
            j+=1
            x+=j
    elif a==c:
            print('Trokut je istokračan')
            print('Opseg trokuta je {.2f}'.format(c*a+b))
            j+=1
            x+=j
x=i+j
print('Bilo je ukupno {0:d} trokuta od kojih je {1:d} istokračna'.format(x, j))
    
