import pandas as pd

#Ler o CSV (com delimitador ;)
df = pd.read_csv("frutas.csv", delimiter=";")

#Criar resumo por produto somando "Total Vendido Por Produto"
resumo = df.groupby("Produto", as_index=False)["Total Vendido Por Produto"].sum()

#Salvar no Excel
with pd.ExcelWriter("relatorio.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Detalhado", index=False)
    resumo.to_excel(writer, sheet_name="Resumo", index=False)

print("Relatório gerado: 'relatorio.xlsx'")