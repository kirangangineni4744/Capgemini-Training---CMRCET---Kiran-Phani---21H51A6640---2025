import pandas as pd

data={

    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'State': ['Delhi', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG', 'Odisha'],
    'Year': [2021, 2022, 2021, 2022, 2021, 2022],
    'Sales': [750000, 820000, 690000, 720000, 670000, 710000],
    'Profit': [95000, 102000, 85000, 91000, 77000, 88000]
}

df=pd.DataFrame(data)
df.to_csv("data.csv",index=False)

df_1=df.set_index(["Region","State","Year"],inplace=False)
print(df_1)

print(df_1.loc[('South','Tamil Nadu',2021),'Profit'])


