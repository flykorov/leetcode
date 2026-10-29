# Find the names ofr:
#
# referred by any customer with id != 2.
# not referred by any customer.
# Return the result table in any order.


import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:

    customer = customer.fillna(0)
    return customer[customer["referee_id"] != 2][["name"]]
