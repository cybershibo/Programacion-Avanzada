#include <Arduino.h>
#include <Wire.h>
#include <Arduino_MachineControl.h>
#include "ArduinoJson.h"

//#define DEBUG

using namespace machinecontrol;

int PROG_PINS[12] = {IO_WRITE_CH_PIN_00, 
                      IO_WRITE_CH_PIN_01, 
                      IO_WRITE_CH_PIN_02, 
                      IO_WRITE_CH_PIN_03, 
                      IO_WRITE_CH_PIN_04,
                      IO_WRITE_CH_PIN_05, 
                      IO_WRITE_CH_PIN_06, 
                      IO_WRITE_CH_PIN_07, 
                      IO_WRITE_CH_PIN_08, 
                      IO_WRITE_CH_PIN_09, 
                      IO_WRITE_CH_PIN_10, 
                      IO_WRITE_CH_PIN_11};

struct CommandData {
  String command;
  int pin;
  String message;
};

struct readInputData {
  String command;
};
// Variable para almacenar el estado de los pines
int pinStates[8] = {LOW, LOW, LOW, LOW, LOW, LOW, LOW, LOW};

void setup() {
  Serial.begin(9600);
  Wire.begin();

  // Inicializar las salidas digitales
  digital_outputs.setLatch();

  // Inicializar los pines de entrada digital
  if (!digital_inputs.init()) {
    Serial.println("Error initializing digital inputs!");
  }
  digital_inputs.begin();

  // Inicializar los pines programables
  if (!digital_programmables.init()) {
    Serial.println("Error initializing digital programmables!");
  }

  digital_programmables.setLatch();
}

CommandData commandReceived;
readInputData readInput;

void sendInputStates() {
  uint32_t inputs = digital_inputs.readAll();

  DynamicJsonDocument doc(1024);
  JsonObject root = doc.to<JsonObject>();

  for (int i = 0; i < 8; ++i) {
    root["Input_" + String(i)] = (inputs & (1 << i)) >> i;
  }

  serializeJson(doc, Serial);
  Serial.println();
  delay(100);  // Añadimos un pequeño retraso
}

void productionCode(){
    String data = Serial.readStringUntil('}');
    Serial.println(data);
    DynamicJsonDocument doc(1024);
    deserializeJson(doc, data);
    readInput.command = doc["command"].as<String>();
    commandReceived.command = doc["command"].as<String>();
    commandReceived.pin = doc["pin"].as<int>();
    commandReceived.message = doc["message"].as<String>();

    // Aplicar el comando recibido
    if (commandReceived.command == "digital_outputs") {
      if(commandReceived.message == "HIGH")
        digital_outputs.set(commandReceived.pin, HIGH);
      else
        digital_outputs.set(commandReceived.pin, LOW); 
    }

if(commandReceived.command == "digital_prog"){
        if(commandReceived.message == "HIGH")
        digital_programmables.set(commandReceived.pin, HIGH);
      else
        digital_programmables.set(commandReceived.pin, LOW); 
}

  if(readInput.command == "digital_inputs")
    sendInputStates();
  
}

void debuingCode(){

  sendInputStates();

  for(int x = 0; x < 8; x++){
      bool readPin = digital_inputs.read(x);
      Serial.print(String(readPin) + " ");
    delay(150);
  }
  Serial.println();
  for(int x = 0; x<=7; x++){
    if(pinStates[x] == LOW){
      pinStates[x] = HIGH;
      digital_outputs.set(x, HIGH);
      delay(150);
    }
      else{
        pinStates[x] = LOW;
        digital_outputs.set(x, LOW);
        delay(150);
      }
  }
    digital_outputs.setAll(LOW);
    delay(100);
        digital_programmables.writeAll(SWITCH_ON_ALL);
        delay(1000);
        digital_programmables.writeAll(SWITCH_OFF_ALL);
        delay(1000);
        if(digital_programmables.read(IO_READ_CH_PIN_08) == HIGH){
          digital_outputs.set(0, HIGH);
        }
        else if(digital_programmables.read(IO_READ_CH_PIN_09) == LOW){
          digital_outputs.set(0, LOW);
        }
        if(digital_programmables.read(IO_READ_CH_PIN_10) == HIGH){
          digital_outputs.set(1, HIGH);
        }
        else if(digital_programmables.read(IO_READ_CH_PIN_11) == LOW){
          digital_outputs.set(1, LOW);
        }
        if(digital_programmables.read(IO_READ_CH_PIN_02) == HIGH){
          digital_outputs.set(2, HIGH);
        }
        else if(digital_programmables.read(IO_READ_CH_PIN_02) == LOW){
          digital_outputs.set(2, LOW);
        }
        if(digital_programmables.read(IO_READ_CH_PIN_03) == HIGH){
          digital_outputs.set(3, HIGH);
        }
        else if(digital_programmables.read(IO_READ_CH_PIN_03) == LOW){
          digital_outputs.set(3, LOW);
        }
        if(digital_programmables.read(IO_READ_CH_PIN_04) == HIGH){
          digital_outputs.set(4, HIGH);
        }
        else if(digital_programmables.read(IO_READ_CH_PIN_04) == LOW){
          digital_outputs.set(4, LOW);
        }
        if(digital_programmables.read(IO_READ_CH_PIN_05) == HIGH){
          digital_outputs.set(5, HIGH);
        }
        else if(digital_programmables.read(IO_READ_CH_PIN_05) == LOW){
          digital_outputs.set(5, LOW);
        }
        if(digital_programmables.read(IO_READ_CH_PIN_06) == HIGH){
          digital_outputs.set(6, HIGH);
        }
        else if(digital_programmables.read(IO_READ_CH_PIN_06) == LOW){
          digital_outputs.set(6, LOW);
        }
        if(digital_programmables.read(IO_READ_CH_PIN_07) == HIGH){
          digital_outputs.set(7, HIGH);
        }
        else if(digital_programmables.read(IO_READ_CH_PIN_07) == LOW){
          digital_outputs.set(7, LOW);
        }

  uint32_t inputs = digital_inputs.readAll();
  Serial.println("CH00: " + String((inputs & (1 << DIN_READ_CH_PIN_00)) >> DIN_READ_CH_PIN_00));
  Serial.println("CH01: " + String((inputs & (1 << DIN_READ_CH_PIN_01)) >> DIN_READ_CH_PIN_01));
  Serial.println("CH02: " + String((inputs & (1 << DIN_READ_CH_PIN_02)) >> DIN_READ_CH_PIN_02));
  Serial.println("CH03: " + String((inputs & (1 << DIN_READ_CH_PIN_03)) >> DIN_READ_CH_PIN_03));
  Serial.println("CH04: " + String((inputs & (1 << DIN_READ_CH_PIN_04)) >> DIN_READ_CH_PIN_04));
  Serial.println("CH05: " + String((inputs & (1 << DIN_READ_CH_PIN_05)) >> DIN_READ_CH_PIN_05));
  Serial.println("CH06: " + String((inputs & (1 << DIN_READ_CH_PIN_06)) >> DIN_READ_CH_PIN_06));
  Serial.println("CH07: " + String((inputs & (1 << DIN_READ_CH_PIN_07)) >> DIN_READ_CH_PIN_07));
  Serial.println();

}

void loop() {
  #ifdef DEBUG
    debuingCode();
  #else
    productionCode();
  #endif
}
