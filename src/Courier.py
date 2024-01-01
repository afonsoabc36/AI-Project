class Courier:

    def __init__(self, name, vehicle, number=-1, ratingValue=0, numberRatings=0, deliveries=None):
        self.number = number
        self.name = name
        self.free = True
        self.vehicle = vehicle
        self.ratingValue = ratingValue
        self.numberRatings = numberRatings
        self.deliveries = deliveries if deliveries is not None else []

    def __str__(self):
        return f"Courier {self.number}: {self.name}; Rating: {self.ratingValue}"

    def getNumber(self):
        return self.number

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def setFree(self):
        self.free = True

    def setBusy(self):
        self.free = False

    def getFree(self):
        return self.free

    def getRating(self):
        return self.ratingValue

    def getDeliveries(self):
        return self.deliveries

    # Substitui a lista de deliveries por uma lista nova
    def setDeliveries(self, deliveries):
        self.deliveries = deliveries

    def setVehicle(self, vehicle):
        self.vehicle = vehicle

    def getVehicle(self):
        return self.vehicle

    # Adiciona uma lista de deliveries à lista existente
    def addDeliveries(self, deliveries):
        self.deliveries.extend(deliveries)

    # Adiciona uma delivery à lista existente
    def addDelivery(self, delivery):
        self.deliveries.append(delivery)

    # Altera o rating do Courier quando recebe uma nova avaliação
    def updateRating(self, rating):
        self.ratingValue = (self.ratingValue * self.numberRatings + rating) / (self.numberRatings + 1)
        self.numberRatings += 1
