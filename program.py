import RPi.GPIO as GPIO
from Bluetin_Echo import Echo
GPIO.setmode(GPIO.BCM)
import time

ECHO_PIn = 16
TRIG_PIN = 20
LED_PIN = 27
SPEED = 315

GPIO.setup(27, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(27, 100)   # Initialize PWM on pwmPin 100Hz frequency

echo = Echo(TRIG_PIN, ECHO_PIn, SPEED)
samples = 2

pwm.start(0)

def setLed(percent):
    print(percent)
    pwm.ChangeDutyCycle(percent)


try:
    while True:
        result = echo.read('cm',samples)
        percent = 0
        if result < 5:
            percent = 100
        elif result < 20:
            percent = 50
        elif result < 50 :
            percent = 10

        setLed(percent)

except KeyboardInterrupt:
    print("ctrl-c pressed")


pwm.stop()
GPIO.cleanup()