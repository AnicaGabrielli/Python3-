#tocar música mp3 

import pygame
#iniciar o pygame
pygame.init()
#loadar a música
pygame.mixer.music.load('ex01.mp3')
#dar o play na música
pygame.mixer.music.play()
#verificar repetidamente se a música está tocando 
while pygame.mixer.music.get_busy():
    #verificando a cada dez segundos a condição
    pygame.time.Clock().tick(10)
    
pygame.mixer.quit
pygame.quit

'''
Claro! O comando `while` é uma estrutura de controle de fluxo em Python que permite repetir um bloco de código enquanto uma condição específica for verdadeira. Aqui está a sintaxe básica:

```python
while condição:
    # código a ser executado enquanto a condição for verdadeira
```

O bloco de código dentro do `while` é repetido continuamente enquanto a condição especificada for verdadeira. Assim que a condição se tornar falsa, a execução do bloco de código dentro do `while` é interrompida e o controle do programa é transferido para a próxima instrução após o `while`.

No contexto do código fornecido:

```python
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
```

O loop `while` verifica continuamente se a música ainda está tocando, verificando a condição `pygame.mixer.music.get_busy()`. Esta função retorna `True` se a música estiver tocando e `False` se a música tiver terminado. Portanto, enquanto a música estiver tocando (ou seja, `pygame.mixer.music.get_busy()` retorna `True`), o bloco de código dentro do `while` é executado repetidamente. 

Dentro do loop, `pygame.time.Clock().tick(10)` é chamado para controlar a taxa de atualização do loop. Isso basicamente faz com que o loop espere um curto período de tempo antes de verificar novamente se a música ainda está tocando. Nesse caso, espera-se 10 milissegundos antes de verificar novamente.

Assim que a música terminar de tocar e `pygame.mixer.music.get_busy()` retornar `False`, o loop `while` será interrompido e o programa continuará executando as instruções seguintes, que encerram o mixer de áudio e o Pygame.

As duas últimas linhas do código são responsáveis por encerrar o mixer de áudio do Pygame e o próprio Pygame. Vamos examinar cada linha:

```python
pygame.mixer.quit()
pygame.quit()
```

1. `pygame.mixer.quit()`: Este comando encerra o mixer de áudio do Pygame. O mixer de áudio é responsável por reproduzir e controlar os sons e músicas no Pygame. Ao chamar `pygame.mixer.quit()`, você está encerrando todas as operações relacionadas ao áudio que estavam sendo executadas pelo Pygame.

2. `pygame.quit()`: Esta linha encerra o Pygame completamente. Ao chamar `pygame.quit()`, você está encerrando todas as funcionalidades do Pygame que foram inicializadas anteriormente com `pygame.init()`. Isso libera os recursos usados pelo Pygame e encerra o programa de maneira limpa.

Juntas, essas duas linhas garantem que todos os recursos do Pygame relacionados ao áudio e ao próprio Pygame sejam liberados adequadamente quando o programa terminar de executar. Isso é importante para garantir que não haja vazamentos de memória ou problemas persistentes após a execução do código.
'''