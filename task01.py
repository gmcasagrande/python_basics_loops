# Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print()
print(f'A sequência entre os números {num1} e {num2} será:')
if num1 < num2:
  for contador in range((num1+1), num2):
    print(contador)
else:
  for contador in range((num2+1), num1):
    print(contador)
