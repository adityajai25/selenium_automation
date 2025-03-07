import pandas

def get_csv_into_list(csv_file):
    data = pandas.read_csv(csv_file,delimiter=";")
    return data.values

def get_excel_into_list(excel_file,sheet_name):
    df = pandas.read_excel(io=excel_file,sheet_name=sheet_name)
    return df.values