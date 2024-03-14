import pandas as pd

df = pd.read_csv('dataset/sales_data.csv')

a = df.head(10)
print(a)

print("Dataset Information:")
b = df.info()
print(b)

total_sales = df['SALES'].sum()
print(f"\nTotal Sales: {total_sales}")

mean_sold = df['QUANTITYORDERED'].mean()
print(f"Rata-rata unit terjual: {mean_sold} per transaksi")