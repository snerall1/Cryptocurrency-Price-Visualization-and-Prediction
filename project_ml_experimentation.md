#### SER594: Experimentation
#### TODO Crypto Currency Price Prediction
#### TODO Sai Sunil Neralla
#### TODO 11/21/2022


## Explainable Records
### Record 1
**Raw Data:** 
	Name	High	Low	Open	Close	Volume	Marketcap
1285	Dogecoin	0.00318765	0.00304427	0.00310059	0.00314277	9479750	345466885

Prediction Explanation:** The closing price prediction for this record is equivalent to 0.00306266339 and the actual value is 0.00314277
The opening price of the crypto on that day is 0.00310059. The highest price and the lowest prices are 0.00318765 and 0.00304427 respectively.
The predicted closing price 0.00306266339 lies between 0.00304427(lowest price) and 0.00318765 (highest price). Hence it is valid and correct.

### Record 2
**Raw Data:** 
    Name	High	Low	Open	Close	Volume	Marketcap
175	Ethereum	2.611809969	2.398920059	2.507719994	2.445060015	3725080	187435391.2

Prediction Explanation:** The closing price prediction for this record is equivalent to 2.21502622 and the actual value is 2.445060015
The opening price of the crypto on that day is 2.507719994. The highest price and the lowest prices are 2.611809969 and 2.398920059 respectively.
The predicted closing price 2.21502622 almost lies near the lowest price of the day which is 2.398920059. The prediction (though is lesser than the actual value) therefore is valid and correct.

## Interesting Features
### Feature A
**Feature:** High

**Justification:** High feature is the highest price of the crypto on a given day. It affects the closing price of the crypto, for example if the High value is significantly smaller and is near to Opening price of the crypto then the closing price of the crypto on that day would be lesser. Similarly if the High value is much higher, then the crypto price on that day would be good.

### Feature B
**Feature:** Low

**Justification:** Low feature is the lowest price of the crypto on a given day. It affects the closing price of the stock, for example if the Low value is significantly lower and is near to Opening price of the crypto then the closing price of the crypto on that day would be lesser. Similarly if the Low value is much higher, then the crypto price on that day would be good.

## Experiments 
### Varying A
**Prediction Trend Seen:** If the 'High' feature is varied, that is if the value is increased then we can see a shift in the closing price of the crypto towards the 'High' feature value. Similarly, if the 'High' value is reduced then we can observe a shift in the closing price in the opposite direction.

### Varying B
**Prediction Trend Seen:** If the 'Low' feature is varied, that is if the value is decreased then we can see a shift in the closing price of the crypto towards the 'Low' feature value. Similarly, if the 'Low' value is increased then we can observe a shift in the closing price in the opposite direction.

### Varying A and B together
**Prediction Trend Seen:** If both 'High' and 'Low' are increased or decreased together then we observe a corresponding increase or decrease in the closing price of the crypto.


### Varying A and B inversely
**Prediction Trend Seen:** If 'High' value is increased and 'Low' value is decreased then there is a very small shift in the closing price of the crypto and it can be either on the 'High' side or the 'Low' side. Similarly, If 'High' value is decreased and 'Low' value is increased then the closing price of the crypto shifts minimally either towards 'High' feature or towards 'Low' feature.
