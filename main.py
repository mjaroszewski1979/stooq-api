# Import the FastAPI module for creating API endpoints
import fastapi
# Import uvicorn for running the FastAPI application
import uvicorn
# Import custom stock_data module for fetching stock data
import stock_data
# Import HTMLResponse for returning HTML content
from fastapi.responses import HTMLResponse

# Initialize FastAPI app
app = fastapi.FastAPI()

@app.get('/')
def index():
    """
    Endpoint to display the main page of the Stooq Data API application.
    Returns an HTML page with information about the application and how to use the API.
    """
    
    html_content = """
    <html>
        <head>
            <title>Stooq Data API</title>
        </head>
        <body>
            <div style="margin: 7%;">
            <h2 style="text-align:center;">This is an application build with one of the fastest Python web frameworks - FastAPI. 
            The main function is to display current trend direction for all financial instruments included in Stooq's database. 
            After receiving user's input, application is gaining access to the historical data and then calculates 
            moving averages by using 50-day, 100-day and 200-day lookback period.</h2>
            <h3 style="text-align:center;">Call /stock/{symbol} to use the API</h3>
            <br/>
            <h3 style="text-align: center;">See the /docs for interactive API documentation and exploration web user interfaces provided by FastAPI</h3>
            </div>
            <div style="text-align:center;">
            <iframe width="500" height="400" frameborder="0" scrolling="no" src="//plotly.com/~mjaroszewski/21.embed"></iframe>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get('/stock/{symbol}')
def get_data(symbol):
    """
    Endpoint to fetch and return stock data for a given symbol.
    Args:
        symbol (str): The stock symbol for which data is to be fetched.
    Returns:
        data (dict): The stock data retrieved from the stock_data module.
    Raises:
        fastapi.HTTPException: If the provided stock symbol does not exist, returns a 404 status code.
    """
    
    data = stock_data.get_data(symbol)
    
    # Return a 404 status code if the provided stock symbol does not exist
    if not data:
        raise fastapi.HTTPException(status_code=404)

    return data

