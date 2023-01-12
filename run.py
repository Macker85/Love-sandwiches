import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('cred.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Copy of love_sandwiches')


def get_sales_data():
    """
    Get sales figures from user.
    run a loop to ensure data is valid
    must be 6 entries seperated by commas
    The loop will repeat until valid
    """
    while True:
        print("enter dales data")
        print("data should be 6 numners, seperated by commas")
        print("example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
    
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid")
            break

    return sales_data


def validate_data(values):
    """
    inside the try, vonverts all string values to integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't 6 numbers
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"invalid data : {e}")
        return False

    return True


def update_sales_worksheet(data):
    """
    update worksheet
    """
    print("updating sales worksheet....")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("updated successsfully.\n")


def calculate_surplus_data(sales_row):
    """
    Compare stock and calculate surplus
    """
    print("calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(stock_row)



def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)


print("Welcome to love sandwiches")
main()