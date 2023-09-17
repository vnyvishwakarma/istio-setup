# Simple Flask Application

This simple Flask application has two endpoints; one that handles GET requests and another that handles POST requests.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python and pip installed on your system. You can download Python from the [Python official website](https://www.python.org/).

### Installation

Clone the repository to your local machine.

Install the required Python packages using the following command:

```bash
pip install -r requirements.txt

```

### Project Structure
The project has the following structure:

app.py: This is the main file that contains the Flask application.
requirements.txt: This file contains the list of packages required to run the application.


```bash
python app.py
```
> Note:Your application will start running at `http://127.0.0.1:5000`

### GET Endpoint

Access the GET endpoint at the following URL:

```bash
http://127.0.0.1:5000/get-endpoint?name=YourName
```

> Note: Replace `"YourName"` with any name you want to use.

```bash
curl "http://127.0.0.1:5000/get-endpoint?name=YourName"
```

### POST Endpoint
Access the POST endpoint at the following URL:

```bash
http://127.0.0.1:5000/post-endpoint
```
Send a POST request with a JSON body using a tool like curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"key1": "value1", "key2": "value2"}' "http://127.0.0.1:5000/post-endpoint"
```