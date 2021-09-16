import pandas as pd

from vvsa.conf import settings


def read_product_eod_data(**kwargs):
    series_name = kwargs["series_name"] if "series_name" in kwargs else "Value"

    return pd.read_csv(
        filepath_or_buffer=f"{settings.DATA_LOCATION}/eod_data/{kwargs['file_name']}",
        header=0,
        names=["Date", series_name],
        thousands=",",
        index_col="Date",
        parse_dates=True,
        infer_datetime_format=True,
    )
