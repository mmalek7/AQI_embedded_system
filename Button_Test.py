# Import the "wiringpi" library with the alias name "WiPi"
# import wiringpi as WiPi
import RPi.GPIO as RPI
# Import the sleep function from the time module
from time import sleep
# Definition of Pins of PI-Trokli system: Here the directional buttons
PinButtonLeft = 25
PinButtonRight = 19
PinButtonUp = 26
PinButtonDown = 13
PinBuzzer = 18
PinRelay = 21
PinVibration = 27
# Define an array with all input pins
GPIOInputPins = [PinButtonLeft, PinButtonDown, PinButtonRight]
ButtonDescription = ["Left", "Down", "Right"]
# Define an array with all output pins
GPIOOutputPins = [PinRelay, PinVibration, PinBuzzer]
ActuatorDescription = ["Relay", "VibrationAlarm", "Buzzer"]
# Defining that we want to use the GPIO (BCM) numberings system
# WiPi.wiringPiSetupGpio()
RPI.setmode(RPI.BCM)
# Iterate through all elements of the GPIOInputPins array
#for CurrentPin in GPIOInputPins:
    # Defining that we want to utilise the defined input pins as input
    # WiPi.pinMode(CurrentPin, 0)
    # Deactivating PullUp/PullDown resistance
    # WiPi.pullUpDnControl(CurrentPin, 0)
RPI.setup(GPIOInputPins, RPI.IN, pull_up_down=RPI.PUD_OFF)

# Iterate through all elements of the GPIOOutputPins array
#for CurrentPin in GPIOOutputPins:
    # Defining that we want to utilise the defined output pins as output
    # WiPi.pinMode(CurrentPin, 1)
RPI.setup(GPIOOutputPins, RPI.OUT, pull_up_down=RPI.PUD_OFF)

# Continue the program FOREVER
while 1:
    # Iterate through all elements of the GPIOInputPins array by using an index
    for index in range(0, len(GPIOInputPins)):
        # Reading the current pin
        # if not WiPi.digitalRead(GPIOInputPins[index]):
        if not RPI.input(GPIOInputPins[index]):
            # Show which button was pressed
            print('Button pressed:')
            print(ButtonDescription[index])
            # Show which output will be started
            print('Associated output:')
            print(ActuatorDescription[index])
            # In case the actual button is pressed, start the associated output and stop it again
            # Turn the output on
            # WiPi.digitalWrite(GPIOOutputPins[index], 1)
            RPI.output(GPIOOutputPins[index], RPI.HIGH)
            # Wait for specific time
            sleep(1)
            # Turn the output off
            # WiPi.digitalWrite(GPIOOutputPins[index], 0)
            RPI.output(GPIOOutputPins[index], RPI.LOW)





