a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a Razão desse termo: '))
n = 1
for n in range(1,11):
    an = a1 + (n-1)*r
    print(an, end=' ')
