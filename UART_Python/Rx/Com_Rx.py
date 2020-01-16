
import serial


def get_data_port(usb_port):

    #Flush of file like objects
    usb_port.flushInput()

    #Read data from port
    data_read = usb_port.readline()

    return(data_read)
    
def data_to_string(data):

    #Convert data in bytes to string
    data_string = data.decode()

    return(data_string)


if __name__ == "__main__":

    #Create a por objet
    usb_port = serial.Serial('/dev/ttyUSB0', 9600)

    while (True):

        #Obtain data from USB port 
        data = get_data_port(usb_port)
  
        #This data is in variable Bytes
        print("Data in Bytes")
        print(data)

        #Convert a data in variable bytes to string
        data_string = data_to_string(data)
        print("Data in String")
        print(data_string)

            
                
    
   


