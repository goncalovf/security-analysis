product_data = {
    "SDWD": {
        "name": "iShares MSCI World ESG Screened UCITS ETF",
        "type": "ETF",
        "asset_class": "Equity",
        "fund_family": "iShares",
        "product_page": "https://www.ishares.com/uk/individual/en/products/305418/ishares-msci-world-esg-screened-ucits-etf",
        "eod_data_files": [
            {"file_name": "SDWD.L.csv", "source": "yahoo"},
            {"file_name": "SDWD_iShares.csv", "source": "iShares"},
        ],
        "related": {"SAWD"},
    },
    "SAWD": {
        "name": "iShares MSCI World ESG Screened UCITS ETF",
        "type": "ETF",
        "asset_class": "Equity",
        "fund_family": "iShares",
        "product_page": "https://www.ishares.com/uk/individual/en/products/305419/ishares-msci-world-esg-screened-ucits-etf",
        "eod_data_files": [{"file_name": "SAWD.L.csv", "source": "yahoo"}],
        "related": {"SDWD"},
    },
    "MSCIW": {
        "name": "MSCI World Index",
        "type": "Index",
        "asset_class": "Equity",
        "index_family": "MSCI",
        "product_page": "https://www.msci.com/developed-markets",
        "eod_data_files": [
            {"file_name": "MSCIW.csv", "source": "msci", "series_name": "Price"},
            {"file_name": "MSCIW_net.csv", "source": "msci", "series_name": "Net"},
        ],
    },
    "MSCIWES": {
        "name": "MSCI World ESG Screened Index",
        "type": "Index",
        "asset_class": "Equity",
        "index_family": "MSCI",
        "product_page": "https://www.msci.com/esg-screened-indexes",
        "eod_data_files": [
            {"file_name": "MSCIWES.csv", "source": "msci", "series_name": "Price"},
            {"file_name": "MSCIWES_net.csv", "source": "msci", "series_name": "Net"},
        ],
        "parent": "MSCIW",
    },
}
