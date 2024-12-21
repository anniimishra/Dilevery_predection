from flask import Flask, request, jsonify
import joblib
import pandas as pd


model = joblib.load('shipment_delay_model.pkl')
encoder_weather = joblib.load('encoder_weather.pkl')  
encoder_traffic = joblib.load('encoder_traffic.pkl')  

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input
        data = request.get_json()
        weather_conditions = data['Weather Conditions']
        traffic_conditions = data['Traffic Conditions']

        # Validate inputs
        if weather_conditions not in encoder_weather.classes_:
            return jsonify({
                "error": f"Invalid 'Weather Conditions': {weather_conditions}. "
                         f"Expected one of {list(encoder_weather.classes_)}"
            }), 400

        if traffic_conditions not in encoder_traffic.classes_:
            return jsonify({
                "error": f"Invalid 'Traffic Conditions': {traffic_conditions}. "
                         f"Expected one of {list(encoder_traffic.classes_)}"
            }), 400

        # Encode inputs
        weather_encoded = encoder_weather.transform([weather_conditions])[0]
        traffic_encoded = encoder_traffic.transform([traffic_conditions])[0]

        # Prepare input for the model
        input_data = pd.DataFrame([{
            'Weather Conditions': weather_encoded,
            'Traffic Conditions': traffic_encoded
        }])

        # Predict
        prediction = model.predict(input_data)
        result = 'Delayed' if prediction[0] == 1 else 'On Time'

        return jsonify({'Prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
