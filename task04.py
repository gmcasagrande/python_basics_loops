# Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. 
# A leitura deve ser encerrada ao ser enviado o valor -273°C.

temperatura = float(input('Insira a temperatura em Celsius (-273 para encerrar a leitura): '))
contadora = 0
soma = 0

while temperatura > -273:
    soma += temperatura
    contadora += 1
    temperatura = float(input('Insira a temperatura em Celsius (-273 para encerrar a leitura): '))

media = soma / contadora

print('A média das temperaturas é %.2f' %(media))
