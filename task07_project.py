# Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
# Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input('Digite um número: '))
primo = True

if num <= 1:
  primo = False

else:
  for z in range(2, num):
    if num % z == 0:
      primo = False
      break

if primo:
  print(f'O número {num} é primo.')
else:
  print(f'O número {num} não é primo.')
