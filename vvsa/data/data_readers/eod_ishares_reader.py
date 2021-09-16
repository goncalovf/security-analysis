import pandas as pd

from vvsa.conf import settings


def read_product_eod_data(**kwargs):
    df = pd.read_csv(
        filepath_or_buffer=f"{settings.DATA_LOCATION}/eod_data/{kwargs['file_name']}",
        thousands=",",
        usecols=["As Of", "Fund Return Series"],
        index_col="As Of",
        parse_dates=True,
        infer_datetime_format=True,
        na_values="--",
    )

    df.index.rename("Date")
    df.sort_index(inplace=True)
    df.columns = ["Adj Close"]

    return df
