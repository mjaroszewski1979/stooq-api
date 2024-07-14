# Import TestClient from fastapi.testclient for testing the FastAPI app
from fastapi.testclient import TestClient
# Import the FastAPI app instance from the main module
from main import app
# Import the get_data function from the stock_data module
from stock_data import get_data

# Create a TestClient instance for testing the FastAPI app
client = TestClient(app)


def test_app_exists():
    """
    Test to ensure that the FastAPI application instance exists.
    """
    assert app != None

def test_index_get():
    """
    Test to ensure that the index page loads correctly.
    Verifies that the status code is 200 and the response contains the expected HTML content.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert '<title>Stooq Data API</title>' in response.text 

def test_stock_success():
    """
    Test to ensure that the stock page behaves as expected when given a valid stock symbol.
    Verifies that the status code is 200 and the response JSON matches the expected trend data.
    """
    response = client.get("/stock/amzn")
    assert response.status_code == 200
    assert response.json() == {"Short_Term_Trend": "Negative", "Medium_Term_Trend": "Negative", "Long_Term_Trend": "Positive"}

def test_stock_failure():
    """
    Test to ensure that the stock page behaves as expected when given an invalid stock symbol.
    Verifies that the status code is 404 and the response JSON contains the appropriate error message.
    """
    response = client.get("/stock/wrong_symbol")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}

def test_get_data_success():
    """
    Test to ensure that the get_data method works correctly when given a valid stock symbol.
    Verifies that the returned trend data matches the expected result.
    """
    data = get_data('amzn')
    result = {"Short_Term_Trend": "Negative", "Medium_Term_Trend": "Negative", "Long_Term_Trend": "Positive"}
    assert result == data

def test_get_data_failure():
    """
    Test to ensure that the get_data method works correctly when given an invalid stock symbol.
    Verifies that the method returns None for an invalid symbol.
    """
    data = get_data('wrong_symbol')
    assert data == None
