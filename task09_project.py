# Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:
# Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
# Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
# Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco.
# Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

cand1 = 0 # Valeria 1
cand2 = 0 # Regina 2
cand3 = 0 # Mateus 3
cand4 = 0 # Ricardo 4
nulos = 0 # numero 5
brancos = 0 # numero 6

for i in range(1,21):
  voto = int(input('Digite o voto (1 a 6): '))
  if voto == 1:
    cand1 += 1
  elif voto == 2:
    cand2 += 1
  elif voto == 3:
    cand3 += 1
  elif voto == 4:
    cand4 += 1
  elif voto == 5:
    nulos += 1
  elif voto == 6:
    brancos += 1
  else:
    print('Voto inválido.')

print()
print(f'Votos na Valeria: {cand1}')
print(f'Votos na Regina: {cand2}')
print(f'Votos no Mateus: {cand3}')
print(f'Votos no Ricardo: {cand4}')
print(f'Votos nulos: {nulos} ({nulos / 20 * 100}%)')
print(f'Votos em branco: {brancos} ({brancos / 20 * 100}%)')
