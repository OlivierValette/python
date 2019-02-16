import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
print("Led On")
GPIO.output(18, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
time.sleep(5)
GPIO.output(18, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
print("Led Off")
GPIO.cleanup()
