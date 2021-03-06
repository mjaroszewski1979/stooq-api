import pandas_datareader.data as web

# Fetching data from Stooq API and returning current trend direction for given stock
def get_data(stock):
    try:
        trend = {}

        data = web.DataReader(stock, 'stooq')
        data = data['Close']
        data = data[::-1]
        
        # Creating variables for key technical lookback periods
        ma_50 = data.rolling(50).mean()
        ma_100 = data.rolling(100).mean()
        ma_200 = data.rolling(200).mean()

        # Comparing actual results
        if data[-1] > ma_50[-1]:
            trend['Short_Term_Trend'] = 'Positive'
        else:
            trend['Short_Term_Trend'] = 'Negative'
        if data[-1] > ma_100[-1]:
            trend['Medium_Term_Trend'] = 'Positive'
        else:
            trend['Medium_Term_Trend'] = 'Negative'
        if data[-1] > ma_200[-1]:
            trend['Long_Term_Trend'] = 'Positive'
        else:
            trend['Long_Term_Trend'] = 'Negative'

        return trend

    except:
        return None
    
    
    
