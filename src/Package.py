
class Package:
    packageId = 0

    def __init__(self, id, weight, volume, deliveryDate, destination, price=0):
        global packageId
        self.id = id
        self.weight = weight
        self.volume = volume
        self.deliveryDate = deliveryDate
        self.price = price
        self.destination = destination

    def __str__(self):
        return f"Package {self.id}: {self.weight}kg; {self.volume}volume; Date: {self.deliveryDate}; Destination: {self.destination}"

    def getId(self):
        return self.id

    def setID(self, newId):
        self.id = newId

    @classmethod
    def getPackageId(cls):
        cls.packageId += 1
        return cls.packageId

    def setPackageId(self, newId):
        self.packageId = newId

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

    def getDestination(self):
        return self.destination

    def setDestination(self, destination):
        self.destination = destination
