'''
+ = soma 
- = Subtração 
* = Multiplicação 
/ = divisão 
** = potenciação 
// = divisão inteira 
% = Módulo
Ordem de presidência:
1- ()
2- **
3- * / // % (quem aparecer primeiro)
4- + - 
'''
#consegue-se fazer isto 
nome = str(input('qual seu nome? '))
print(f'prazer em conhecer vc {nome:^25}')
print('oi'*2)

print(5+2, 5-2, 5*2, 5/2, 5**2,  5//2, 5%2)
print('outra forma de fazer o cálculo de potência pow(x,y). veja: ')
n1=float(input('Digite um número: '))
n2=float(input('digite o número da potência:'))
resultado = pow(n1,n2)
print(f'O resultado, utilizando o cálculo pow({n1},{n2}) é {resultado}')

s = n1+n2
d = n1-n2
p = n1*n2
q = n1/n2

print(f'a soma é {s},\n a diferença {d},\n o produto {p}, \n o quociente {q:.2f}', end=' >>>')
print('Essa linha não foi quebrada')
