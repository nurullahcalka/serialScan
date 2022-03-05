import serial.tools.list_ports

connected = []
while True:
    comlist = serial.tools.list_ports.comports()
    for element in comlist:
        connected.append(element.device)

    print("Bağlı COM portları: " + str(connected))
    connected.clear()