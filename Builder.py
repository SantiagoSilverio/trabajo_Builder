class Auto:
    def __init__(self, puertas, color, marca):
        self.puertas = puertas
        self.color = color
        self.marca = marca

class autobuilder:

    def with_puertas(self, puertas):
        self.puertas = puertas
        return self

    def with_color(self, color):
        self.color = color
        return self

    def with_marca(self, marca):
        self.marca = marca
        return self

    def build(self):
        return Auto(self.puertas, self.color, self.marca)


auto1 = autobuilder().with_puertas("2").with_color("azul").with_marca("peugeot")


print(f"Auto: puertas={auto1.puertas}, color={auto1.color}, marca={auto1.marca}")
