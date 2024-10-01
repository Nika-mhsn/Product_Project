from Product_Project.electrical import Electrical


class LapTop(Electrical):
    def __init__(self, name, price, vol, cpu, ram):
        super().__init__(name, price, vol)
        self.cpu = cpu
        self.ram = ram
