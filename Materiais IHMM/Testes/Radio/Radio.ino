#include "BluetoothSerial.h"
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

const int fmModuleTX = 1;
const int fmModuleRX = 3;

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Pleas run `make menuconfig`to and enabe it
#endif

BluetoothSerial SerialBT;
uint8_t counter = 0;

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; // I2C

float fs = 0.0;

void setup() {
  pinMode(2,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(34,INPUT);
  pinMode(15,OUTPUT);
  Serial.begin(115200);
  Serial.setTimeout(1000);
  SerialBT.begin("Rádio DelFM");  
  Serial2.begin(38400, SERIAL_8N1, fmModuleRX, fmModuleTX); // Configurado para a velocidade do módulo FM
  delay(1000);
  Serial2.print("AT+BANK=01");
  delay(200);

  bool status;

  // default settings
  // (you can also pass in a Wire library object like &Wire2)
  status = bme.begin(0x76);  
  if (!status) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }

  while (Serial2.available()) {
    String response = Serial2.readStringUntil('\n');
  }
}

void loop() {

  String V = String(bme.readTemperature()) + "_" + String(bme.readHumidity()) + "_" + String((analogRead(34)/4095.0)*3.3) + "_" + String(fs);
  SerialBT.println(V);
  delay(500);

  if (SerialBT.available()) {
    String dado = SerialBT.readString();
    digitalWrite(2,1);
    delay(10);
    digitalWrite(2,0);

    if (dado == "F_up"){
      Serial2.print("AT+FREU");
      fs = fs+0.1;
      if(fs>108.0){fs=108.0;}
      delay(500);
      while (Serial2.available()) {
        String response = Serial2.readStringUntil('\n');
        String frequency = response.substring(4);
        float frequencia = frequency.toFloat();
        fs = frequencia;
        frequency= String(frequencia);
        //SerialBT.println(frequency);
      }
    }

    if (dado == "F_down"){
      Serial2.print("AT+FRED");
      fs = fs-0.1;
      if(fs<87.5){fs=87.5;}
      delay(500);
      while (Serial2.available()) {
        String response = Serial2.readStringUntil('\n');
        String frequency = response.substring(4);
        float frequencia = frequency.toFloat();
        frequencia = frequencia/10.0;
        fs = frequencia;
        frequency = String(frequencia);
        //SerialBT.println(frequency);
      }
    }

    if (dado == "play"){
      Serial2.print("AT+PAUS");
      delay(50);
      while (Serial2.available()) {
        String response = Serial2.readStringUntil('\n');
      }
    }

    if (dado == "V_up"){
      Serial2.print("AT+VOLU");
      delay(50);
      while (Serial2.available()) {
        String response = Serial2.readStringUntil('\n');
      }
    }

    if (dado == "V_down"){
      Serial2.print("AT+VOLD");
      delay(50);
      while (Serial2.available()) {
        String response = Serial2.readStringUntil('\n');
      }
    }

    if (dado == "cooler"){
      digitalWrite(15, !digitalRead(15));
    }
    if (dado == "on_off"){
      digitalWrite(4, !digitalRead(4));
    }

    else{
    float frequencia = dado.toFloat();
    frequencia = frequencia/10.0;
    fs = frequencia;
    String frequency = String(frequencia) + "MHz";
    
      String command = "AT+FRE=" + String(dado);
      Serial2.print(command);

      delay(50);  // Aguarde para dar tempo ao módulo de processar o comando

      while (Serial2.available()) {
        String response = Serial2.readStringUntil('\n');
       // Serial.println(response);
      }

    }
  }
}
