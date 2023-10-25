from service.toyotaservice import Toyotaservice
from service.peugeotservice import Peugeotservice
from service.nissanservice import Nissanservice
from domain.autobuilder import AutoBuilder
from controller.autocontroller import CarHandler

def main():
    auto = AutoBuilder().with_marca("peugeot").with_color("negro").with_puertas("2").build()
    auto2 = AutoBuilder().with_marca("toyota").with_color("rojo").with_puertas("4").build()
    print(auto,)

if __name__ == "__main__":
    main()
    

def main():
    marca = input("Por favor, ingrese la marca del automóvil que desea: ").lower()

    toyota_service = Toyotaservice()
    peugeot_service = Peugeotservice()
    nissan_service = Nissanservice()

    car_handler = CarHandler(toyota_service)  
    toyota_service.set_next_handler(peugeot_service)
    peugeot_service.set_next_handler(nissan_service)   


    car_handler.handle_request(marca)

if __name__ == "__main__":
    main()