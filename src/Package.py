class Package:

    def __init__(self, weight, volume, deliveryDate, price, id=-1):
        self.id = id
        self.weight = weight
        # Não sei se tem de ser 3 atributos diferentes ou se dá para ser só volume
        self.volume = volume
        self.deliveryDate = deliveryDate
        self.price = price

    def getId(self):
        return self._id
    
    def setID(self, newId):
        self.id = newId

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
