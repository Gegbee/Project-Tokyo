import serial, time

time.sleep(2)
arduino = serial.Serial("COM5", 9600)
print("Setup complete")
time.sleep(2)
arduino.write(("HI!").encode())
print("Finished")

while True:
    i = input("To Arduino: ")
    arduino.write(i.encode())