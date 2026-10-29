# A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
#
# Write a solution to find the employees who are high earners in each of the departments.
#
# Return the result table in any order.


import pandas as pd


def top_three_salaries(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    employee["departmentId"] = employee["departmentId"].map(
        department.set_index("id")["name"]
    )

    employee["rank"] = employee.groupby("departmentId")["salary"].rank(
        method="dense", ascending=False
    )

    return employee[employee["rank"] <= 3][["departmentId", "name", "salary"]].rename(
        columns={"departmentId": "Department", "name": "Employee", "salary": "Salary"}
    )
