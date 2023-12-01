class Package:

    def __init__(self, weight, volume, deliveryDate, price, id=-1):
        self.id = id
        self.weight = weight
        self.volume = volume
        self.deliveryDate = deliveryDate
        self.price = price

    def getId(self):
        return self.id

    def setID(self, newId):
        self.id = newId

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def getVolume(self):
        return self.volume

    def setVolume(self, volume):
        self.volume = volume

    def getDeliveryDate(self):
        return self.deliveryDate

    def setDeliveryDate(self, newDate):
        self.deliveryDate = newDate

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice
