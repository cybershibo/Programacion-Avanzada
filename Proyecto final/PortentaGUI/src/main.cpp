#include <Arduino.h>
#include <Wire.h>
#include <Arduino_MachineControl.h>
#include "ArduinoJson.h"

using namespace machinecontrol;

struct CommandData {
  String command;
  int pin;
  String message;
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

  for (int i = 0; i < 8; ++i) {
    digital_inputs.pinMode(i, INPUT_PULLUP);
  }

  // Inicializar los pines programables
  if (!digital_programmables.init()) {
    Serial.println("Error initializing digital programmables!");
  }

  digital_programmables.setLatch();
}

CommandData commandReceived;

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('}');
    Serial.println(data);
    DynamicJsonDocument doc(1024);
    deserializeJson(doc, data);
    commandReceived.command = doc["command"].as<String>();
    commandReceived.pin = doc["pin"];
    commandReceived.message = doc["message"].as<String>();

    // Aplicar el comando recibido
    if (commandReceived.command == "digital_outputs") {
      if(commandReceived.message == "HIGH")
        digital_outputs.set(commandReceived.pin, HIGH);
      else
        digital_outputs.set(commandReceived.pin, LOW); 
    }
  }

  if (commandReceived.command == "digital_inputs") {
    // Realizar acciones específicas para la entrada digital según sea necesario
  }
}
