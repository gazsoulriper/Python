# acrescentar um item em uma lista com o comando append
lst = ['a', 'g', 'j', 'z', 'b', 'w', 'b']
lst.append('acabou')
print(lst)
print()
# utilize o comando pop para retirar o indice 0 da lista
lst = ['a', 'g', 'j', 'z', 'b', 'w', 'b', 'acabou']
lst.pop(0)
print(lst)
print()
#utilize sort para ordenar a lista
lst = ['a', 'g', 'j', 'z', 'b', 'w', 'b', 'acabou']
lst.sort()
print(lst)
print()
# utilize reverse para inverter a lista
lst = ['a', 'g', 'j', 'z', 'b', 'w', 'b', 'acabou']
lst.reverse()
print(lst)
print()
#listas aninhadas, colocar uma lista dentro de outra. É possivel criar uma matriz
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]
matriz = [lst1, lst2, lst3]
print(matriz)