from flask import Flask, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/api/send_data', methods=['POST'])
def receive_data():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    date = data.get('date')

    # Process the received data (this is a placeholder for your actual processing logic)
    current_time = datetime.now().strftime("%H:%M:%S")
    actual_load = random.randint(80, 120)  # Simulated actual load
    predicted_load = random.randint(90, 110)  # Simulated predicted load

    print(f"Received data: Lat: {latitude}, Lon: {longitude}, Date: {date}")

    # Return a response
    return jsonify({
        "time": current_time,
        "actual_load": f"{actual_load} MW",
        "predicted_load": f"{predicted_load} MW"
    })

if __name__ == '_main_':
    app.run(debug=True)