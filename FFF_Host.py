import serial
import time
import requests

API_ENDPOINT = "(API Key)"
bluetoothSerial = serial.Serial("/dev/rfcomm0",baudrate=115200)
print("Bluetooth connected")
try:		
	while True:
		veri = bluetoothSerial.readline()
		print(veri)
		time.sleep(1)
		bluetoothSerial.write(veri)
		
		data = {'id':1,'token':'NST-02-01','data':veri} 
        
		r = requests.post(url = API_ENDPOINT,data=data)
        
except KeyboardInterrupt:
	port.close()
	print("Quit")
