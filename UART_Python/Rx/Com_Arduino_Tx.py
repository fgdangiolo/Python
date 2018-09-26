
import serial
import time

com_arduino = serial.Serial('/dev/ttyACM0', 9600)

time.sleep(2)

dato_arduino = 'H'

while True:
    com_arduino.write(dato_arduino)
    print(dato_arduino)
   


