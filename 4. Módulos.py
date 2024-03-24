# módulos ou pacotes
'''
 exemplos ilustrativos:
    
    - Para importar a biblioteca de bebidas 
    import bebidas
    
    - Para usar a cachaça (uma bebida específica e somente ela) da biblioteca de bebidas: 
    
    from bebida import cachaça '''
''' 
math

ceil - arredondamento para cima
floor - arredondamento para baixo
trunc - Elimina os números após a vírgula
pow(X,Y) - potência 
sqrt - Calcula raiz quadrada
factorial - calcula o fatorial de um número 

'''
import math

num = int(input("digite um número: "))
raiz = math.sqrt(num)
print(f'a raiz quadrada de {num} é igual a {math.floor(raiz):.2f}\n')

#Inportando um comando específico

from math import sqrt,floor

num = int(input("digite um número: "))
raiz = sqrt(num)
print(f'a raiz quadrada de {num} é igual a {floor(raiz):.2f}\n')

# a função random mostra números aleatórios

import random

numero_qualquer = random.random()
print(numero_qualquer,'\n')

numero_qualquer_2 = random.randint(3,90)
print(numero_qualquer_2)

# Para vc importar bibliotecas que não estão no python mais foram criadas, é nescessário ir na documentação e procurar a parte de pyPI. Depois disso, é nescessário somente instalar no terminal e usar normalmente.
print("Olá mundo: \U0001F30E")

'''
*Esse código está dando erro 
import emoji

print(emoji.emojize("Olá mundo: sunglasses", use_aliases = True))
'''