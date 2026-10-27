# Write a solution to find for each user, the join date and the number of orders they made as a buyer in 2019.
#
# Return the result table in any order.


import pandas as pd


def market_analysis(
    users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame
) -> pd.DataFrame:

    return (
        users.merge(
            orders[orders["order_date"] >= "2019-01-01"].value_counts("buyer_id"),
            left_on="user_id",
            right_on="buyer_id",
            how="left",
        )
        .drop(columns="favorite_brand")
        .fillna(0)
        .rename(columns={"user_id": "buyer_id", "count": "orders_in_2019"})
    )
