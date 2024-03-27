frase = "Curso em vídeo Python"
#cada carácter, incluindo os espaços, ocupam um micro espaço na memória. Esses espaços são numerados começando do número zero e recebem o nome de indices.

#Fatiamento - o faturamento serve para coletar partes da cadeia de texto

print(frase[9],'\n')

print(frase[9:13], '- nesse caso, o fatiamento não pega o carácter do índice treze. É sempre um a menos. \n ')

print(frase[9:21],'\n')
#nesse caso vai saltar as casas de dois em dois

print(frase[9:21:2],'\n')

#nesse caso, quando não se coloca de onde a string começa, ela inicia no índice zero

print(frase[:5])

#nesse caso ocorre ocorre o mesmo raciocínio

print(frase[15:])

#mostra do nove até o final e salta três casas 

print(frase[9::3])

#Analise - Análise de algumas informações sobre as string

# mostra o comprimento
print(len(frase))
#conta a quantidade de alguma coisa dentro da frase. o segundo exemplo faz essas contagem já com o fatiamento 
print(frase.count('o'),'\n')
print(frase.count('o',0,13))
#mostra a posição do que foi especificado dentro da fase
print(frase.find('deo'))
#retorna -1 para a estring não encontrada 
print(frase.find('Android'))
#verifica se algo existe ou não na frase

print('Curso' in frase)

#Trasformaçāo 
#essa função substitui I'm conjunto de caracteres por outro

print(frase.replace('Pythaon','Android'))

#Coloca as letras em maiúsculo

print(frase.upper())

#Transforma as letras em minúsculo

print(frase.lower())

#Coloca tudo em minúsculo, deixando apenas a primeira letra em maiúsculo

print(frase.capitalize())

#Analiza cada palavra, deixando a inicial maiúscula

print(frase.title())

#Remove todos os espaços inúteis no início e no final da string. Ao se colocar o r de right, ele remove somente os espaços finais ou da direita. Ao se colocar o l de left, ele remove somente os espaços iniciais ou da esquerda.

print(frase.strip())


#Divisao
#O split divide a cadeia de carácter de acordo com cada palavra gerando, assim, uma nova lista. 

print(frase.split())

# Junta as palavras separadas pelo split e coloca traços entre elas.
frase = frase.split()

print('-'.join(frase),'\n')

#testes

print("""Entendo que você está interessado em explorar o tema do "sexo selvagem". É importante notar que esse termo pode ter diferentes interpretações e significados para pessoas diferentes. Geralmente, ele é associado a uma atividade sexual intensa, apaixonada e até mesmo mais agressiva. Vou criar um texto que explora esse conceito de forma respeitosa e informativa.

**Sexo Selvagem: Explorando a Paixão e a Intensidade na Sexualidade Humana**

O sexo é uma parte fundamental da experiência humana, que pode ser expressa de várias formas, incluindo aquelas que são consideradas mais "selvagens". Quando falamos de sexo selvagem, estamos nos referindo a uma expressão intensa e apaixonada da sexualidade, onde os instintos primários e a energia sexual são liberados de forma vigorosa e sem inibições.

Para muitas pessoas, o sexo selvagem é uma forma de escapar das restrições sociais e das expectativas culturais sobre como devemos nos comportar na intimidade. É uma oportunidade de se conectar com um parceiro de maneira visceral e profunda, explorando fantasias, desejos e limites físicos e emocionais.

No entanto, é essencial enfatizar que o sexo selvagem deve sempre ser consensual e seguro para todos os envolvidos. Embora possa envolver elementos de dominação, submissão ou até mesmo certa dose de agressividade consentida, o respeito mútuo e a comunicação clara são fundamentais para garantir uma experiência positiva para ambas as partes.

É importante entender que a intensidade do sexo selvagem pode variar de pessoa para pessoa e de relacionamento para relacionamento. O que pode ser considerado selvagem para alguns pode não ser o mesmo para outros. Além disso, nem todo mundo se sente confortável ou interessado nesse tipo de atividade sexual, e isso é perfeitamente válido. A diversidade de preferências e limites é parte do que torna a sexualidade humana tão rica e complexa.

Explorar o sexo selvagem pode envolver experimentar novas posições, incorporar brinquedos sexuais, explorar o BDSM (Bondage, Disciplina, Dominação, Submissão, Sadismo e Masoquismo) de forma segura e consensual, ou simplesmente deixar-se levar pela paixão e pela energia do momento.

É importante lembrar que o sexo selvagem não é exclusivo de relacionamentos de longo prazo ou de casais. Pode ser experimentado de forma igualmente intensa e emocionante em encontros casuais, desde que haja respeito mútuo e consentimento claro.

Em última análise, o sexo selvagem é sobre liberdade, paixão e entrega mútua. É uma oportunidade de explorar os limites do prazer e da intimidade de uma maneira que seja autêntica e satisfatória para todos os envolvidos. Desde que seja praticado com responsabilidade, respeito e comunicação aberta, pode ser uma experiência incrivelmente enriquecedora e gratificante na jornada sexual de uma pessoa.""")