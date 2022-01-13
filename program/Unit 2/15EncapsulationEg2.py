class Product:
    def __init__(self):
      self.__maxprice = 1000
      self.__minprice = 1

    def sellingPrice(self):
        print('Our product maximum price is: {}'.format(self.__maxprice))
        print('Our product minimum price is: {}'.format(self.__minprice))

    def productMaxPrice(self, price):
        self.__maxprice = price
    def productMinPrice(self, price):
        self.__minprice = price

prod1= Product()
prod1.sellingPrice()

prod1.__maxprice = 1500
prod1.sellingPrice()

prod1.__minprice = 10
prod1.sellingPrice()

prod1.productMaxPrice(1500)
prod1.sellingPrice()

prod1.productMinPrice(10)
prod1.sellingPrice()
