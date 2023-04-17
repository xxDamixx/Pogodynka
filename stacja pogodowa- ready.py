#Autor: Damian Popławski
import time
import RPi.GPIO as GPIO
from seeed_dht import DHT
from grove.display.jhd1802 import JHD1802

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14, GPIO.OUT)
GPIO.output(14, GPIO.HIGH)

temperature_max = 22.0
humidity_max = 88

lcd = JHD1802()
sensor = DHT('11', 5)

try:
    while True:
        humi, temp = sensor.read()
        print('temperature {}C, humidity {}%'.format(temp, humi))

        lcd.setCursor(0, 0)
        lcd.write('temperatura: {0:2}C'.format(temp))

        lcd.setCursor(1, 0)
        lcd.write('humidity: {0:5}%'.format(humi))

        if (temp > temperatura_max):
                GPIO.output(14, GPIO.LOW)            
                print('alarm temperatury')
        else: GPIO.output(14, GPIO.HIGH)
                
        if (humi > humidity_max):
            GPIO.output(14, GPIO.LOW)
            print('alarm wilgotno')
        else:
            GPIO.output(14, GPIO.HIGH)

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.output(21, GPIO.HIGH)
    print('Koniec')
    GPIO.cleanup()
