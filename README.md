## Stooq API
### This app has one primary function: to display the current trend direction of financial instruments included in Stooq's database. To achieve this, the user inputs their desired parameters, and the application accesses the historical data for those instruments.

#### Once the data is accessed, the app calculates moving averages using three lookback periods: 50-day, 100-day, and 200-day. These moving averages provide a helpful indicator of the trend direction for each instrument.

The beauty of FastAPI is that it is designed to be performant and easy to use. It's lightweight, so it can handle heavy loads without sacrificing speed. And its intuitive design means that developers can quickly create APIs with minimal code.

As a result, this financial trend direction application is lightning fast and easy to use. With just a few clicks, users can gain valuable insight into the trend direction of various financial instruments. It's a powerful tool that can help traders and investors make informed decisions about their portfolios.

--------------------------------------------------

#### Main Features
* The **basic HTML landing/index page** serves as the initial point of contact between the user and the application. It's the first thing that the user sees, and it sets the tone for their entire experience. As such, it's essential that this landing page is well-designed, easy to navigate, and visually appealing. A well-designed landing page can make all the difference when it comes to user engagement and retention. By using a basic HTML landing page, developers can create a visually appealing, user-friendly entry point into the application. And the best part is that it can be done quickly and easily without a lot of overhead.
* **Interactive API documentation and exploration web user interfaces provided by FastAPI**. These interfaces are an essential tool for any developer who is working with APIs. They provide a user-friendly way to explore and interact with the API, making it easy to understand the available endpoints and request/response formats. FastAPI's interactive API documentation is particularly impressive because it is automatically generated based on the code. This means that developers don't need to spend a lot of time creating documentation manually. Instead, they can focus on writing code, and the documentation will be generated automatically. The API exploration web interface provided by FastAPI is also a powerful tool. It allows developers to test the API endpoints and see the responses in real-time. This is especially helpful when it comes to debugging and testing, as developers can quickly identify and fix any issues that arise.
* Capability of **returning HTTP exceptions** with a status code of 404 for non-existing symbols or tickers. When users are searching for financial instruments that are not available in the database, it is essential to inform them of this and prevent them from wasting time and effort searching for something that does not exist. With this feature, the application can identify when users enter non-existing symbols or tickers and then return a clear error message indicating that the requested data is not available. The HTTP exception with a status code of 404 is a standard way to inform users that the requested resource was not found. This response code is a part of the HTTP protocol and is used by all web servers and clients. By using this status code, the application can ensure that users receive an accurate and standard error message that they can understand. Moreover, this feature can improve the user experience by providing them with clear and informative feedback. It can help users quickly identify and correct any errors in their input and save them valuable time and effort. Additionally, it can prevent users from becoming frustrated with the application or abandoning it altogether due to lack of feedback or unclear error messages.
* One of the standout features of this application is the inclusion of **embedded interactive plotly visualizations charts**. These charts are a powerful tool for visualizing complex financial data, allowing users to easily identify trends, patterns, and insights. By leveraging the advanced charting capabilities of plotly, this application provides an immersive and interactive user experience that makes it easy to explore and analyze financial data in real-time. The plotly charts are fully customizable, giving users the ability to tailor their view of the data to meet their specific needs. Users can zoom in and out of charts, adjust the time horizon, and even overlay multiple data series to gain deeper insights into financial trends. This level of customization allows users to quickly identify and respond to changes in the market, making it an indispensable tool for any trader or investor. In addition to their flexibility and interactivity, plotly charts are also highly responsive and can be easily embedded into any web-based application. This makes it easy to integrate these powerful visualizations into your own financial applications, providing your users with a world-class experience that will help them make informed decisions and stay ahead of the curve. Whether you are building a trading platform, financial dashboard, or portfolio management tool, the plotly charts included in this application are sure to take your application to the next level.

--------------------------------------------------

### Code Coverage

<img src="https://github.com/mjaroszewski1979/stooq-api/blob/main/cov_report.png">

--------------------------------------------------

  ![caption](https://github.com/mjaroszewski1979/stooq-api/blob/main/stooq_mockup.png)

  
  Live | Code | Docker | Technologies
  ---- | ---- | ------ | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/deta_g.png">](https://8xl3m1.deta.dev/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/stooq-api) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/stooqapi) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/fastapi_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pandas.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/numpy_g.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/plotly.png">  &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/uvicorn_g.png">   
