class AutoModel:
    def __init__(self, marca, color, puertas):
        self.marca = marca
        self.color = color
        self.puertas = puertas


    def __str__(self):
        return f"auto: {self.marca} {self.color}, puertas: {self.puertas}"
