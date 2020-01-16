
import serial
import time

def get_data_port(usb_port):
    data_read = usb_port.readline()
    print(data_read)



if __name__ == "__main__":

    usb_port = serial.Serial('/dev/ttyUSB0', 9600)

    while (True):
        #Obtain data from USB port
        get_data_port(usb_port)
    
   


