class laptop :
    chargertype = "C-TYPE"

    def __init__(self):
        self.brand = ''
        self.price = 34

    def setPrice(self,price):
        self.price = price

    def getPrice(self):
        print("Price :", self.price)
        print("Charger Type :", self.chargertype)
        
    @classmethod
    def changeChargerType(cls):
        cls.chargertype = "B-TYPE"

    @staticmethod
    def info():
        print("This is laptop class")

hp = laptop()
hp.setPrice("$239")
laptop.changeChargerType()
hp.getPrice()
hp.info()

