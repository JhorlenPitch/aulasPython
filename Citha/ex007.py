import pandas as pd

#Carregar os dados
dados = pd.read_csv('vendas.csv', delimiter=';')

#Calcular Ticket Medio
#Total de vendas = Total Vendido Por Produto
#Número de vendas = quantidade de produtos vendidos
ticket_medio = dados['Total Vendido Por Produto'].sum() / dados['Quantidade'].sum()
print(f'Ticket Médio: R${ticket_medio:.2f}')

#Calcular Margem de Lucro
dados['Margem de Lucro'] = dados['Preco'] - dados['Custo']
produtos_com_margem_baixa = dados[dados['Margem de Lucro'] < 1]  #Exmplo, produtos com margem menor que 1
print(f'\nProdutos com Margem de Lucro Baixa:\n{produtos_com_margem_baixa[["Produto", "Margem de Lucro"]]}')

#Calcular os Top 3 Produtos Mais Lucrativos
#Lucro Total = (Preço - Custo) * Quantidade Vendida
dados['Lucro Total'] = (dados['Preco'] - dados['Custo']) * dados['Vendido']
top_3_produtos = dados[['Produto', 'Lucro Total']].sort_values(by='Lucro Total', ascending=False).head(3)

print(f'\nTop 3 Produtos Mais Lucrativos:\n{top_3_produtos}')