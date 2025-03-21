import pandas as pd
from plyer import notification

dadosFrutas = pd.read_csv('frutas.csv', delimiter=';')

print(dadosFrutas)

indice = dadosFrutas['Total Vendido Por Produto'].idxmax()

nome = dadosFrutas.loc[indice, 'Produto']
quantidade = dadosFrutas.loc[indice, 'Quantidade']
preco = dadosFrutas.loc[indice, 'Preco']
vendido = dadosFrutas.loc[indice, 'Vendido']
TotalPorProduto = dadosFrutas.loc[indice, 'Total Vendido Por Produto']

print('Relatório')
print(f'A fruta {nome} teve o melhor Total vendido por produto, de {quantidade} unidades, foram vendidas {vendido} unidades, com um lucro total de R${TotalPorProduto}.')

#Notificação
notification.notify(
    title = 'Relatórios Frutas',
    message = f'A fruta {nome} teve o melhor Total vendido por produto, \nde {quantidade} unidades, foram vendidas {vendido} unidades, \ncom um lucro total de R${TotalPorProduto}.',
    timeout = 15
)
#Fim Notificação