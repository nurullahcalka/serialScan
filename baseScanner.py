import serial.tools.list_ports
import time

class COMPorts:
    def __init__(self, data: list):
        self.data = data

    @classmethod
    def get_com_ports(cls):
        data = []
        ports = list(serial.tools.list_ports.comports())

        for port_ in ports:
            obj = Object(data=dict({"device": port_.device, "serial_number": port_.serial_number,
                                    "description": port_.description.split("(")[0].strip()}))
            data.append(obj)
        return cls(data=data)

class Object:
    def __init__(self, data: dict):
        self.data = data
        self.device = data.get("device")
        self.description = data.get("description")
        self.serial_number = data.get("serial_number")

class Time:
    def time_now(self):
        t = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
        return current_time
