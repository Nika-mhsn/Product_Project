from Product_Project.mobile import Mobile


class Apple(Mobile):
    def __init__(self, name, price, vol, screen_size, country):
        super().__init__(name, price, vol, screen_size)
        self.country = country
