# Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. 
# Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:
# Tabuada do 2: 2 x 1 = 2 2 x 2 = 4 [...] 2 x 10 = 20

num = int(input('Escolha um número inteiro de 1 a 10: '))
fator = 1
print()
print(f'Tabuada do {num}')

while fator <= 10:
  print(f'{num} x {fator} = {num * fator}')
  fator += 1
