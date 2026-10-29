# Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:
#
# "Low Salary": All the salaries strictly less than $20000.
# "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories. If there are no accounts in a category, return 0.
#
# Return the result table in any order.

import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    data = [
        ["Low Salary", len(accounts[accounts["income"] < 20000]["income"])],
        [
            "Average Salary",
            len(
                accounts[(accounts["income"] >= 20000) & (accounts["income"] <= 50000)][
                    "income"
                ]
            ),
        ],
        ["High Salary", len(accounts[accounts["income"] > 50000]["income"])],
    ]

    return pd.DataFrame(data, columns=["category", "accounts_count"]).astype(
        {"category": "object", "accounts_count": "Int64"}
    )
