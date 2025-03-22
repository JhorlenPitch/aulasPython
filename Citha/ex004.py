import pandas as pd
import smtplib
import os
from email.message import EmailMessage

#Ler o arquivo CSV e processar os dados
df = pd.read_csv("frutas.csv", delimiter=";")

#Criar resumo por produto
resumo = df.groupby("Produto", as_index=False)["Total Vendido Por Produto"].sum()

#Salvar no Excel
arquivo_excel = "relatorioEnviar.xlsx"
with pd.ExcelWriter(arquivo_excel, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Detalhado", index=False)
    resumo.to_excel(writer, sheet_name="Resumo", index=False)

print("✅ Relatório gerado: 'relatorioEnviar.xlsx'")

#Configuração do e-mail
EMAIL_REMETENTE = "jhorlenpitch@gmail.com"
SENHA_APP = "bkdp isma swrb zzqe"  #Senha Gerada do app no Gmail
EMAIL_DESTINATARIO = "anaflaviadasilvarodrigues1611@gmail.com"
ASSUNTO = "Relatório de Vendas"

#Criar a mensagem
msg = EmailMessage()
msg["Subject"] = ASSUNTO
msg["From"] = EMAIL_REMETENTE
msg["To"] = EMAIL_DESTINATARIO
msg.set_content("Olá,\n\nSegue em anexo o relatório atualizado das vendas.\n\nAtenciosamente,\nJhorlen Souza Bianor")

#Anexar o arquivo Excel
with open(arquivo_excel, "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=arquivo_excel)

#Enviar o e-mail
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_REMETENTE, SENHA_APP)
        server.send_message(msg)

    print("✅ E-mail enviado com sucesso!")

except Exception as e:
    print(f"❌ Erro ao enviar o e-mail: {e}")


#https://myaccount.google.com/lesssecureapps
