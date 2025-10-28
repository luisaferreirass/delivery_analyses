# 📊 Análise de Pedidos e Cardápio com Pandas

Este projeto realiza uma **análise exploratória de dados (EDA)** e tratamento de informações de dois arquivos CSV — `cardapio.csv` e `pedidos.csv`.  
O objetivo é gerar insights sobre **vendas, receitas e desempenho por item, categoria e mês**.

---

## 🧩 Estrutura do Código

### 1. Importação das Bibliotecas
O código utiliza as bibliotecas **NumPy** e **Pandas** para manipulação e análise de dados:


### 2. Leitura dos Dados
Carregamento dos arquivos CSV contendo informações de cardápio e pedidos

### 3. Análise Exploratória (EDA)
Exploração inicial para compreender a estrutura e estatísticas básicas dos dados:

### 4. Criação de Novas Features
Criação da coluna `Receitas_Item`, que representa o faturamento de cada item

### 5. Tratamento de Valores Ausentes
Verificação e tratamento de valores nulos


### 6. Agrupamento e Métricas por Item
Agrupamento de dados para cálculo de quantidade e receita por item
Ordenação e identificação dos itens **mais vendidos** e **mais lucrativos**


### 7. Análise Temporal
Conversão da coluna de data e agrupamento por mês
Cálculo de **receita** e **vendas por mês**


### 8. Junção com o Cardápio
Realização de `merge` para adicionar informações de categoria a cada pedido:
Agrupamento por categoria e cálculo da **receita total por categoria**:

### 9. Filtros e Consultas
Filtragem de pedidos de **salgados** com **quantidade superior a 10**


### 10. KPIs (Indicadores de Desempenho)
Cálculo dos principais indicadores de negócio

**KPIs gerados:**
- 💰 Receita Total (`receita_total`)
- 📦 Itens Vendidos (`items_total`)
- 🧾 Total de Pedidos (`pedidos_total`)
- 🎟️ Ticket Médio (`ticket_medio`)

---

## 📈 Possíveis Extensões
- Geração de gráficos com Matplotlib ou Seaborn  
- Análises sazonais (por semana, trimestre, etc.)  
- Dashboard interativo com Streamlit ou Power BI  


## 🗂️ Requisitos
- Python ≥ 3.8  
- Bibliotecas necessárias:
  ```bash
  pip install pandas numpy
  ```

---

## ✍️ Autor
Projeto desenvolvido para análise de desempenho de vendas e receitas com base em dados de pedidos e cardápio.
