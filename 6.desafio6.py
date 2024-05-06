#faça um programa que leia tres numeros e diga qual é o maior e o menor valor.

a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f"O menor valor é {menor}")

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f"O maior valor é {maior}")
