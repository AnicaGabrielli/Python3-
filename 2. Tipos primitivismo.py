'''
tipos primitivos

int - 7, -6, 0, 1675
float - 4.5, 0.075, -12.667, 7.0
bool - True or False
str - "Olá", '7.4'

format - print(f'sou{nome} e tenho {idade}')
'''
#para saber o tipo
n1=input('digite um número:')
print(type(n1))
n2=int(input('digite um número:'))
print(type(n1))
n3=int(input('digite um número:'))
print(type(n1))

soma=n2+n3

print(f'a soma entre {n2} e {n3} é {soma}')

num=float(input('Digite um número: '))
print(num)

n=input('digite algo: ')
print(n.isnumeric())