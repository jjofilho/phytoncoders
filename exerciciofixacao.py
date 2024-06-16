"""
# operadores 
x = 4.2
y = 10

var = x * y

print(type(var))

"""
"""# se número inteiro é psoitivo/negativo e par/ímpar
x = int(input("Digite um número inteiro: "))

if x < 0:
    resp1 = "negativo"
else:
    resp1 = "positivo"
    
if x % 2 == 0:
    resp2 = "par"
else:
    resp2 = "impar"
    
print('O número {} é {} e {}.'.format(x, resp1, resp2))"""

"""# É muito frequente o uso de programação para a automação de tarefas repetitivas, sendo possível devido às estruturas de repetição. Em python, uma dessas estruturas é o laço while, que determina que um bloco de código seja repetido enquanto uma dada condição for verdadeira. Observe o código a seguir:
cont = 0
resultado = 0
n = 10
while cont != n:
    print(cont)
    resultado = resultado + 1/(2**cont)
    print(resultado)
    cont = cont + 1
print(resultado)"""

""" # Quando queremos utilizar o for explicitamente como um laço de repetição, é muito comum utilizarmos a estrutura acima, com o auxílio do iterador range(). No entanto, o mesmo comportamento é possível se nos aproveitarmos do fato de que o for percorre qualquer iterável. Sabendo disso, das alternativas a seguir, qual é a única que NÃO reproduz o mesmo resultado que o trecho acima?
for i in range(10):
   print("Olá, mundo!") 
print('---')

for i in "let's code":
  print("Olá, mundo!")
print('---')

for i in " "*10:
    print("Olá, mundo!")
print('---')

for i in range(10, 20, 1):
    print("Olá, mundo!")
print('---')

for i in [10]:
    print("Olá, mundo!")
print('---')

for _ in [10]*10:
    print("Olá, mundo!")
print('---')"""

# Qual deve ser o valor de A, B, C e D, respectivamente,
# para que o código acima gere a 
# seguinte lista_final: [10, 10, 14, 6, 42, 126, 8, 10, 26]?

lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:

    if item % 2 == 0:

        if item < 0:

            lista_final.append(-item)
    
        else:

            lista_final.append(item)
    else:

        if item < 0:
            
            lista_final.append(-2*item)
    
        else:

            lista_final.append(2*item)
print(lista_final)

# Output desejado:
# > ['coelho', 'macaco', 'girafa']
# > 3
# > 0

animais = ['gato', 'coelho', 'macaco', 'girafa']
animais.remove('gato')
print(animais)
print(len(animais))
print(animais.index('coelho'))