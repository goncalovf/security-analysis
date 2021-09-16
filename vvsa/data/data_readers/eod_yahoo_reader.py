import pandas as pd

from vvsa.conf import settings


def read_product_eod_data(**kwargs):
    return pd.read_csv(
        filepath_or_buffer=f"{settings.DATA_LOCATION}/eod_data/{kwargs['file_name']}",
        thousands=",",
        index_col="Date",
        parse_dates=True,
        infer_datetime_format=True,
    )
