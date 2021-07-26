termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1
while  c < 11:
    an = termo + (c-1)*razao
    print(an , '-> ' if c < 10 else '', end='')
    c += 1
print('FIM')