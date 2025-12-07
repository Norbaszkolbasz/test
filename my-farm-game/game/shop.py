class Shop:
    def __init__(self):
        # prices are arbitrary
        self.catalog = {
            'wheat_seed': {'crop_template': None, 'price': 1},
            'corn_seed': {'crop_template': None, 'price': 2},
        }

    def set_templates(self, templates):
        # templates is dict like {'wheat_seed': CropTemplate}
        for key in templates:
            if key in self.catalog:
                self.catalog[key]['crop_template'] = templates[key]

    def list_items(self):
        return [(k, v['price']) for k, v in self.catalog.items()]

    def buy(self, key, coins):
        if key not in self.catalog:
            raise KeyError('No such item')
        price = self.catalog[key]['price']
        if coins < price:
            raise ValueError('Not enough coins')
        return price, self.catalog[key]['crop_template']
