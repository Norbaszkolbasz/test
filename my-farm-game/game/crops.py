class Crop:
    def __init__(self, name, grow_time, symbol):
        self.name = name
        self.grow_time = grow_time
        self.symbol = symbol
        self.age = 0

    def is_mature(self):
        return self.age >= self.grow_time

    def grow(self):
        if not self.is_mature():
            self.age += 1

    def harvest_value(self):
        return 1 if self.is_mature() else 0


# Example crops
WHEAT = Crop("Wheat", grow_time=3, symbol='w')
CORN = Crop("Corn", grow_time=5, symbol='c')

def clone_crop(template):
    return Crop(template.name, template.grow_time, template.symbol)
