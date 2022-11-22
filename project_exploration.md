#### SER594: Exploratory Data Munging and Visualization
#### Data Munging and Visualization for Crypto Currency Price Prediction
#### Sai Sunil Neralla
#### 10/23/2022

## Basic Questions
**Dataset Author(s):** 
https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory
(This data is taken from kaggle which was origially obtained from https://coinmarketcap.com/)
**Dataset Construction Date:** 07/06/2021 (last updated)

**Dataset Record Count:**
coin_Dogecoin: 2759
coin_Ethereum: 2159
coin_Bitcoin: 2990

**Dataset Field Meanings:** 
Date : date of observation
Open : Opening price on the given day
High : Highest price on the given day
Low : Lowest price on the given day
Close : Closing price on the given day
Volume : Volume of transactions on the given day
Market Cap : Market capitalization in USD

**Dataset File Hash(es):** 
9ab3a933284986faad2880dcfaf3c65e
478beba6f09570a1d3f8a692a058e022
6db948bef83d685fc849c99a4b4c05b8

## Interpretable Records
### Record 1
**Raw Data:** 
SNo	Name	Symbol	Date	High	Low	Open	Close	Volume	Marketcap
1	Dogecoin	DOGE	2013-12-16 23:59:59	0.000866	0.000150	0.000299	0.000205	0.0	1.509085e+06

**Interpretation:** The above record belongs to coin_Dogecoin.csv. It shows the highest price, lowest price, opening price, closing price, volume of transactions and market capitalization for the date 2013-12-16 23:59:59.

### Record 2
**Raw Data:**
SNo	Name	Symbol	Date	High	Low	Open	Close	Volume	Marketcap
1	Ethereum	ETH	2015-08-08 23:59:59	2.798810	0.714725	2.793760	0.753325	674188.0	4.548689e+07

**Interpretation:** The above record belongs to coin_Ethereum.csv. It shows the highest price, lowest price, opening price, closing price, volume of transactions and market capitalization for the date 2015-08-08 23:59:59.

## Data Sources
https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory

### Transformation 	1
**Description:** Dropped unnecessary columns

**Soundness Justification:** Columns like SNo,Symbol,Date are not required for exploratory analysis as they donot have any insight.

### Transformation 	2
**Description:** Replaced 0's with Mean for 'Volume' column

**Soundness Justification:** There are some records which has 0 for 'Volume' label. So, to avoid 0 values, I replaced them with the mean of the 'Volume' column.



## Visualization

### Visual 1 ScatterPlot-1(Bitcoin)
**Analysis:** The plot is between 'High' and 'Low' columns. The plot is almost linear which shows both of them increase at the same rate.

### Visual 2 ScatterPlot-2(Bitcoin)
**Analysis:** The plot is between 'Low' and 'Open' columns. The plot is almost linear which shows both of them increase at the same rate.

### Visual 3 ScatterPlot-3(Bitcoin)
**Analysis:** The plot is between 'Open' and 'Close' columns. The plot is almost linear which shows both of them increase at the same rate.

### Visual 4 ScatterPlot-4(Bitcoin)
**Analysis:** The plot is between 'Close' and 'High' columns. The plot is almost linear which shows both of them increase at the same rate.

### Visual 5 ScatterPlot-5(Bitcoin)
**Analysis:** The plot is between 'High' and 'Open' columns. The plot is almost linear which shows both of them increase at the same rate.

### Visual 6 ScatterPlot-6(Bitcoin)
**Analysis:** The plot is between 'Low' and 'Close' columns. The plot is almost linear which shows both of them increase at the same rate.

### Visual 7 Histogram(Bitcoin)
**Analysis:** The plot is for 'Bitcoin' label. It shows the number of occurences of Bitcoin in the whole data.

### Visual 8 ScatterPlot-1(Dogecoin)
**Analysis:** The plot is between 'High' and 'Low' columns. The plot is not so linear and both the attributes have different rate of increase.

### Visual 9 ScatterPlot-2(Dogecoin)
**Analysis:** The plot is between 'Low' and 'Open' columns. The plot is not so linear and both the attributes have different rate of increase.

### Visual 10 ScatterPlot-3(Dogecoin)
**Analysis:** The plot is between 'Open' and 'Close' columns. The plot is not so linear and both the attributes have different rate of increase.

### Visual 11 ScatterPlot-4(Dogecoin)
**Analysis:** The plot is between 'Close' and 'High' columns. The plot is not so linear and both the attributes have different rate of increase.

### Visual 12 ScatterPlot-5(Dogecoin)
**Analysis:** The plot is between 'High' and 'Open' columns. The plot is not so linear and both the attributes have different rate of increase.

### Visual 13 ScatterPlot-6(Dogecoin)
**Analysis:** The plot is between 'Low' and 'Close' columns. The plot is not so linear and both the attributes have different rate of increase.

### Visual 14 Histogram(Dogecoin)
**Analysis:** The plot is for 'Bitcoin' label. It shows the number of occurences of Dogecoin in the whole data.

### Visual 15 ScatterPlot-1(Ethereum)
**Analysis:** The plot is between 'High' and 'Low' columns. The plot is almost a straight line which shows both of them increase at the same rate.

### Visual 16 ScatterPlot-2(Ethereum)
**Analysis:** The plot is between 'Low' and 'Open' columns. The plot is almost a straight line which shows both of them increase at the same rate.

### Visual 17 ScatterPlot-3(Ethereum)
**Analysis:** The plot is between 'Open' and 'Close' columns. The plot is almost a straight line which shows both of them increase at the same rate.

### Visual 18 ScatterPlot-4(Ethereum)
**Analysis:** The plot is between 'Close' and 'High' columns. The plot is almost a straight line which shows both of them increase at the same rate.

### Visual 19 ScatterPlot-5(Ethereum)
**Analysis:** The plot is between 'High' and 'Open' columns. The plot is almost a straight line which shows both of them increase at the same rate.

### Visual 20 ScatterPlot-6(Ethereum)
**Analysis:** The plot is between 'Low' and 'Close' columns. The plot is almost a straight line which shows both of them increase at the same rate.

### Visual 21 Histogram(Ethereum)
**Analysis:** The plot is for 'Bitcoin' label. It shows the number of occurences of Ethereum in the whole data.


