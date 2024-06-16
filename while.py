# condicional com while para controle de fluxo indeterminado, mas não infinito
"""
numero_sorteado = 15
numero_escolhido = int(input('Informe um número entre 1 e 20: '))
if numero_sorteado == numero_escolhido:
    print('Você acertou')
else:
    print('Você errou')

# condicional com while
numero_sorteado = 15
numero_escolhido = int(input('Informe um número entre 1 e 20: '))
while numero_sorteado != numero_escolhido:
    print('Você errou! Tente novamente')
    numero_escolhido = int(input('Informe um número entre 1 e 20: '))
print('Parabéns! Você acertou')

"""

# condicional com contador
contador = 0
while contador < 11:
    print(contador)
    contador = contador +1