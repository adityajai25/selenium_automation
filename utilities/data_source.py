from utilities import read_utils

class DataSource:
    test_invalid_login = [
        ["john","john123","Invalid credentials"],
        ["steve","smith123","Invalid credentials"]
    ]
    test_invalid_login_csv = read_utils.get_csv_into_list("../test_data/test_invalid_login.csv")
    # test_invalid_login_excel = read_utils.get_excel_into_list("../test_data/orange-test-data.xlsx","test_invalid_login")
    test_invalid_login_excel = read_utils.get_excel_into_list("../test_data/orange-test-data.xlsx","test_invalid_login")