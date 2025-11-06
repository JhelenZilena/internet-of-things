#Script description: Get Data (Temp and Hum) from Arduino
import serial
import time
import os

from supabase import create_client, Client
from getPort import port

url = "https://bcgbbgadtqtkavdsalyu.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJjZ2JiZ2FkdHF0a2F2ZHNhbHl1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA2MjI5MzMsImV4cCI6MjA3NjE5ODkzM30.zXRh3hcMO29zOdefjQvqtb9bpmNgVz3jhKNRX3lUkS0"
supabase: Client = create_client(url, key)

arduino_port = port # Don't worry by the port
baud_rate = 9600 # Baudios
ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)

id_sensor = 1  
id_station = 1 

print("📡 Escuchando datos del ESP32...\n")

while True:
    data = ser.readline().decode('utf-8').rstrip()

    #print(data)
    if data:
        humidity, temp_value = data.split(",")
        humidity = float(humidity)
        temp_value = float(temp_value)
        print(f"Humidity: {humidity}%, temp_value: {temp_value}°C")

response = supabase.table("sensor__data").insert({
                    "id_sensor": id_sensor,
                    "id_station": id_station,
                    "humidity": humidity,
                    "temp_value": temp_value,
                    "status": True
                }).execute()
if response.data:
    print("✅ Datos insertados correctamente en Supabase\n")
else:
    print(f"⚠️ No se insertaron datos: {response}\n")
except ValueError:
print(f"⚠️ Formato inválido recibido: {data}")
time.sleep(2)
    
except KeyboardInterrupt:
    print("\n👋 Programa detenido por el usuario.")
    break
except Exception as e:
print(f"❌ Error inesperado: {e}")
time.sleep(2)