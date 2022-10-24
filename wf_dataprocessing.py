import pandas as pd
import numpy as np

def preprocessing():
    df1=pd.read_csv("data_original\coin_Dogecoin.csv")
    df2=pd.read_csv("data_original\coin_Ethereum.csv")
    df3=pd.read_csv("data_original\coin_Bitcoin.csv")
    cols = ['Symbol', 'SNo', 'Date']
    df1 = df1.drop(cols, axis=1)
    df2 = df2.drop(cols, axis=1)  #dropping unnecessary columns
    df3 = df3.drop(cols, axis=1)
    df1 = df1.iloc[: , 0:] 
    df2 = df2.iloc[: , 0:]     #removing S.No column
    df3 = df3.iloc[: , 0:]
    df1['Volume']=df1['Volume'].replace(0,df1['Volume'].mean())
    df2['Volume']=df2['Volume'].replace(0,df2['Volume'].mean())  #replacing 0 with mean in Volume column
    df3['Volume']=df3['Volume'].replace(0,df3['Volume'].mean())
    df1.to_csv("data_processing\Dogecoin.csv")
    df2.to_csv("data_processing\Ethereum.csv")
    df3.to_csv("data_processing\Bitcoin.csv")