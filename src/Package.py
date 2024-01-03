from Vehicle import Vehicle
from datetime import datetime, timedelta

class Package:
    packageId = 0

    def __init__(self, id, weight, volume, deliveryDate, destination, time ,price=0, courier=-1, rating = -1):
        global packageId
        self.id = id
        self.weight = weight
        self.volume = volume
        self.deliveryDate = deliveryDate
        self.price = price
        self.destination = destination
        self.courier = courier
        self.rating = rating
        delivery_datetime = datetime.strptime(deliveryDate, "%d/%m/%YT%H:%M")
        time_datetime = datetime.strptime(time, "%d/%m/%YT%H:%M")

        # Calculate the day difference
        self.dayDifference = (time_datetime - delivery_datetime).days

    def __str__(self):
        return f"Package {self.id}: {self.weight}kg; {self.volume}volume; Date: {self.deliveryDate}; Destination: {self.destination}; Price: {self.price}€"

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

    def setPrice(self, distance, vehicle):  # 'Bicycle', 'Motorcycle', 'Car'
        pricePerKm = Vehicle(vehicle).getPriceToCostumer()
        total_price = 3 + (distance * pricePerKm)  # TODO
        if self.dayDifference < 1:
            total_price += 1.5
        elif self.dayDifference < 2:
            total_price += 1
        else:
            total_price += 0.5

        self.price = total_price

    def arriveOnTime(self, duration, time):
        delivery_datetime = datetime.strptime(self.deliveryDate, "%d/%m/%YT%H:%M")
        time_datetime = datetime.strptime(time, "%d/%m/%YT%H:%M")

        expected_delivery_time = time_datetime + timedelta(minutes=duration)

        return expected_delivery_time <= delivery_datetime

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
