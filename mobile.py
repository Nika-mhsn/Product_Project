from Product_Project.electrical import Electrical


class Mobile(Electrical):
    def __init__(self, name, price, vol, screen_size):
        super().__init__(name, price, vol)
        self.screen_size = screen_size
