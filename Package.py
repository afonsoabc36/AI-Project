class Package:

    def __init__(self, weight, length, width, height, deliveryDate, price, id = -1):
        self.id = id
        self.weight = weight
        # Não sei se tem de ser 3 atributos diferentes ou se dá para ser só volume
        self.length = length
        self.width = width
        self.height = height
        self.deliveryDate = deliveryDate
        self.price = price

    def getId(self):
        return self._id
    
    def setID(self, new_id):
        self._id = new_id

    def getWeight(self):
        return self._weight

    def setWeight(self, new_weight):
        self._weight = new_weight

    def getLength(self):
        return self._length

    def setLength(self, new_length):
        self._length = new_length

    def getWidth(self):
        return self._width

    def setWidth(self, new_width):
        self._width = new_width

    def getHeight(self):
        return self._height

    def setHeight(self, new_height):
        self._height = new_height

    def getDeliveryDate(self):
        return self._deliveryDate

    def setDeliveryDate(self, new_date):
        self._deliveryDate = new_date

    def getPrice(self):
        return self._price

    def setPrice(self, new_price):
        self._price = new_price

    def getPackageVolume(self):
        '''
        @return volume of a package, which is the product of length, width, and height.
        '''
        return self._length * self._width * self._height
