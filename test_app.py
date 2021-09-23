from fastapi.testclient import TestClient
from main import app
from stock_data import get_data


client = TestClient(app)


# Ensures that the application instance exists
def test_app_exists():
    assert app != None

# Ensures that index page loads correctly
def test_index_get():
    response = client.get("/")
    assert response.status_code == 200
    assert '<title>Stooq Data API</title>' in response.text 

# Ensures that stock page behaves as expected given valid symbol
def test_stock_success():
    response = client.get("/stock/amzn")
    assert response.status_code == 200
    assert response.json() == {"Short_Term_Trend": "Negative", "Medium_Term_Trend": "Negative", "Long_Term_Trend": "Positive"}

# Ensures that stock page behaves as expected given invalid symbol
def test_stock_failure():
    response = client.get("/stock/wrong_symbol")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}

# Ensures that get_data method works correctly given valid symbol
def test_get_data_success():
    data = get_data('amzn')
    result = {"Short_Term_Trend": "Negative", "Medium_Term_Trend": "Negative", "Long_Term_Trend": "Positive"}
    assert result == data

# Ensures that get_data method works correctly given invalid symbol
def test_get_data_failure():
    data = get_data('wrong_symbol')
    assert data == None
