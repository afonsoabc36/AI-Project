"""
Como usar a classe:
bicycle = Vehicle("Bicycle", 5, 10)
motorcycle = Vehicle("Motorcycle", 20, 35)
car = Vehicle("Car", 100, 50)
"""


class Vehicle:

    def __init__(self, type, maxWeight, averageSpeed):
        self.type = type  # Tipo de veículo, "Bicycle", "Motorcycle", "Car"
        self.maxWeight = maxWeight  # Peso máximo que o veículo pode levar (Em kg)
        self.averageSpeed = averageSpeed  # Velocidade média do veículo

    # Velocidade do veículo ajustada ao peso das encomendas que leva
    def effectiveSpeed(self, packageWeight):
        effectiveSpeed = self.averageSpeed
        if self.type == "Bicycle":
            effectiveSpeed -= (packageWeight * 0.6)
        elif self.type == "Motorcycle":
            effectiveSpeed -= (packageWeight * 0.5)
        else:  # self.type == "Car"
            effectiveSpeed -= (packageWeight * 0.1)
        return effectiveSpeed

    # Verifica se um Veículo pode realizar a entrega
    def validateWeightCapacity(self, packageWeight):
        return packageWeight <= self.maxWeight
