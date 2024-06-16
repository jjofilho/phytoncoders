# Conversão de tipos

idade = '47'
numero1 = '20'
numero2 = '30'

print(idade, type(idade))
print(numero1 + numero2)

# recebe um dado float por conversão de forma explícita

idade_inteira = int(idade)
print(idade_inteira)

# int()
# str()
# float()
# bool()

# recebe um dado string por padrão
altura = input('Qual é a sua altura? ')
print(altura, type(altura))

# recebe um dado float por conversão de forma implícita
altura = float(input('Qual é a sua altura? '))
print(altura, type(altura))