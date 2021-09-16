from vvsa.abstracts.product import Product


class Index(Product):
    def __init__(self, id, product_data, product_eod_data):
        super().__init__(id, product_data, product_eod_data)
        self.index_family = product_data["index_family"]

    """
    Getters
    """

    def get_net(self, **kwargs):
        return self.get_eod("Net", **kwargs)
