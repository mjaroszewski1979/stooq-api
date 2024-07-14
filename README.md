## Stooq API
### This app has one primary function: to display the current trend direction of financial instruments included in Stooq's database. To achieve this, the user inputs their desired parameters, and the application accesses the historical data for those instruments.

#### Once the data is accessed, the app calculates moving averages using three lookback periods: 50-day, 100-day, and 200-day. These moving averages provide a helpful indicator of the trend direction for each instrument.


### Features
* Data Fetching: Retrieves historical data using pandas-datareader.
* Trend Analysis: Calculates moving averages to indicate trend direction.
* Interactive Documentation: Automatically generated API docs using FastAPI.
* Error Handling: Returns 404 status for non-existent symbols/tickers.
* Plotly Visualizations: Embeds interactive charts for data analysis.

### Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/mjaroszewski1979/stooq-api.git
  cd stooq-api
  ```
2. Create a virtual environment:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Usage

1. Run the application:
  ```bash
  uvicorn main:app --reload
  ```
2. Access the application at http://127.0.0.1:8000/ to view and interact with the API.
   
### Testing

1. Run unit tests:
  ```bash
  pytest
  ```
### Code Coverage

<img src="https://github.com/mjaroszewski1979/stooq-api/blob/main/cov_report.png">

### Docker

1. Build the Docker image:
  ```bash
  docker build -t stooq-api .
  ```

2. Run the Docker container:
  ```bash
  docker run -p 8000:8000 --env-file .env stooq-api
  ```

### Technologies Used
* FastAPI: Web framework for building the application.
* Uvicorn: ASGI web server implementation for async frameworks, ensuring efficient performance.
* Pandas-Datareader: Fetching financial data.
* Plotly: For creating interactive charts.
* Docker: Containerization of the application.

### Contributing
* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Make your changes and commit them (git commit -m 'Add new feature').
* Push to the branch (git push origin feature-branch).
* Open a pull request.

### Contact
For questions or feedback, please contact [mjaroszewski1979.](https://github.com/mjaroszewski1979)


  ![caption](https://github.com/mjaroszewski1979/stooq-api/blob/main/stooq_mockup.png)

  
  Live | Code | Docker | Technologies
  ---- | ---- | ------ | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/deta_g.png">](https://8xl3m1.deta.dev/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/stooq-api) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/stooqapi) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/fastapi_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pandas.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/numpy_g.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/plotly.png">  &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/uvicorn_g.png">   
