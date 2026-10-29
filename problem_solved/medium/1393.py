# Write a solution to report the Capital gain/loss for each stock.
#
# The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.
#
# Return the result table in any order.


import pandas as pd


def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:

    stocks.loc[stocks["operation"] == "Buy", "price"] *= -1
    return (
        stocks.groupby("stock_name")["price"]
        .sum()
        .reset_index()
        .rename(columns={"price": "capital_gain_loss"})
    )
