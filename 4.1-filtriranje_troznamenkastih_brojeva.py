N=int(input('Troznamenkasti broj: '))
while N <100 or N >999:
    N=int(input('Troznamenkasti broj: '))
for a in range(100,N+1):
    if a%10%3==0 and a%10!=0 and (a//100)%2!=0 and (a//10)%2!=0:
        print(a, end=' ')
