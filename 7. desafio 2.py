"""Escreva um programa que leia um número inteiro qualquer e peça para o  usuário escolher qual será a base de concversão:
-1 para vinário
-2 para octal
-3 para Hexadecimal """

n = int(input("Digite um numero inteiro: "))
print('''Escolha uma das bases para conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input("Digite sua opção:"))
if opcao == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f"{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]} ")
else:
    print("Opção inválida.")