class Courier:

    def __init__(self, id = -1, rating = 0, deliveries = []):
        self.id = id
        self.rating = rating
        self.deliveries = deliveries

    def getId(self):
        return self.id
    
    def getRating(self):
        return self.rating
    
    def getDeliveries(self):
        return self.deliveries
    
    # Substitui a lista de deliveries por uma lista nova
    def setDeliveries(self, deliveries):
        self.deliveries = deliveries

    # Adiciona uma lista de deliveries à lista existente
    def addDeliveries(self, deliveries):
        self.deliveries.extend(deliveries)

    # Adiciona uma delivery à lista existente
    def addDelivery(self, delivery):
        self.deliveries.append(delivery)