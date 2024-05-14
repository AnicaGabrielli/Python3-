'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com suaidade, se ele vai se alistar ao servgiço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.'''
nascimento = int(input('Digite seu ano de nascimento: '))
from datetime import datetime
ano_atual = datetime.now().year
idade = ano_atual - nascimento
if idade == 18:
    print("JÁ É HORA. Parabéns, você tem que se alistar. ")
elif idade < 18:
   
    print(f'INFELIZMENTE VOCÊ AINDA NÃO É MACHO!Faltam {18 - idade} anos para você se alistar.')
elif idade > 18:
    print(f'BORA VAGABUNDO! Já passaram {idade-18} anos do seu alistamento.')
    


