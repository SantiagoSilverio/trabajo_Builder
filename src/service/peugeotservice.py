from controller.autocontroller import CarHandler

class Peugeotservice(CarHandler):
    def handle_request(self, car):
        if car.lower() == "peugeot":
            print("Manejando solicitud de Peugeot")
        elif self.next_handler:
            self.next_handler.handle_request(car)
        else:
            print("Solicitud no manejada.")
