# 📊 Order and Menu Analysis with Pandas

This project performs **exploratory data analysis (EDA)** and data treatment on two CSV files — `cardapio.csv` (menu) and `pedidos.csv` (orders).  
The goal is to generate insights about **sales, revenue and performance by item, category and month**.

---

## 🧩 Code Structure

### 1. Importing Libraries
The code uses the **NumPy** and **Pandas** libraries for data manipulation and analysis:


### 2. Loading the Data
Loading the CSV files containing menu and order information

### 3. Exploratory Analysis (EDA)
Initial exploration to understand the structure and basic statistics of the data:

### 4. Feature Engineering
Creation of the `Receitas_Item` column, which represents the revenue of each item

### 5. Handling Missing Values
Checking for and handling null values


### 6. Grouping and Metrics by Item
Grouping data to compute quantity and revenue per item
Sorting and identifying the **best-selling** and **most profitable** items


### 7. Time Analysis
Converting the date column and grouping by month
Computing **revenue** and **sales per month**


### 8. Joining with the Menu
Using `merge` to add category information to each order:
Grouping by category and computing **total revenue per category**:

### 9. Filters and Queries
Filtering orders of **salgados** (savory snacks) with **quantity greater than 10**


### 10. KPIs (Key Performance Indicators)
Computing the main business indicators

**Generated KPIs:**
- 💰 Total Revenue (`receita_total`)
- 📦 Items Sold (`items_total`)
- 🧾 Total Orders (`pedidos_total`)
- 🎟️ Average Ticket (`ticket_medio`)

---

## 📈 Possible Extensions
- Charts with Matplotlib or Seaborn  
- Seasonal analysis (by week, quarter, etc.)  
- Interactive dashboard with Streamlit or Power BI  


## 🗂️ Requirements
- Python ≥ 3.8  
- Required libraries:
  ```bash
  pip install pandas numpy
  ```

---

## ✍️ Author
Project developed to analyze sales and revenue performance based on order and menu data.
