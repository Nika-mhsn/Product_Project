from Product_Project.product import Product


class Electrical(Product):
    def __init__(self, name, price, vol):
        super().__init__(name, price)
        self.vol = vol
