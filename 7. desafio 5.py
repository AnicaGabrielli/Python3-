"""Faça um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média, mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5: reprovado.
- média entre 5 e 6.9: recuperação.
- média 7 ou superior: Aprovado. """

nota1 = float(input('Digite sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))
media = (nota1+nota2)/2
print(f'Sua média foi {media}.')
if media < 5:
    print('Infelizmente você foi REPROVADO.')
elif media >=5 and media <= 6.9:
    print('Quase deu meu amigo. Você está de RECUPERAÇÃO.')
elif media >=7:
    print('Parabéns. Você foi aprovado.')
