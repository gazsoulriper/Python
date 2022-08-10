# Imprir a string "Hello Python" de trás para frente usando indexação
s = "Hello Python"
s = s[ : : -1]
print(f'Utilizando indexação para escrever "{s}" ao contrário')
print()
#Usando a string "Hello Python" imprima somente "Python"
s = "Hello Python"
s = s[6 : : ]
print(f'Fatiando a string "Hello Python" para escrever somente "{s}"')
print()
# Descobrir o comprimento da string usando a função len()
s = "Hello Python"
c = len(s)
print(f'O comprimento da string "Hello Python" é de {c} caracteres')