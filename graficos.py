
"""#**Graficos** -- Ivan Grand Champs"""

df["LojaID"].value_counts(ascending=False)

#Gráfico de barras
df["LojaID"].value_counts(ascending=False).plot.bar()

#Gráfico de barras horizontais
df["LojaID"].value_counts().plot.barh()

#Gráfico de barras horizontais
df["LojaID"].value_counts(ascending=True).plot.barh();

#Gráfico de Pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

#Total vendas por cidade
df["Cidade"].value_counts()

#Adicionando um título e alterando o nome dos eixos
import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar(title="Total vendas por Regiao")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

#Alterando a cor
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="gold")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

#Alterando o estilo
plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total Produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend();

df.groupby(df["mes_venda"])["Qtde"].sum()

#Selecionando apenas as vendas de 2018
df_2019 = df[df["Ano_Venda"] == 2018]

df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum()

#Total produtos vendidos por mês
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "o")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend();

#Hisograma
plt.hist(df["Qtde"], color="gray");

plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"]);

#Salvando em png
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend()
plt.savefig("grafico QTDE x MES.png")

