import fastapi
import uvicorn
import stock_data
from fastapi.responses import HTMLResponse


app = fastapi.FastAPI()

@app.get('/')
def index():
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
    data = stock_data.get_data(symbol)
    
    # Returning correct status code when provided with non existing stock symbol
    if not data:
        raise fastapi.HTTPException(status_code=404)

    return data

