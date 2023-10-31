import pandas as pd
df=pd.read_excel("C:\\Users\\Admin\\Desktop\\2019 Order Data.xlsx")
for x in df.index:
    if df.loc[x,"Order ID"]=="XXXXXX":
        df.drop(x,inplace=True)
df[["CustomerID","Customer Name"]]=df["Customer ID"].str.split(" - ",expand=True)
df.drop(columns="Customer ID",inplace=True)
df["CustomerID"]=df["CustomerID"].astype(int)
df=df[[ "Order ID","CustomerID","Customer Name","Cookies Shipped","Revenue","Cost","Order Date","Ship Date","Order Status"]]
df["Lead Time"]=df["Ship Date"]-df["Order Date"]
df.sort_values(by="Order Date", ascending= True, inplace=True)
df.to_excel("C:\\Users\\Admin\\Desktop\\Project 1\\CleanedData.xlsx",index=False)
