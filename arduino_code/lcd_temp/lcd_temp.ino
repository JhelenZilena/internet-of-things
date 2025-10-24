#include <DHT.h>

#define DHTPIN 9        
#define DHTTYPE DHT11   

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("Iniciando sensor DHT11...");
}

void loop() {
  float temperatura = dht.readTemperature(); 
  float humedad = dht.readHumidity();        

  // Verificar si la lectura fue exitosa
  if (isnan(temperatura) || isnan(humedad)) {
    Serial.println("Error al leer el sensor DHT11");
  } else {
    Serial.print("Temperatura: ");
    Serial.print(temperatura);
    Serial.print(" °C  |  Humedad: ");
    Serial.print(humedad);
    Serial.println(" %");
  }

  delay(1000); 
}
