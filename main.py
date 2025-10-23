# Smart Pill Dispenser - ESP32 + Adafruit IO Logging (1-minute dispense)
import network, urequests, time
from machine import Pin, PWM, SoftI2C
from ds3231 import DS3231  # RTC module library

# ---------- Wi-Fi ----------
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASS = ""

# ---------- Adafruit IO ----------
AIO_USERNAME = "jije007"
AIO_KEY = "AIO_key of yours"
AIO_FEED = "pill-disp-log"

# ---------- Hardware Pins ----------
servo_pins = [15, 2, 4]  # Servos for 3 pill compartments
servos = [PWM(Pin(p), freq=50) for p in servo_pins]

buzzer = Pin(5, Pin.OUT)
led = Pin(18, Pin.OUT)

# ---------- RTC (I2C) ----------
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
rtc = DS3231(i2c)

# ---------- Global variables ----------
dispense_count = 0
servo_index = 0
dispense_log = []
last_dispense_time = time.time()  # Track seconds since start

# ---------- Wi-Fi connect ----------
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASS)
print("Connecting to Wi-Fi...", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)
print("\nConnected:", wlan.ifconfig())

# ---------- Alerts ----------
def alert():
    for _ in range(3):
        led.value(1)
        buzzer.value(1)
        time.sleep(0.2)
        led.value(0)
        buzzer.value(0)
        time.sleep(0.2)

# ---------- Dispense ----------
def dispense(servo_idx):
    global dispense_count
    print(f"Dispensing from servo {servo_idx+1}...")
    servos[servo_idx].duty(40)  # Rotate (adjust for your servo)
    time.sleep(0.5)
    servos[servo_idx].duty(77)  # Back to normal position
    time.sleep(0.2)
    dispense_count += 1
    print("Done.")
    return dispense_count

# ---------- Adafruit IO Logging ----------
def log_to_adafruit(time_str, servo_idx, count):
    try:
        if not wlan.isconnected():
            wlan.connect(WIFI_SSID, WIFI_PASS)
            while not wlan.isconnected():
                time.sleep(0.5)

        url = f"https://io.adafruit.com/api/v2/jije007/feeds/pill-disp-log/data"
        headers = {"X-AIO-Key": AIO_KEY, "Content-Type": "application/json"}
        data = {"value": f"{time_str},servo{servo_idx+1},{count}"}
        response = urequests.post(url, json=data, headers=headers)
        print("Adafruit IO log sent:", response.status_code, data)
        response.close()
    except Exception as e:
        print("Adafruit IO error:", e)
    dispense_log.append((time_str, servo_idx, count))

# ---------- Main loop ----------
while True:
    y, m, d, h, mi, s, wd = rtc.datetime()
    time_str = f"{h:02d}:{mi:02d}:{s:02d}"
    print("Time:", time_str)

    now = time.time()
    if now - last_dispense_time >= 60:  # Every 1 minute
        alert()
        count = dispense(servo_index)
        log_to_adafruit(time_str, servo_index, count)

        servo_index = (servo_index + 1) % 3  # Rotate through servos
        last_dispense_time = now

    time.sleep(1)
