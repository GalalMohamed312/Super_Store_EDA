import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

df = pd.read_csv("SampleSuperstore.csv")

print(df.head())

print("info", df.info)
print("describe statistics", df.describe())
print("nulls checks", df.isnull().sum())
print("profit sales",df[["Sales","Profit"]].sum())

category_profit = df.groupby("Category")[["Sales","Profit"]].sum().reset_index()
print("category profit: \n",category_profit)

print("Weak Area: Categories with negative or low profit especially Furniture")
subcat_profit = df.groupby("Sub-Category")[["Sales","Profit"]].sum().reset_index()
subcat_profit = subcat_profit.sort_values("Profit")
print("sub category sales and profit: \n",subcat_profit.head(10))

sns.barplot(data=subcat_profit.head(10), x="Profit", y="Sub-Category")
plt.title("Top 10 Loss-Making Sub-Categories")
plt.show()

print("Weak Area: Sub-categories like Tables,Bookcases and Supplies cause heavy losses.")

sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.5)
plt.title("Discount vs Profit")
plt.show()
print("Weak Area: Higher discounts → lower profit")

region_profit = df.groupby("Region")[["Sales","Profit"]].sum().reset_index()
print("region per sales and profit:\n",region_profit)
sns.barplot(data=region_profit, x="Region", y="Profit")
plt.title("Profit by Region")
plt.show()
print("Regions with lower profit need pricing/logistics review.")


ship_profit = df.groupby("Ship Mode")[["Sales","Profit"]].sum().reset_index()
print("ship mode per sales profit:\n",ship_profit)

sns.barplot(data=ship_profit, x="Ship Mode", y="Profit")
plt.title("Profit by Ship Mode")
plt.show()

print("Shipping cost misalignment affects margins.")

loss_orders = df[df["Profit"] < 0]
print("loss orders \n",loss_orders[["Category","Sub-Category","Sales","Discount","Profit"]].head())
print("Problem: Revenue growth without profitability.")

segment_profit = df.groupby("Segment")[["Sales","Profit"]].sum().reset_index()
print("segment profitability:\n",segment_profit)

sns.barplot(data=segment_profit, x="Segment", y="Profit")
plt.title("Profit by Customer Segment")
plt.show()

print("Problem: Some segments buy more but generate less profit like Corporate and Home Office but less than Consumer in sales "
      "and profit.")

# Quantity vs profit
sns.scatterplot(data=df, x="Quantity", y="Profit", alpha=0.5)
plt.title("Quantity vs Profit")
plt.show()

print("Problem:Higher quantity does not guarantee profit")

city_profit = df.groupby("City")[["Sales","Profit"]].sum().reset_index()
city_profit = city_profit.sort_values("Profit")
print("city loss per sales and profit:\n",city_profit.head(10))

print("Problem: Certain cities consistently lose money.")


plt.figure(figsize=(8,6))
sns.heatmap(
    df[["Sales","Quantity","Discount","Profit"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Matrix")
plt.show()

print("""
Key Weak Areas:
1. Furniture category, especially Tables, is loss-making
2. High discounts significantly reduce profit
3. Some regions and cities consistently underperformed
4. Sales volume is prioritized over profitability
5. Shipping cost strategy is not margin-aware
""")
