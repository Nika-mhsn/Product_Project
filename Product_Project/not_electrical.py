from Product_Project.product import Product


class NotElectrical(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
