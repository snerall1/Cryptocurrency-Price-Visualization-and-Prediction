#### SER594: Machine Learning Evaluation
#### Crypto Currency Price Prediction
#### Sai Sunil Neralla
#### 11/21/2022

## Evaluation Metrics
### Metric 1
**Name:** Root Mean Square Error

**Choice Justification:** The RMSE takes the error (the difference between prediction and the actual value) and squares them. Then, it averages them out and calculates the square root of that mean. This double transformation has two effects: it gives more weight to the bigger errors and it stops positive and negative errors from cancelling out, since they will all become positive.

### Metric 2
**Name:** Mean Absolute Error

**Choice Justification:** The Mean Absolute Error sums the error in absolute value, so the negative differences won’t cancel out the positive differences and averages them out. Unlike RMSE, the changes in MAE are linear and therefore intuitive.

## Alternative Models
### Alternative 1 Ridge Model
**Construction:** Ridge regression is an extension of linear regression where the loss function is modified to minimize the complexity of the model. This modification is done by adding a penalty parameter that is equivalent to the square of the magnitude of the coefficients. In the loss function, alpha is the parameter we need to select. A low alpha value can lead to over-fitting, whereas a high alpha value can lead to under-fitting.

**Evaluation:** 
Loss function = OrdinaryLeastSquares + alpha * summation (squared coefficient values)
The Root Mean Square Error of Dogecoin using Ridge model: 0.002342361116324058
The Root Mean Square Error of Ethereum using Ridge model: 17.22688359665781
The Root Mean Square Error of Bitcoin using Ridge model: 276.199861519837
The Mean Absolute Error of Dogecoin using Ridge model: 0.020194319382965856
The Mean Absolute Error of Ethereum using Ridge model: 2.530849998146625
The Mean Absolute Error of Bitcoin using Ridge model: 9.589515284369746


### Alternative 2 Lasso Model
**Construction:** Lasso regression is also a modification of linear regression. In Lasso, the loss function is modified to minimize the complexity of the model by limiting the sum of the absolute values of the model coefficients. In the loss function, alpha is the penalty parameter we need to select. Using an l1 norm constraint forces some weight values to zero to allow other coefficients to take non-zero values.

**Evaluation:** 
Loss function = OrdinaryLeastSquares + alpha * summation (absolute values of the magnitude of the coefficients)
The Root Mean Square Error of Dogecoin using Lasso model: 0.042442216146104134
The Root Mean Square Error of Ethereum using Lasso model: 17.298811841250455
The Root Mean Square Error of Bitcoin using Lasso model: 276.39188286621885
The Mean Absolute Error of Dogecoin using Lasso model: 0.11446209157297207
The Mean Absolute Error of Ethereum using Lasso model: 2.523458216282556
The Mean Absolute Error of Bitcoin using Lasso model: 9.762182858281056


## Best Model

**Model:** Ridge model
Ridge model works well when there are large number of parameters with same value. And since the input parameters like Crypto 'Open' , 'Close' , 'High', 'Low' are almost similar in a given set of consequent dates, therefore Ridge works well than Lasso model.