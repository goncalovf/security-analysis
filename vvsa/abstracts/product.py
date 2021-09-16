from abc import ABC

from vvsa.products.inc.eod_series import EOD_Series


class Product(ABC):
    def __init__(self, id, product_data, product_eod_data):
        self.id = id
        self.name = product_data["name"]
        self.type = product_data["type"]
        self.asset_class = product_data["asset_class"]
        self.product_page = product_data["product_page"]
        self.eod_data = product_eod_data

    def get_eod(self, series, **kwargs):

        series_list = self.eod_data[series]

        if "source" in kwargs:
            eod_s = [
                eod_s for eod_s in series_list if eod_s.source == kwargs["source"]
            ][0]
            del kwargs["source"]
        else:
            eod_s = series_list[0]

        return EOD_Series(eod_s.name, eod_s.series, eod_s.source, **kwargs)
