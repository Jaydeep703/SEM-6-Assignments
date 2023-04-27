import pandas as pd
data={
    'Name':['Jaydeep','Subodh','Yuvraj','Surabh','Sanket'],
    'marks':[90,80,70,60,50],
    'age':[20,25,19,20,20]
}
df=pd.DataFrame(data)

col= ['Name']
print(df[col].head(2))
print(df[col].tail(2))

print(df['marks'].mean())
print(df['age'].median())