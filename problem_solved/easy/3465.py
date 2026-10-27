# Write a solution to find all products whose description contains a valid serial number pattern. A valid serial number follows these rules:
#
# It starts with the letters SN (case-sensitive).
# Followed by exactly 4 digits.
# It must have a hyphen (-) followed by exactly 4 digits.
# The serial number must be within the description (it may not necessarily start at the beginning).
# Return the result table ordered by product_id in ascending order.


import pandas as pd


def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:

    return products[
        products["description"].str.contains(r"(^|\W)SN\d{4}(?!\d)-\d{4}($|\W)")
    ].sort_values("product_id")

    # explication regex
    # W tout les non caractere (pas de lettre et chiffre)
    # (?<) verifier la lettre avant
    # (?) verifier la lettre apres
    # ! not
    # ^ debut de chaine
    # $ fin de chaine
