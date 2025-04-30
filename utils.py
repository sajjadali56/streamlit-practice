import pandas as pd

excel = pd.ExcelFile("./budget.xlsx")


def get_data(sheet_name: str):
    data = pd.read_excel(excel, sheet_name=sheet_name)
    data.dropna(inplace=True)
    data.fillna(0, inplace=True)
    return data
