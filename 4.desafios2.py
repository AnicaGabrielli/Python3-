import random

aluno1 = input("Digite o nome do aluno um: ")
aluno2 = input("Digite o nome do aluno dois:")
aluno3 = input("Digite o nome do aluno três: ")
aluno4 = input("Digite o nome do aluno quatro: ")

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice(alunos)

print(f' \nQuem vai apagar o quandro é: {sorteado}\n')

random.shuffle(alunos)

print(f'A ordem de quem vai apagar o quadro é a seguinte: {alunos}')

