import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import math

def prediction():
    Dogecoin_model = pickle.load(open("models/regression_model_Dogecoin.sav", 'rb'))
    ridge_dogecoin = pickle.load(open("models/ridge_model_Dogecoin.sav", 'rb'))
    lasso_dogecoin = pickle.load(open("models/lasso_model_Dogecoin.sav", 'rb'))
    X_test=pd.read_csv("data_processing/X_test_Dogecoin.csv")
    y_test=pd.read_csv("data_processing/y_test_Dogecoin.csv")
    predicted1=Dogecoin_model.predict(X_test)
    ridge_pred1=ridge_dogecoin.predict(X_test)
    lasso_pred1=lasso_dogecoin.predict(X_test)
    print("Predicted Price for Dogecoin")
    print(predicted1)
    file = open("evaluation/summary.txt","w")
    file.write("Root Mean Square Error for Dogecoin crypto using Linear Regression: ")
    file.write(str(math.sqrt(mean_squared_error(y_test,predicted1)))+" ")
    mae1=str(math.sqrt(mean_absolute_error(y_test,predicted1)))
    mae11=str(math.sqrt(mean_absolute_error(y_test,ridge_pred1)))
    mae111=str(math.sqrt(mean_absolute_error(y_test,lasso_pred1)))
    ridge_prediction=ridge_dogecoin.predict(X_test)
    file.write("Root Mean Square Error for Dogecoin crypto using Ridge model: ")
    file.write(str(math.sqrt(mean_squared_error(y_test,ridge_prediction)))+" ")
    lasso_prediction=lasso_dogecoin.predict(X_test)
    file.write("Root Mean Square Error for Dogecoin crypto using Lasso model: ")
    file.write(str(math.sqrt(mean_squared_error(y_test,lasso_prediction)))+" ")
    Ethereum_model = pickle.load(open("models/regression_model_Ethereum.sav", 'rb'))
    ridge_ethereum = pickle.load(open("models/ridge_model_Ethereum.sav", 'rb'))
    lasso_ethereum = pickle.load(open("models/lasso_model_Ethereum.sav", 'rb'))
    X_test=pd.read_csv("data_processing/X_test_Ethereum.csv")
    y_test=pd.read_csv("data_processing/y_test_Ethereum.csv")
    predicted2=Ethereum_model.predict(X_test)
    ridge_pred2=ridge_ethereum.predict(X_test)
    lasso_pred2=lasso_ethereum.predict(X_test)
    print("Predicted Price for Ethereum")
    print(predicted2)
    file.write("Root Mean Square Error for Ethereum crypto using Linear Regression: ")
    file.write(str(math.sqrt(mean_squared_error(y_test,predicted2)))+" ")
    mae2=str(math.sqrt(mean_absolute_error(y_test,predicted2)))
    mae22=str(math.sqrt(mean_absolute_error(y_test,ridge_pred2)))
    mae222=str(math.sqrt(mean_absolute_error(y_test,lasso_pred2)))
    ridge_prediction=ridge_ethereum.predict(X_test)
    file.write("Root Mean Square Error for Ethereum crypto using Ridge model: ")
    file.write(str(math.sqrt(mean_squared_error(y_test,ridge_prediction)))+" ")
    lasso_prediction=lasso_ethereum.predict(X_test)
    file.write("Root Mean Square Error for Ethereum crypto using Lasso model: ")
    file.write(str(math.sqrt(mean_squared_error(y_test,lasso_prediction)))+" ")
    Bitcoin_model = pickle.load(open("models/regression_model_Bitcoin.sav", 'rb'))
    ridge_bitcoin = pickle.load(open("models/ridge_model_Bitcoin.sav", 'rb'))
    lasso_bitcoin = pickle.load(open("models/lasso_model_Bitcoin.sav", 'rb'))
    X_test=pd.read_csv("data_processing/X_test_Bitcoin.csv")
    y_test=pd.read_csv("data_processing/y_test_Bitcoin.csv")
    predicted3=Bitcoin_model.predict(X_test)
    ridge_pred3=ridge_bitcoin.predict(X_test)
    lasso_pred3=lasso_bitcoin.predict(X_test)
    print("Predicted Price for Bitcoin")
    print(predicted3)
    file.write("Root Mean Square Error for Bitcoin crypto using Linear Regression: ")
    file.write(str(math.sqrt(mean_squared_error(y_test,predicted3)))+" ")
    mae3=str(math.sqrt(mean_absolute_error(y_test,predicted3)))
    mae33=str(math.sqrt(mean_absolute_error(y_test,ridge_pred3)))
    mae333=str(math.sqrt(mean_absolute_error(y_test,lasso_pred3)))
    ridge_prediction=ridge_bitcoin.predict(X_test)
    file.write("Root Mean Square Error for Bitcoin crypto using Ridge model: ")
    file.write(str(math.sqrt(mean_squared_error(y_test,ridge_prediction)))+" ")
    lasso_prediction=lasso_bitcoin.predict(X_test)
    file.write("Root Mean Square Error for Bitcoin crypto using Lasso model: ")
    file.write(str(math.sqrt(mean_squared_error(y_test,lasso_prediction)))+" ")
    file.write("Mean Absolute Error for Dogecoin using Linear Regression: ")
    file.write(mae1+" ")
    file.write("Mean Absolute Error for Dogecoin using Ridge model: ")
    file.write(mae11+" ")
    file.write("Mean Absolute Error for Dogecoin using Lasso model: ")
    file.write(mae111+" ")
    file.write("Mean Absolute Error for Ethereum using Linear Regression: ")
    file.write(mae2+" ")
    file.write("Mean Absolute Error for Ethereum using Ridge model: ")
    file.write(mae22+" ")
    file.write("Mean Absolute Error for Ethereum using Lasso model: ")
    file.write(mae222+" ")
    file.write("Mean Absolute Error for Bitcoin using Linear Regression: ")
    file.write(mae3)
    file.write("Mean Absolute Error for Bitcoin using Ridge model: ")
    file.write(mae33+" ")
    file.write("Mean Absolute Error for Bitcoin using Lasso model: ")
    file.write(mae333+" ")
    file.close()