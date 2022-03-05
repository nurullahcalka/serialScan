import baseScanner #ilgili class import edildi
import json #JSON kütüphanesi eklendi

#Database işlemleri için veriler JSON dosyasına çevriliyor.
class DalJson:
    while True:
#while döngüsü ile portlar 2 saniyelik delay ile kayt işlemi yapılmaktadır.
        for port in baseScanner.COMPorts.get_com_ports().data:
            data_dict = {

                'Time': baseScanner.Time.time_now(self=0),
                "Port": port.device,
                'Name': port.description,
                'Seri No': port.serial_number,
            }
            print(data_dict)
            with open('data.json', 'a') as json_dosya: #json dosyayı yoksa oluşturulup ilgili kayıtları ekler
                json.dump(data_dict, json_dosya)
                json_dosya.write('\n')

            baseScanner.time.sleep(2)
