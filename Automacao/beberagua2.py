import time

def lembrar(intervalo):
    contador=1

    while True:
        print('Tempo Encerrado!')
        contador=+1
        time.sleep(intervalo*5)

lembrar(1)