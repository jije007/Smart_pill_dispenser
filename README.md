💊 Smart Pill Dispenser

An IoT-based Smart Pill Dispenser system designed to automatically dispense medicines at scheduled intervals using an ESP32, RTC module, and servo motors. This project aims to help patients, especially the elderly or chronically ill, adhere to medication schedules with minimal manual effort.

🧠 Project Overview

The Smart Pill Dispenser automates the process of medicine management by integrating real-time scheduling, automated dispensing, and cloud-based monitoring. It dispenses pills at predefined times, notifies users with alarms, and logs all events to the Adafruit IO cloud platform for remote tracking.

⚙️ Features

Automated pill dispensing using servo motors.

Real-Time Clock (DS3231) for accurate scheduling.

Wi-Fi-enabled ESP32 microcontroller for cloud connectivity.

Buzzer and LED alerts for reminder notifications.

Real-time dose tracking on Adafruit IO dashboard.

Reliable, affordable, and easy-to-use healthcare solution.

🧩 Components Used

ESP32 Development Board

DS3231 RTC Module

Micro Servo Motors (SG90 / MG90S)

Buzzer

LED

Adafruit IO Cloud

🖥️ Software Used

MicroPython (for ESP32)

Wokwi Simulator – for virtual testing and debugging

Adafruit IO Dashboard – for cloud visualization and data logging

Network & urequests libraries – for HTTP communication

DS3231 Library – for RTC time management

🔌 Pin Connections
ESP32 Pin	Component	Description
GPIO21	SDA (RTC)	I²C Data
GPIO22	SCL (RTC)	I²C Clock
GPIO15	Servo 1	PWM Control
GPIO2	Servo 2	PWM Control
GPIO4	Servo 3	PWM Control
GPIO5	Buzzer	Alert Signal
GPIO18	LED	Notification Indicator
3.3V / 5V	Power	To RTC / Servo (external recommended)
GND	Ground	Common connection
🔄 Working Principle

The RTC module maintains accurate time and sends it to the ESP32.

At each preset time, the ESP32 activates a specific servo motor to dispense the corresponding pill.

A buzzer and LED alert the user to take the medicine.

Dispensing details (time, servo number, dose count) are uploaded to Adafruit IO for remote monitoring.

⚠️ Challenges Faced

Synchronizing time between RTC and ESP32.

Calibrating servo angles for precise dispensing.

Managing stable power supply when multiple servos run.

Handling Wi-Fi disconnections during Adafruit IO updates.

✅ Conclusion

The Smart Pill Dispenser successfully automates medication management, ensuring timely and accurate dosing with real-time monitoring. It enhances patient safety, reduces human error, and provides a foundation for future improvements such as mobile app integration, voice reminders, and dose tracking analytics.
