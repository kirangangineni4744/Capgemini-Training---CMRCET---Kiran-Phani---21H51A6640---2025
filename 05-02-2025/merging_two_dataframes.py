import pandas as pd

data={

    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'State': ['Delhi', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG', 'Odisha'],
    'Year': [2021, 2022, 2021, 2022, 2021, 2022],
    'Sales': [750000, 820000, 690000, 720000, 670000, 710000],
    'Profit': [95000, 102000, 85000, 91000, 77000, 88000]
}

df=pd.DataFrame(data)

df_sales=pd.DataFrame({'State':['Delhi','Tamil Nadu','WestBengal'],
                       'Sales':[1570000,1410000,1380000]})
print(df_sales)
df_profit=pd.DataFrame({'State':['Delhi','Tamil Nadu','WestBengal'],
                       'Sales':[185000,165000,155000]})
print(df_profit)
df_merged=pd.merge(df_sales,df_profit,on="State",how="inner")
print(df_merged)