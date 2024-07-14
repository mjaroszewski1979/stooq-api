# Import the web module from pandas_datareader for fetching financial data
import pandas_datareader.data as web

def get_data(stock):
    """
    Fetch stock data from Stooq API and determine the current trend direction.
    Args:
        stock (str): The stock symbol for which data is to be fetched.
    Returns:
        trend (dict): A dictionary containing the trend direction for short, medium, and long-term periods.
    """
    
    try:
        # Initialize an empty dictionary to store trend directions
        trend = {}

        # Fetch stock data from the Stooq API
        data = web.DataReader(stock, 'stooq')
        # Extract the closing prices
        data = data['Close']
        # Reverse the data to have the latest data at the end
        data = data[::-1]
        
        # Creating variables for key technical lookback periods
        ma_50 = data.rolling(50).mean()
        ma_100 = data.rolling(100).mean()
        ma_200 = data.rolling(200).mean()

        # Comparing actual results with moving averages to determine trend direction
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

        # Return the dictionary with trend directions
        return trend

    except:
        # Return None if there is any exception during data fetching or processing
        return None
    
    
    
