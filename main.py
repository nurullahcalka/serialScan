import baseScanner
import time
while True:
    for port in baseScanner.COMPorts.get_com_ports().data:
        print("-------------------------------")
        print("Okuma Zamanı:",baseScanner.Time.time_now(self=0))
        print("Bağlantı Noktası:", port.device)
        print("Aygıt Adı:", port.description)
        print("Seri No:", port.serial_number)
        print("-------------------------------")
        time.sleep(2)
       # print(baseScanner.COMPorts.get_device_by_description(description="Arduino Leonardo"))


