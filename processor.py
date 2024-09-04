import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import paho.mqtt.client as mqtt

MQTT_BROKER = "TU_IP"
MQTT_PORT = "TU_PUERTO"
MQTT_TOPIC = "TU_TOPICO"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    temp = float(msg.payload.decode())
    process_temperature(temp)

def process_temperature(temp):
    """Processes received temperature data and makes predictions."""
    data.append(temp)
    if len(data) > 1:
        # Create DataFrame with the data
        df = pd.DataFrame({'x': range(len(data)), 'y': data})
        X = df[['x']].values
        y = df['y'].values
        
        # Train the model
        model.fit(X, y)
        
        # Make a prediction for the next data point
        next_index = len(data)
        prediction = model.predict(np.array([[next_index]]))
        print(f"Latest temperature: {temp:.2f}°C, Predicted temperature for next time: {prediction[0]:.2f}°C")
    else:
        print(f"Latest temperature: {temp:.2f}°C")

if __name__ == "__main__":
    data = []
    model = LinearRegression()
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()
