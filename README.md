# Shipment Delay Prediction API

This project provides a REST API to predict shipment delays based on weather and traffic conditions using a trained Random Forest model. The API is built using Flask.

---

## Features

- Predict shipment delays (`Delayed` or `On Time`).
- Encodes categorical inputs like weather and traffic conditions using `LabelEncoder`.
- Provides validation for input data.

---

## API Endpoints

### 1. Prediction Endpoint

**URL:** `/predict`  
**Method:** `POST`  

**Payload:**  
```json
{
    "Weather Conditions": "Rainy",
    "Traffic Conditions": "Heavy"
}
