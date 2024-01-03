
class Package:
    packageId = 0

    def __init__(self, id, weight, volume, deliveryDate, destination, price=0, courier=-1, rating = -1):
        global packageId
        self.id = id
        self.weight = weight
        self.volume = volume
        self.deliveryDate = deliveryDate
        self.price = price
        self.destination = destination
        self.courier = courier
        self.rating = rating
        # self.dayDifference = Float que diz quantos dias faltam até à data de entrega

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

    def setPrice(self, distance, vehicle):
        cost = 0  # TODO

        self.price = cost

    def getDestination(self):
        return self.destination

    def setDestination(self, destination):
        self.destination = destination

    def getCourier(self):
        return self.courier

    def setCourier(self, courier):
        self.courier = courier

    def notReviewed(self):
        return self.rating == -1

    def getRating(self):
        return self.rating

    def setRating(self, rating):
        self.rating = rating
