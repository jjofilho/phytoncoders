# condicional com for para controle de fluxo determinada

# for variavel in range(10):
  #  print(variavel)

"""
for variavel in range(1, 10):
    print(variavel)

"""

"""
for variavel in range(1, 10, 3):
    print(variavel)
"""

soma = 0
for i in range(1, 4):
    nota = float(input(f'Nota {i}: '))
    soma = soma + nota
print('Média', soma/3)