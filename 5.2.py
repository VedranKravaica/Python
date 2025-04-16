def provjera(a, b):
    while a<b:
        print('Neispravan unos')
        a=int(input('Unesite a: '))
        b=int(input('Unesite b: '))
    return a, b

def racun(a, b, z):
    if z=='+':
        kvz=a**2+b**2+2*a*b
        print(kvz)
    elif z=='-':
        kvm=a**2+b**2-2*a*b
        print(kvm)

def main():
    a=int(input('Unesite a: '))
    b=int(input('Unesite b: '))
    provjera(a, b)
    z=input('+ ili -: ')
    racun(a, b, z)

if __name__=='__main__':
    main()
