from sales_analyzer.data_loader import load_sales_data
from sales_analyzer.data_cleaner import clean_data
from sales_analyzer.analyzer import basic_stats, sales_by_category
from sales_analyzer.visualizer import sales_chart
from sales_analyzer.reporter import export_report

path = "data/raw/sales_data.csv"

df = load_sales_data(path)

df = clean_data(df)

stats = basic_stats(df)

print("\nSales Statistics")
print(stats)

category = sales_by_category(df)

print("\nSales by Category")
print(category)

sales_chart(category)

export_report(stats)