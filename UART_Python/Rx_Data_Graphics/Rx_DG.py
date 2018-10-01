# -*- coding: utf-8 -*-

# This example take data from temperature and pressure sensor and plot them

import serial 
import numpy  
import matplotlib.pyplot as plt 
from drawnow import *

temperature = []      # List that contains the temperature         
pressure = []         # List that contains the pressure 

com_arduino = serial.Serial('/dev/ttyUSB0', 9600) # Open USB port

plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

def makeFig(): #Create a function that makes our desired plot
    plt.ylim(20,35)                                 #Set y min and max values
    plt.title('Sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Temperature C')                            #Set ylabels
    plt.plot(temperature, 'ro-', label='Degrees C')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    plt2=plt.twinx()                                #Create a second y axis
    plt.ylim(101000,101070)                           #Set limits of second y axis- adjust to readings you are getting
    plt2.plot(pressure, 'b^-', label='Pressure (Pa)') #plot pressure data
    plt2.set_ylabel('Pressrue (Pa)')                    #label second y axis
    plt2.ticklabel_format()           #Force matplotlib to NOT autoscale y axis
    plt2.legend(loc='upper right')                  #plot the legend
    

while True: 
    while (com_arduino.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    arduinoString = com_arduino.readline() #read the line of text from the serial port
    dataArray = arduinoString.split(',')   #Split it into an array called dataArray
    print(dataArray)
    temp = float(dataArray[0])            #Convert first element to floating number and put in temp
    P =    float(dataArray[1])            #Convert second element to floating number and put in P
    temperature.append(temp)               #Build our tempF array by appending temp readings
    pressure.append(P)                     #Building our pressure array by appending P readings
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        temperature.pop(0)                       #This allows us to just see the last 50 data points
        pressure.pop(0)

