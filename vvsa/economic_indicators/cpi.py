from vvsa.abstracts.economic_indicator import Economic_Indicator
from vvsa.data.data_reader import get_cpi_data


class CPI(Economic_Indicator):
    def __init__(self):
        super().__init__("CPI")
        self.data = get_cpi_data()