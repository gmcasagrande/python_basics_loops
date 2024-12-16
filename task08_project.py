# Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. 
# Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. 
# Encerre a entrada de dados com um número negativo.

idade = int(input('Digite a idade (ou um número negativo para encerrar): '))

contador0a25 = 0
contador26a50 = 0
contador51a75 = 0
contador76a100 = 0

while idade > 0:
  if idade > 0 and idade <= 25:
    contador0a25 += 1
  elif idade >= 26 and idade <= 50:
    contador26a50 += 1
  elif idade >=51 and idade <=75:
    contador51a75 += 1
  elif idade >= 76 and idade <= 100:
    contador76a100 += 1

  idade = int(input('Digite a idade (ou um número negativo para encerrar): '))

print('As quantidades de pensionistas estão distribuídos no grupos de idades:')
print(f'Até 25 anos: {contador0a25}')
print(f'De 26 a 50 anos: {contador26a50}')
print(f'De 51 a 75 anos: {contador51a75}')
print(f'De 76 a 100 anos: {contador76a100}')
