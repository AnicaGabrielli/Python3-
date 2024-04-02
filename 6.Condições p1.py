'''Exemplo ilustrativo:
if carro.esquerda():
    bloco True
else:
    bloco False'''

tempo = int(input('Digite a idade do seu carro: '))

if tempo<=3:
    print("Carro novo!")
else:
    print("Carro velho!")
print("--FIM--\n")

#Condição simplificada

tempo2 = int(input("Digite a idade do seu carro novamente: "))
print('Carro novo!' if tempo2 <<=3 else 'carro velho!')
print('---FIM---')
    