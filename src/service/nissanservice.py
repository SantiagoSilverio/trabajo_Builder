from controller.autocontroller import CarHandler

class Nissanservice(CarHandler):
    def handle_request(self, car):
        if car.lower() == "nissan":
            print("Manejando solicitud de nissan")
        elif self.next_handler:
            self.next_handler.handle_request(car)
        else:
            print("Solicitud no manejada.")