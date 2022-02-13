# IoT Sensor Web API

The REST API was built with Django Rest framework. The server receives the data from the clients through REST API, and stores the data into the database. The server make OpenWeather API and collect the data needed for analytics report.


## Setup and Configuration

Setup and activate the env
```
python -m venv env
env\Scripts\activate # windows
source env/bin/activate # mac/linux
```
Install the libraries into the virtual environment if needed
```
pip install -r requirements.txt
```
Make pyhton migration if needed
```
cd sensor
python manage.py migrate
```
Run the server
```
cd sensor
python manage.py runserver <port>
```

### REST API Endpoints

| Url | Endpoint Description | HTTP method | Expected Header Request | Expected Response |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| /api/data | submit data as needed | POST | Content-Type: application/json | 200 response status |

Sample JSON Request Format
```
{
    "sensor": "1",
    "temp_c": "27.1",
    "temp_f": "88.9",
    "humidity": "67.0",
    "sound": "100"
}
```
