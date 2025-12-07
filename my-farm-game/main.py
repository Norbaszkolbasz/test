from game.grid import Grid
from game.crops import clone_crop, WHEAT, CORN
from game.ui import draw, help_text


def main():
    grid = Grid(width=6, height=4)
    # simple state
    coins = 5
    seed_templates = {'wheat_seed': WHEAT, 'corn_seed': CORN}

    print('Welcome to My Farm (minimal)')
    print(help_text())

    while True:
        draw(grid)
        cmd = input('> ').strip().lower()
        if not cmd:
            continue
        parts = cmd.split()
        if parts[0] == 'q':
            print('Bye')
            break
        if parts[0] == 'help':
            print(help_text())
            continue
        if parts[0] == 'p' and len(parts) == 4:
            try:
                seed = parts[1]
                x = int(parts[2]); y = int(parts[3])
                if seed not in seed_templates:
                    print('Unknown seed. Use wheat_seed or corn_seed')
                    continue
                crop = clone_crop(seed_templates[seed])
                grid.plant(x, y, crop)
                print(f'Planted {crop.name} at {x},{y}')
            except Exception as e:
                print('Error planting:', e)
            continue
        if parts[0] == 'h' and len(parts) == 3:
            try:
                x = int(parts[1]); y = int(parts[2])
                crop = grid.harvest(x, y)
                if crop is None:
                    print('Nothing to harvest')
                else:
                    gained = crop.harvest_value()
                    coins += gained
                    print(f'Harvested {crop.name}, gained {gained} coins')
            except Exception as e:
                print('Error harvesting:', e)
            continue
        if parts[0] == 't':
            grid.tick()
            print('Time advanced')
            continue
        print('Unknown command. Type help')


if __name__ == '__main__':
    main()
