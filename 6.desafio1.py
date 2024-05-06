#faça um programa em que o computador pense um numero e diga se ele é igual ao que o usuário digitou.
from random import randint
from time import sleep
computador = randint(0,5)
print('--='*20)
print("Vou pensar em um número de 0 a 5 agora, tente adivinhar!")
print('--='*20)
jogador = int(input("qual número eu pensei? "))
print("PROCESSANDO...")
sleep(4)
if computador == jogador:
    print("Parabéns, você ganhou!")
else: 
    print(f"Você perdeu pois pensei no numero {computador} e não no número {jogador}")3
