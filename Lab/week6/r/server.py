from flask import Flask, jsonify
import random  # Simulate temperature sensor data

app = Flask(__name__)

# Route to provide temperature data
@app.route('/temperature', methods=['GET'])
def get_temperature():
    # Simulate temperature data
    temperature = round(random.uniform(20.0, 30.0), 2)  # Random value between 20°C and 30°C
    return jsonify({
        "temperature": temperature,
        "unit": "Celsius"
    })

# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Listen on all network interfaces

