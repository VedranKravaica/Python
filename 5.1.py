def provjera(M, N):
    if M>2 and N>M+99:
        return True
    elif M<2 and N<M+99:
        print('Učitani brojevi ne ispunjavaju uvjete!')
        M=int(input('Unesite prvi broj: '))
        N=int(input('Unesite drugi broj: '))
        return False
def ispis(M, N):
    brojac=0
    for a in range(M, N):
        if a%5==0 and not a%7==0:
            print(a,  end=' ')
            brojac+=1
    print(brojac)
def main():
    M=int(input('Unesite prvi broj: '))
    N=int(input('Unesite drugi broj: '))
    provjera(M, N)
    ispis(M, N)

if __name__ == '__main__':
    main()
    
