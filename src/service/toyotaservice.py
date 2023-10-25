from controller.autocontroller import CarHandler

class Toyotaservice(CarHandler):
    def handle_request(self, car):
        if car.lower() == "toyota":
            print("Manejando solicitud de Toyota")
        elif self.next_handler:
            self.next_handler.handle_request(car)
        else:
            print("Solicitud no manejada.")
