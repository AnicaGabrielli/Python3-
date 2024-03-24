
#recebe o valor em metros e converte ele para centímetros e milímetros

metros = float(input('digite o valor em metros: '))
km = metros/1000
hm = metros/100
dm = metros/10
dc = metros*10
cm = metros*100
mm = metros*1000

print(f'O valor de {metros} metros convertido \nem centímetros é {cm} e \nem milímetros é {mm} \nem decimetros {dc}, \nem decametros {dm}, \nem hectometros {hm} , \nem kilometros{km}\n')

#recebe um número inteiro qualquer e mostra sua tabuada
n = int(input("Digite um número: "))
u = n*1
d = n*2
t = n*3
q = n*4
c = n*5
s = n*6
st = n*7
o = n*8 
nv = n*9 
dz = n*10
print('🔪'*12)
print(f'a tabuada de {n}:'+
f'{n}x1={u} \n {n}x2={d} \n {n}x3={t} \n {n}x4={q} \n {n}x5={c} \n {n}x6={s} \n {n}x7={st} \n {n}x8={o} \n {n}x9={nv} \n {n}x10={dz}')
print('🌞'*12,'\n')
#recebe um valor e mostra quantos dólares pode comprar

real = float(input('digite quantos reais voce tem: R$'))
dolar = float(input('digite o valor do dólar atualmente: '))
dolar_comprado = real/dolar

print(f'Vc consegue obter esse valor em dólares comprados: {dolar_comprado}')
