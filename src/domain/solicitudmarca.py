from service.toyotaservice import Toyotaservice
from service.peugeotservice import Peugeotservice
from service.nissanservice import Nissanservice
from controller.autocontroller import CarHandler

class solicitud():
    def main():
        marca = input("Por favor, ingrese la marca del automóvil que desea (nissan/toyota/peugeot): ").lower()

        toyota_service = Toyotaservice()
        peugeot_service = Peugeotservice()
        nissan_service = Nissanservice()

        car_handler = CarHandler(toyota_service)  
        toyota_service.set_next_handler(peugeot_service)
        peugeot_service.set_next_handler(nissan_service)   

        car_handler.handle_request(marca)