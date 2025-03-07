import pandas as pd 

data={
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,30,34,40],
    'City':['HYD','MUM','DEL','PUNE']
}

df=pd.DataFrame(data)
print(df)

print(df.head())

data=pd.read_csv("C:/Users/Phani/OneDrive/Desktop/Capgemini Training 2025/05-02-2025/customers-100.csv")

print(data[1:5])

data.to_json("JSON.json",index=False)

data=data.sort_values(by='First Name',ascending=False)
print(data[1:10])