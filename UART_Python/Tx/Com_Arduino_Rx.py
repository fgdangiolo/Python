
import serial
import time

com_arduino = serial.Serial('/dev/ttyUSB0', 9600)

time.sleep(2)

while True:
    dato_arduino = com_arduino.readline()
    print(dato_arduino)
   


