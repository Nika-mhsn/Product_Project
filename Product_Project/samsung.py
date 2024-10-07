from Product_Project.mobile import Mobile


class SamSung(Mobile):
    def __init__(self, name, price, vol, screen_size, foldable):
        super().__init__(name, price, vol, screen_size)
        self.foldable = foldable
