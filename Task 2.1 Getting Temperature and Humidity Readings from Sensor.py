import RPi.GPIO as RPi
import dht11
import time

RPi.setwarnings(False)
RPi.setmode(RPi.BCM)
RPi.cleanup()

while True:
    instance = dht11.DHT11(pin=4)
    result = instance.read()
    while not result.is_valid():
        result = instance.read()

    temperature = result.temperature
    humidity = result.humidity

    print("Temperature: %-3.1f C" % temperature)
    print("Humidity: %-3.1f %%" % humidity)

    time.sleep(0.1)



