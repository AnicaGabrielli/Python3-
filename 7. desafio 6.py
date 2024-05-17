'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: mirin
- até 14 anos : infantil
- até 19 anos: junior
- até 25: sênior
- acima: MASTER
'''
from datetime import datetime
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual-ano_nascimento
if idade <= 9 :
    print("MIRIN")
elif idade > 9 and idade <=14:
    print('INFANTIL')
elif idade > 14 and  idade <=19:
    print("JUNIOR")
elif idade > 19 and  idade <=25:
    print("SÊNIOR")
else:
    print('MASTER')