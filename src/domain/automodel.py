from service.toyotaservice import Toyotaservice

class AutoModel:
    def __init__(self):
        self.dispenser = Toyotaservice()

    def dispense_amount(self, car):
        self.dispenser.dispense(car)