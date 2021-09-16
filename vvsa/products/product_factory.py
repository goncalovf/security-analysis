from vvsa.data import product_data
from vvsa.data.data_reader import get_product_eod_data
from vvsa.products import types

from vvsa.utils.errors import print_error

product_classes = {
    "Equity_ETF": types.Equity_ETF,
    "Equity_Index": types.Equity_Index,
}


def get_product(product_id):
    """Initiate the product class that corresponds to the product type (and asset class).

    Args
    ----
    product_id: str
        The product's identifier in the product_data dict. Typically the product ticker, if it has one.

    Return
    ------
    Product: obj
        An initiated instance of the product class corresponding to the product type (and asset class)
    """
    product_data = get_product_data(product_id)
    product_eod_data = get_product_eod_data(product_data["eod_data_files"])

    product_classname = get_product_classname(product_data)

    return product_classes[product_classname](
        product_id, product_data, product_eod_data
    )


def get_product_data(product_id):
    """Read the product's data from the CSV file.

    Args
    ----
    product_id: str
        The product's identifier in the product_data dict. Typically the product ticker, if it has one.

    Raises
    ------
    KeyError
        If couldn't find a product in the product_data dict with the passed product_id.

    Returns
    ------
    product_data: dict
        The product's data in the product_data dict.
    """
    try:
        return product_data[product_id]
    except KeyError:
        print_error(
            f"Was unable to find data on {product_id} in the 'products' csv file. Did you type the product ID correctly?"
        )
        raise


def get_product_classname(product_data):
    """Get the name of the produt's object class based on the its type and asset class

    Args
    ----
    product_data: dict
        The product's data in the product_data dict, containing the product's type and possibly its asset class

    Return
    ------
    classname: str
        The name of the product's object class
    """
    product_type = product_data["type"]
    product_asset_class = product_data["asset_class"]

    if product_type == "ETF" and product_asset_class == "Equity":
        return "Equity_ETF"
    elif product_type == "ETF" and product_asset_class == "Fixed Income":
        return "Fixed_Income_ETF"
    elif product_type == "Index" and product_asset_class == "Equity":
        return "Equity_Index"
