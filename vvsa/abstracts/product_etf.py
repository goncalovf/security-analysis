from vvsa.abstracts.product import Product


class ETF(Product):
    def __init__(self, id, product_data, product_eod_data):
        super().__init__(id, product_data, product_eod_data)
        self.fund_family = product_data["fund_family"]
        self.related = product_data["related"]

    """
    Getters
    """

    def get_adj_close(self, **kwargs):
        return self.get_eod("Adj Close", **kwargs)
