import time
from plyer import notification

def lembrar_beber_agua(intervalo):
    while True:
        notification.notify(
            title="💧 Lembrete de Hidratação",
            message="Beba um copo de água! Sua saúde agradece. 💙",
            timeout=10  #some depois de 1 segundos
        )
        time.sleep(intervalo)  #espera o tempo definido

lembrar_beber_agua(20)