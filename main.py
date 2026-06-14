import pandas as pd

print("\n===== SALES ANALYSIS REPORT =====\n")

df = pd.read_csv("sales_data.csv")

total_sales = df["Sales"].sum()
avg_sales = df["Sales"].mean()
highest = df["Sales"].max()
lowest = df["Sales"].min()

print(f"Total Sales = {total_sales}")
print(f"Average Sales = {avg_sales}")
print(f"Highest Sales = {highest}")
print(f"Lowest Sales = {lowest}")