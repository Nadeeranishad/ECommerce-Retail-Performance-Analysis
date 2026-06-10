import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Sales_record.csv")
sales=pd.read_csv("Sales_record.csv")
df=pd.read_csv("warehouse_log.csv")
warehouse=pd.read_csv("warehouse_log.csv")
print("missing values in sales \n",sales.isnull().sum())
sales['Revenue']=sales['Revenue'].fillna(sales['Revenue'].median())
category_perfe=sales.groupby('Category')['Revenue'].sum().reset_index()
sns.barplot(x='Category', y='Revenue', data=category_perfe, palette='Blues_d')
plt.title('Revenue Performance by Product Category')
plt.savefig('category_revenue.png', dpi=300) # Saves the chart to upload later
plt.show()
