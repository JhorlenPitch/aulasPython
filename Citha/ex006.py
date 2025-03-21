import schedule
import time
import subprocess
from datetime import datetime

#Função de logging
def log_mensagem(mensagem):
    hora_atual = datetime.now().strftime("%H:%M:%S")
    print(f"[{hora_atual}] {mensagem}")

#Função que executa o seu script de análise
def executar_analise():
    log_mensagem("Executando análise de vendas...")
    
    try:
        #Chamando o script de análise
        subprocess.run(["python", "ex004.py"], check=True)  #check=True vai levantar um erro caso o subprocess falhe
        log_mensagem("Análise concluída com sucesso!")
    except subprocess.CalledProcessError as e:
        log_mensagem(f"Erro ao executar o script: {e}")

#Exibindo a hora atual ao iniciar o script
log_mensagem(f"Hora atual: {datetime.now().strftime('%H:%M')}")

#Agendar a execução do script as 9hrs todos os dias
schedule.every().day.at("09:00").do(executar_analise)

#Manter o script rodando e agendado
log_mensagem("Aguardando a execução agendada...")

while True:
    schedule.run_pending()
    time.sleep(60)  #Espera 1 minuto antes de verificar novamente