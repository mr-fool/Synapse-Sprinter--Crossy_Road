import serial
import time

arduino_port = 'COM3'
baud_rate = 115200

ser = serial.Serial(arduino_port, baud_rate, timeout=1)
def getdata():
    try:
        ser_out = ser.readline().decode().strip().split(',')
        if not len(ser_out) == 2:
            return
        return ser_out
    except:
        return