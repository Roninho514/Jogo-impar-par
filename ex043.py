peso = float(input('Digite o seu peso: '))
Altura = float(input('Digite a sua altura: '))
imc = peso/Altura**2
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 <= 25:
    print('Peso ideal')
elif imc > 25 <= 30:
    print('Sobrepeso')
elif imc > 30 <= 40:
    print('Obesidade')
else:
    print('Obsidade mórbida')
