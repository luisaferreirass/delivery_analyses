import numpy as np
import pandas as pd

# read
df_cardapio = pd.read_csv("cardapio.csv")
df_pedidos = pd.read_csv("pedidos.csv")

# EDA

pedidos_info = df_pedidos.info()
count_col = df_pedidos.shape[1]
pedidos_decribe = df_pedidos.describe()

# Feature Engineering

df_pedidos["Receitas_Item"] = df_pedidos["Quantidade"] * df_pedidos["Preco_Unitario"]

# Tratamento de Valores Ausentes

df_null = df_pedidos.isna()

media = round(df_pedidos["Quantidade"].mean())
df_pedidos.fillna({"Quantidade": media}, inplace=True)

df_pedidos.dropna(subset=["Preco_Unitario"], inplace=True)

# Agrupamento

group_items = df_pedidos.groupby("Item") # Retorna um objeto

quantidade_por_item = group_items["Quantidade"].sum()

receita_por_item = group_items["Receitas_Item"].sum()

receita_por_item.sort_values(inplace=True)
quantidade_por_item.sort_values(inplace=True)

top_vendidos = quantidade_por_item.tail()
top_receita = receita_por_item.tail()

# Análise Temporal

df_pedidos["Data"] = pd.to_datetime(df_pedidos["Data"])

df_mes = df_pedidos.copy()
df_mes["mes"] = df_mes["Data"].dt.month
group_mes = df_mes.groupby("mes")

receita_por_mes = group_mes["Receitas_Item"].sum()
vendas_por_mes = group_mes["Quantidade"].sum()

# Merge

df_merge = pd.merge(df_pedidos, df_cardapio, how='left', on='Item')
group_categoria = df_merge.groupby("Categoria")
receita_por_categoria = group_categoria["Receitas_Item"].sum() # Retorna uma serie e não um df

receita_por_categoria.sort_values(inplace=True)
top_categoria = receita_por_categoria.tail(1)

# Filtros e Consultas

df_filtro = df_merge[(df_merge["Categoria"] == "Salgados") & df_merge["Quantidade"] > 10]
print(df_filtro)

# KPI

receita_total = df_pedidos["Receitas_Item"].sum()

items_total = df_pedidos["Quantidade"].sum()

pedidos_total = df_pedidos.shape[0]
ticket_medio = receita_total / pedidos_total