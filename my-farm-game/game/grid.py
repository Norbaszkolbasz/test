class Grid:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        # None = empty, otherwise store Crop instance
        self.tiles = [[None for _ in range(width)] for _ in range(height)]

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def plant(self, x, y, crop):
        if not self.in_bounds(x, y):
            raise IndexError("Out of bounds")
        if self.tiles[y][x] is not None:
            raise ValueError("Tile already has a crop")
        self.tiles[y][x] = crop

    def harvest(self, x, y):
        if not self.in_bounds(x, y):
            raise IndexError("Out of bounds")
        crop = self.tiles[y][x]
        self.tiles[y][x] = None
        return crop

    def tick(self):
        # advance growth for every planted crop
        for y in range(self.height):
            for x in range(self.width):
                crop = self.tiles[y][x]
                if crop is not None:
                    crop.grow()
