import serial.tools.list_ports #serial kütüphanesi eklendi
import time# zaman işlemleri için time kütüphanesi eklendi
# Ana Port Tarama Modülü
class COMPorts:
    def __init__(self, data: list):
        self.data = data

    @classmethod
    def get_com_ports(cls):  # portbilgileri
        data = []
        ports = list(serial.tools.list_ports.comports())

#for loop ile ihtiyacımız olan cihaz bilgilerinin getirilmesi sağlandı, sürekli bir işlem olduğundan  port ve cihaz değişimleri anlık yansımaktadır.
        for port_ in ports:
            obj = Object(data=dict({"device": port_.device, "serial_number": port_.serial_number,
                                    "description": port_.description.split("(")[0].strip()}))
            data.append(obj)
        return cls(data=data)

class Object:
    def __init__(self, data: dict): # ilgili objeler Public erişime açık hale getirildi
        self.data = data
        self.device = data.get("device")
        self.description = data.get("description")
        self.serial_number = data.get("serial_number")

class Time: # Zaman döngüsü öenmli olduğu için ilgili yerlerde kullanım için hazır.
    def time_now(self):
        t = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", t) #yıl-ay-gün-saat-dk-sn
        return current_time
