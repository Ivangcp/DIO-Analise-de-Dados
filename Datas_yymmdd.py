
"""#**Trabalhando com datas** -- **Ivan Grand Champs**"""

#Trasnformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

#Verificando o tipo de dado de cada coluna
df.dtypes

#Transformando coluna de data em data
df["Data"] = pd.to_datetime(df["Data"])

df.dtypes

#Agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()

#Criando uma nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year

df.sample(15)

#Extraindo o mês e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

df.sample(15)

#Retornando a data mais antiga
df["Data"].min()

#Calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()

df.sample(5)

#Criando a coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter

df.sample(5)

#Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

vendas_marco_19.sample(20)

