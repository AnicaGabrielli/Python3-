'''escreva um programa que receba 2 números inteiros e compare-os, mostrando na tela  uma mesagem. 
- o primeiro valor é maior
- o segundo valor é maior
- Não existe valor maior'''
num1 = int(input("Digite um valor: "))
num2 = int(input("Digite um segundo valor: "))
if num1>num2:
    print('O primeiro valor é maior')
elif num2>num1:
    print('O segundo valor é maior')
else:
    print('Os valores são iguais')