# Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. 
# Considere que a colônia A inicia com 4 elementos e a B com 10.

bacA = 4
bacB = 10

taxaA = 0.03
taxaB = 0.015

dias = 0

while bacA <= bacB:
  bacA *= (1 + taxaA)
  bacB *= (1 + taxaB)
  dias += 1

print(f'Irá levar {dias} dias para a colônia A igualar à colônia B, e cada colônia terá %i bactérias.' %(bacA))
#print(f'Após {dias} dias em cada colônia terá %i bactérias.' %(bacA))
#print(f'Após {dias} dias a colônia B terá {bacB} bactérias.')
