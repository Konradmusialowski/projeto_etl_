import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path


BASE_DIR = Path().resolve().parent

df = pd.read_csv(BASE_DIR / "data" / "output" / "consulta.csv", sep=";")
df2 = pd.read_csv(BASE_DIR / "data" / "output" / "consulta2.csv", sep=";")


plt.style.use("ggplot")
# Visualizar as primeiras linhas
print("\n📊 Estatísticas - Ano")
display(df['ano'].describe())

print("\n📊 Estatísticas - Mês")
display(df['mes'].describe())

print("\n📊 Estatísticas - Total Entrada")
display(df['total_entrada'].describe())

display(df.head())

mov = df['total_entrada'].values

media = np.mean(mov)
variancia = np.var(mov)
desvio = np.std(mov)


print("\n📊 Estatísticas - Ano")
display(df['ano'].describe())

print("\n📊 Estatísticas - Mês")
display(df['mes'].describe())

print("\n📊 Estatísticas - Total Entrada")
display(df['total_entrada'].describe())


print("📌 rank")
ranking_centros = (
    df.groupby('nome_centro_distribuicao')['total_entrada']
    .sum()
    .reset_index()
    .sort_values(by='total_entrada', ascending=False)
)

print("📌 Ranking de Centros por Volume de Entrada")
display(ranking_centros)

plt.figure(figsize=(10,6))
sns.barplot(
    data=ranking_centros,
    x='total_entrada',
    y='nome_centro_distribuicao'
)

plt.title("Total de Entrada por Centro de Distribuição")
plt.xlabel("Total de Entrada")
plt.ylabel("Centro de Distribuição")
plt.tight_layout()
plt.show()




ranking_produtos = (
    df.groupby('codigo_produto')['total_entrada']
    .sum()
    .reset_index()
    .sort_values(by='total_entrada', ascending=False)
)

print("📌 Ranking de Produtos por Volume de Entrada")
display(ranking_produtos)

plt.figure(figsize=(10,6))
sns.barplot(
    data=ranking_produtos,
    x='total_entrada',
    y='codigo_produto'
)

plt.title("Produtos com Maior Volume de Entrada")
plt.xlabel("Total de Entrada")
plt.ylabel("Código do Produto")
plt.tight_layout()
plt.show()

entrada_por_mes = (
    df.groupby(['ano','mes'])['total_entrada']
    .sum()
    .reset_index()
)

display(entrada_por_mes)

plt.figure(figsize=(10,6))
sns.lineplot(
    data=entrada_por_mes,
    x='mes',
    y='total_entrada',
    hue='ano',
    marker='o'
)

plt.title("Evolução Mensal das Entradas")
plt.xlabel("Mês")
plt.ylabel("Total de Entrada")
plt.tight_layout()
plt.show()


