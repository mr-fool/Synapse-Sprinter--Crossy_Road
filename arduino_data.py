import serial
import time

arduino_port = 'COM3'
baud_rate = 115200

ser = serial.Serial(arduino_port, baud_rate, timeout=1)
def getdata():
    received = False
    while not received:
        try:
            ser_out = ser.readline().decode().strip().split(',')
            if not len(ser_out) == 2:
                pass
            else:
                received = True
                ser_out = [float(i) for i in ser_out]
        except:
            pass