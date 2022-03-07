'''
ini perlu install module serial, untuk menjalankan script ini perlu tahu device name, contohnya
python3 check-modem.py /dev/ttyUSB3 , nanti outputnya akan muncul sim card id dan kekuatan sinyal

b'\r\n+CSQ: 23,99\r\n\r\nOK\r\n'
b'\r\n+CCID: 89883070000004646343\r\n\r\nOK\r\n'
sim number is 89883070000004646343 and modem signal is 23

'''

import time
import serial
import sys

def dataSignal(device):
    ser = serial.Serial(port=device,baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
    ser.isOpen()
    ser.write(b'AT+CSQ \r\n')
    time.sleep(1)
    out = b''
    while ser.inWaiting() > 0: 
        out += ser.read()
    time.sleep(1)
    print(out)
    signal = out.decode('utf-8').split('\n')[1]
    signal = signal.split(':')[1]
    signal = signal.strip()
    signal = int(signal.split(',')[0])

    ser.write(b'AT+CCID \r\n')
    time.sleep(1)
    out = b''
    while ser.inWaiting() > 0: 
        out += ser.read()
    time.sleep(1)
    print(out)
    ccid = out.decode('utf-8').split('\n')[1]
    ccid = ccid.split(':')[1]
    ccid = ccid.strip()
    print('sim number is ' + ccid + ' and modem signal is ' + str(signal))

dataSignal(sys.argv[1])

