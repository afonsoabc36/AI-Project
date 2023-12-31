"""
Como usar a classe:
bicycle = Vehicle("Bicycle")
motorcycle = Vehicle("Motorcycle")
car = Vehicle("Car")
"""


class Vehicle:

    def __init__(self, vehicleType):
        self.vehicleType = vehicleType  # Tipo de veículo, "Bicycle", "Motorcycle", "Car"
        self.totalMaxWeight = 0
        if self.vehicleType == "Bicycle":
            self.maxWeight = 5
            self.averageSpeed = 10
            self.costPerKm = 0
            self.carbonEmissionPerMin = 0.013  # Emitido pelo entregador pelo esforço extra
            self.pricePerKmToCustomer = 0.07
        elif self.vehicleType == "Motorcycle":
            self.maxWeight = 20
            self.averageSpeed = 35
            self.costPerKm = 2.5 * 1.6 / 100
            self.carbonEmissionPerMin = 0.077
            self.pricePerKmToCustomer = 0.15
        else:  # self.vehicleType == "Car"
            self.maxWeight = 100
            self.averageSpeed = 50
            self.costPerKm = 5.6 * 1.6 / 100
            self.carbonEmissionPerMin = 0.1546
            self.pricePerKmToCustomer = 0.25
        if self.maxWeight > self.totalMaxWeight:
            self.totalMaxWeight = self.maxWeight

    # Velocidade do veículo ajustada ao peso das encomendas que leva
    def effectiveSpeed(self, packageWeight):
        effectiveSpeed = self.averageSpeed
        if self.vehicleType == "Bicycle":
            effectiveSpeed -= (packageWeight * 0.6)
        elif self.vehicleType == "Motorcycle":
            effectiveSpeed -= (packageWeight * 0.5)
        else:  # self.type == "Car"
            effectiveSpeed -= (packageWeight * 0.1)
        return effectiveSpeed

    # Verifica se um Veículo pode realizar a entrega
    def validateWeightCapacity(self, packageWeight):
        return packageWeight <= self.maxWeight

    # Calcula o custo monetário para o negócio de cada entrega
    def getTripCost(self, distance, timeSpent, wagePerHour):
        return distance * self.costPerKm + timeSpent * wagePerHour

    def getTotalMaxWeight(self):
        return self.totalMaxWeight

    def getVehicleType(self):
        return self.vehicleType

    def getCarbonEmission(self):
        return self.carbonEmissionPerMin

    def canDeliver(self, packageWeight):
        if packageWeight <= self.maxWeight:
            return True
        else:
            return False

    def getPriceToCostumer(self):
        return self.pricePerKmToCustomer
