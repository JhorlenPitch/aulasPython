import pandas as pd
import matplotlib.pyplot as plt

#Ler o arquivo CSV
df = pd.read_csv("frutas.csv", delimiter=";")

#Função para determinar a cor
def determinar_cor(quantidade):
    if quantidade < 40:
        return "red" 
    elif 40 <= quantidade < 80:
        return "orange"  
    else:
        return "green" 

#Criar o grafico de barras
plt.figure(figsize=(8, 5))

#Gerar barras com cores personalizadas
cores = [determinar_cor(v) for v in df["Vendido"]]
plt.bar(df["Produto"], df["Vendido"], color=cores)

#Adicionar titulo e rotulos
plt.title("Quantidade Vendida por Produto", fontsize=14)
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=45)  #Rotacionar os rotulos do eixo X

#Salvar a imagem
plt.savefig("grafico.png", dpi=300, bbox_inches="tight")
plt.show()

print("✅ Gráfico gerado e salvo como 'grafico.png'")