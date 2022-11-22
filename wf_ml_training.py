from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
import wf_ml_evaluation as obj1
import pickle
import numpy as np
import pandas as pd

def training():
    df1=pd.read_csv("data_processing\Dogecoin.csv")
    df2=pd.read_csv("data_processing\Ethereum.csv")
    df3=pd.read_csv("data_processing\Bitcoin.csv")
    X1=df1[['High','Low','Open','Volume']]
    y1=df1[['Close']]
    X2=df2[['High','Low','Open','Volume']]
    y2=df2[['Close']]
    X3=df3[['High','Low','Open','Volume']]
    y3=df3[['Close']]
    X_train , X_test, y_train , y_test = train_test_split(X1,y1,train_size =.8,random_state=0)
    X_train.to_csv('data_processing/X_train_Dogecoin.csv',index=False)
    X_test.to_csv('data_processing/X_test_Dogecoin.csv',index=False)
    y_train.to_csv('data_processing/y_train_Dogecoin.csv',index=False)
    y_test.to_csv('data_processing/y_test_Dogecoin.csv',index=False)
    X_train.to_csv('models/X_train_Dogecoin.csv',index=False)
    X_test.to_csv('models/X_test_Dogecoin.csv',index=False)
    y_train.to_csv('models/y_train_Dogecoin.csv',index=False)
    y_test.to_csv('models/y_test_Dogecoin.csv',index=False)
    regression1=LinearRegression()
    regression1.fit(X_train,y_train)
    filename = 'models/regression_model_Dogecoin.sav'
    pickle.dump(regression1, open(filename, 'wb'))
    ridge1 = Ridge(alpha=0.01)
    ridge1.fit(X_train, y_train)
    filename = 'models/ridge_model_Dogecoin.sav'
    pickle.dump(ridge1, open(filename, 'wb'))
    lasso1 = Lasso(alpha=0.01)
    lasso1.fit(X_train, y_train)
    filename = 'models/lasso_model_Dogecoin.sav'
    pickle.dump(lasso1, open(filename, 'wb'))
    X_train , X_test, y_train , y_test = train_test_split(X2,y2,train_size =.8,random_state=0)
    X_train.to_csv('data_processing/X_train_Ethereum.csv',index=False)
    X_test.to_csv('data_processing/X_test_Ethereum.csv',index=False)
    y_train.to_csv('data_processing/y_train_Ethereum.csv',index=False)
    y_test.to_csv('data_processing/y_test_Ethereum.csv',index=False)
    X_train.to_csv('models/X_train_Ethereum.csv',index=False)
    X_test.to_csv('models/X_test_Ethereum.csv',index=False)
    y_train.to_csv('models/y_train_Ethereum.csv',index=False)
    y_test.to_csv('models/y_test_Ethereum.csv',index=False)
    regression2=LinearRegression()
    regression2.fit(X_train,y_train)
    filename = 'models/regression_model_Ethereum.sav'
    pickle.dump(regression2, open(filename, 'wb'))
    ridge2 = Ridge(alpha=0.01)
    ridge2.fit(X_train, y_train)
    filename = 'models/ridge_model_Ethereum.sav'
    pickle.dump(ridge2, open(filename, 'wb'))
    lasso2 = Lasso(alpha=0.01)
    lasso2.fit(X_train, y_train)
    filename = 'models/lasso_model_Ethereum.sav'
    pickle.dump(lasso2, open(filename, 'wb'))
    X_train , X_test, y_train , y_test = train_test_split(X3,y3,train_size =.8,random_state=0)
    X_train.to_csv('data_processing/X_train_Bitcoin.csv',index=False)
    X_test.to_csv('data_processing/X_test_Bitcoin.csv',index=False)
    y_train.to_csv('data_processing/y_train_Bitcoin.csv',index=False)
    y_test.to_csv('data_processing/y_test_Bitcoin.csv',index=False)
    X_train.to_csv('models/X_train_Bitcoin.csv',index=False)
    X_test.to_csv('models/X_test_Bitcoin.csv',index=False)
    y_train.to_csv('models/y_train_Bitcoin.csv',index=False)
    y_test.to_csv('models/y_test_Bitcoin.csv',index=False)
    regression3=LinearRegression()
    regression3.fit(X_train,y_train)
    filename = 'models/regression_model_Bitcoin.sav'
    pickle.dump(regression3, open(filename, 'wb'))
    ridge3 = Ridge(alpha=0.01)
    ridge3.fit(X_train, y_train)
    filename = 'models/ridge_model_Bitcoin.sav'
    pickle.dump(ridge3, open(filename, 'wb'))
    lasso3 = Lasso(alpha=0.01)
    lasso3.fit(X_train, y_train)
    filename = 'models/lasso_model_Bitcoin.sav'
    pickle.dump(lasso3, open(filename, 'wb'))