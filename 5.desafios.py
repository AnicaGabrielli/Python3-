'''Cria um programa qua leia o nome completo da uma pessoa a mostra:

O nome com todas as latras maiúsculas

O nome com todas minúsculas.

Quantas letras ao todo (sem considerar os paços).

Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo:'))

print(f'Your name in upper {nome.upper()} and your name in lower {nome.lower()} \n')

nome_sem_espacos = nome.replace(" ","")

print(f'Your name without spaces {len(nome_sem_espacos)}\n')

firstname = nome.split()
print(f'Your first name this is here {firstname [0]}\n')

'''Faça um programa qua leia um número de ০ a ৭৭৭৭ e  mostra na tela cada um dos digitos separados.

Ex: Digita um número: 1834

unidade: 4

dazana: 3

centana: 8

milhar: 1
'''

numero = int(input('Digite qualquer número de 0 a 9999: '))


unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f'O número da unidade é {unidade} \no da dezena é {dezena} \no da centena e {centena} \no do milhar é {milhar}\n')



'''Crie um programa qua leia o nome da uma cidade a diga se ala começa ou não com o nome "SANTO".'''

cidade = input('Digite o nome da sua cidade: ')

cidade = cidade.upper()

cidade = cidade.split()

print('SANTO' in cidade[0])


'''Crie um programa que leia o nome da uma passoa a diga se ela tem "SILVA" no nome.'''

name = input('what is your name? ')

name = name.upper()

name_in = 'SILVA' in name

print(f'o nome SILVA está no meu nome? {name_in}')
