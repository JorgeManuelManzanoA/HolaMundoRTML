import time
import random
import paho.mqtt.client as mqtt

MQTT_BROKER = "TU_IP"
MQTT_PORT = "TU_PUERTO"
MQTT_TOPIC = "TU_TOPICO"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def generate_temperature_data(client):
    """Generates random temperature data every second and publishes to MQTT broker."""
    while True:
        temp = random.uniform(-10, 40)  # Generate random temperatures between -10 and 40 degrees Celsius
        client.publish(MQTT_TOPIC, temp)
        print(f"Published temperature: {temp:.2f}°C")
        time.sleep(1)  # Wait 1 second before generating the next data

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    
    generate_temperature_data(client)
