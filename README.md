Shipment Delay Prediction API
This project provides a REST API to predict shipment delays based on weather and traffic conditions using a trained Random Forest model. The API is built using Flask.

Features
Predict shipment delays (Delayed or On Time).
Encodes categorical inputs like weather and traffic conditions using LabelEncoder.
Provides validation for input data. 

API Endpoints
1. Prediction Endpoint
URL: /predict
Method: POST
Payload:

json
Copy code
{
    "Weather Conditions": "Rainy",
    "Traffic Conditions": "Heavy"
}
Response:

json
Copy code
{
    "Prediction": "Delayed"
}
2. Health Check Endpoint
URL: /
Method: GET
Response:

json
Copy code
{
    "message": "Welcome to the delay prediction API!"
}
Notes
Weather Conditions and Traffic Conditions: Supported values are based on the categories used during training:
Weather Conditions: ["Rainy", "Sunny", "Cloudy", "Foggy"]
Traffic Conditions: ["Heavy", "Moderate", "Light"]
Ensure that these values match the dataset used during training.
