import pandas as pd

from collections import defaultdict

from vvsa.conf import settings
from vvsa.data.data_readers import *
from vvsa.products.inc.eod_series import EOD_Series
from vvsa.economic_indicators.inc.series import EI_Series

eod_data_readers = {
    "yahoo": eod_yahoo_reader,
    "msci": eod_msci_reader,
    "iShares": eod_ishares_reader,
}


def get_product_eod_data(eod_data_files):
    eod_series = defaultdict(list)
    for file_info in eod_data_files:

        df = eod_data_readers[file_info["source"]].read_product_eod_data(**file_info)

        for series_name, series in df.iteritems():
            eod_series[series_name].append(
                EOD_Series(series_name, series, file_info["source"])
            )

    return eod_series


def get_cpi_data():
    # TODO: because the time series only has the year, read_csv parses the date column to the first day of each year. So if the time series has as rows the years 1971 and 1972, they will be parsed as 1971-01-01 and 1972-01-01

    # Read the column names so that I can exclude the "Series Name" column.
    cols = list(pd.read_csv(f"{settings.DATA_LOCATION}/economic_data/CPI.csv", nrows=1))

    df = pd.read_csv(
        filepath_or_buffer=f"{settings.DATA_LOCATION}/economic_data/CPI.csv",
        thousands=",",
        usecols=[c for c in cols if c != "Series Name"],
        index_col="Time",
        parse_dates=True,
        infer_datetime_format=True,
    )

    cpi_series = {}
    for country, series in df.iteritems():
        cpi_series[country] = EI_Series(country, series)

    return cpi_series
