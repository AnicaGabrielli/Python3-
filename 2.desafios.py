algo = input('digite algo: ')
print('o tipo primitivo desse dado é',type(algo))

print('Esse dado é numérico:',algo.isnumeric())

print('Esse dado é alfanumérico?',algo.isalnum())

print('Esse dado é alpha:' ,algo.isalpha())

print('Esse dado só contém espaços:', algo.isspace())

print('Esse dado só contém maiúsculas:',algo.isupper())

print('Esse dado só contém minusculas:',algo.islower())

print("Esse dado está capitalizado:", algo.istitle())
