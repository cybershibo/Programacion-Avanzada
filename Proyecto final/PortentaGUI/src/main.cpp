#include <Arduino.h>
#include <ArduinoJson.h>
#include <Arduino_MachineControl.h>
#include <rs485.h>
#include <Wire.h>

#define BOARD_TYPE "Portenta H7"
#define DEVICE_ID 1
#define jsonBufferSize 256
#define DEVICE_BAUDRATE 9600

const int numPins = 8;
int pinStates[numPins] = {0}; // Initial pin states

struct DeviceStatus {
  int pinStates[numPins];
};

void handleCommand(String jsonData);
void sendDeviceStatus();

using namespace machinecontrol;

void setup() {
  Serial.begin(DEVICE_BAUDRATE);
  digital_outputs.setLatch();
  digital_outputs.setAll(0);
}

void loop() {
  if (Serial.available() > 0) {
    String receivedData = Serial.readStringUntil('\n');
    handleCommand(receivedData);
  }
}

void handleCommand(String jsonData) {
  DynamicJsonDocument doc(128);
  deserializeJson(doc, jsonData);

  int command = doc["command"];
  int pinIndex = doc["pinIndex"];

  if (pinIndex >= 0 && pinIndex < numPins) {
    switch (command) {
      case 1: // Example: Turn on pin
        digital_outputs.set(pinIndex, 1);
        pinStates[pinIndex] = 1;
        break;
      case 2: // Example: Turn off pin
        digital_outputs.set(pinIndex, 0);
        pinStates[pinIndex] = 0;
        break;
      // Add more cases as needed for your commands
    }

    // Send device status back to Python GUI
    sendDeviceStatus();
  }
}

void sendDeviceStatus() {
  DeviceStatus deviceStatus;
  for (int i = 0; i < numPins; ++i) {
    deviceStatus.pinStates[i] = pinStates[i];
  }

  DynamicJsonDocument doc(128);
  for (int i = 0; i < numPins; ++i) {
    doc["pinStates"][i] = deviceStatus.pinStates[i];
  }

  String jsonData;
  serializeJson(doc, jsonData);
  Serial.println(jsonData);
}
