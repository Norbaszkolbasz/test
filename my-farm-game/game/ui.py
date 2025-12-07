def draw(grid):
    print("+" + "-" * grid.width + "+")
    for y in range(grid.height):
        row = ""
        for x in range(grid.width):
            c = grid.tiles[y][x]
            row += c.symbol if c is not None else '.'
        print("|" + row + "|")
    print("+" + "-" * grid.width + "+")


def help_text():
    return "Commands: p x y (plant), h x y (harvest), t (tick), q (quit), help"
