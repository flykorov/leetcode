# Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.
#
# Return the result table ordered by employee_id.

import pandas as pd


def find_employees(employees: pd.DataFrame) -> pd.DataFrame:

    return (
        employees[~employees["manager_id"].isin(employees["employee_id"])]
        .dropna()
        .query("salary < 30000")[["employee_id"]]
        .sort_values(by="employee_id")
    )
