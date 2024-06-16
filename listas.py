# Listas

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 9.7, 8.2]

# Criando listas
lista = []
lista = list()
lista =[47, 'João', 1.71, True]
lista_de_lista = [10, [1, 2, 3]]

# indexação e slices (fatiamento)
lista =[47, 'João', 1.71, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1]) # acessa o último elemento da lista -2 (penúltimo), etc
print('---')

# slices
lista = [10, 20, 30, 40, 50, 60, 70, 80]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])
print(lista[:-1])
print(lista[3:-2])
print('---')

# interações com FOR
# 1. utilizando os próprios elementos da lista
for elemento in lista:
    print(elemento)
print('---')

# 2. utilizando os índices
print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(i)
print('---')

for i in range(len(lista)):
    print(lista[i])
print('---')

# Métodos de listas

lista = [1, 3, 12, 8, 2]

# append - adiciona elelmento ao final da lista
# lista antes do append
print('Antes do APPEND ', lista)
print('---')

lista.append(3)
print('Depois do APPEND ', lista)
print('---')

# insert - insere elemento na posição de índice indicada
lista.insert(2, 10) # 2 => posição, 10 => elemento a ser inserido
print('Depois do INSERT ', lista)
print('---')

# extend - concatena uma lista ao final de outra lista 
lista2 = [4, 5, 6]
lista.extend(lista2)
print('Depois do EXTEND ', lista)
print('---')

# pop - remover o elemento indicado ou, se não indicado, o último
lista.pop()
print('Exclui o último elemento ', lista)
print('---')

lista.pop(0)
print('Exclui o elemento de índice indicado ', lista)
print('---')

# remove - remove o primeiro valor indicado
lista.remove(3)
print('Depois do REMOVE ', lista)
print('---')

# count - contagem de elementos
print('Quantidade de 2 na lista: ', lista.count(2))
print('---')

# index - retorna o índice do elemento solicitado
print('Índice do elemento 12: ', lista.index(12))
print('---')

# sort - ordena lista
lista.sort()
print('Lista ordenada com SORT: ', lista)
print('---')

# Funções para listas

# len - tamanho da lista
print('Tamanho da lista com LEN ', len(lista))
print('---')

# sum - soma todos os elementos da lista
print('Soma dos elementos da lista com SUM ', sum(lista))
print('---')

# max e min - retorna o maior e o menor valor entre os elementos da lista
print('Maior valor da lista com MAX: ', max(lista))
print('---')

print('Menor valor da lista com MIN: ', min(lista))
print('---')

      

