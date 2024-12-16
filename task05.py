# Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. 
# Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1.
# Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

num = int(input('Digite o número: '))
numero = num
fim = 1
fatorial = num
sequencia = ""

while num > fim:
  fatorial *= (num-1)
  sequencia += str(num) + 'x'
  num -= 1
  if num == 1:
    sequencia += '1 = '

print(f'O fatorial de {numero} é {sequencia}{fatorial}')
