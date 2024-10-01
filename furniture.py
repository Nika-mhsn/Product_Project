from Product_Project.not_electrical import NotElectrical


class Furniture(NotElectrical):
    def __init__(self, name, price, weight, capacity):
        super().__init__(name, price, weight)
        self.capacity = capacity
