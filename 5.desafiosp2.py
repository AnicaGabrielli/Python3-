"""Faça um programa que leia uma frase palo teclado e mostra:

Quantas vezes aparece a letra "A".

Em que posição ela aparace a primaira VEZ.

Em que posisño ala aparaca a última vez."""


nome = str(input('Digite seu nome: ')).upper().strip()
print(f'A letra a aparece {(nome.count("A"))} vezes.\n')
print(f"A primeira posição em que a letra A aparece é {(nome.find('A')+1)}")
print(f"A última posição em que a letra A aparece é {(nome.rfind('A')+1)}")
