""" Write a function to load data. Parameter: file name, returns a list of users."""
def load_data(file_name):
    """
        Reads input file and returns the content
    """
    with open(file_name, encoding="utf-8") as file:
        data = file.readlines()
    file.close()
    return data


def login(data):
    """
        Compares user input to argument and assigns matching data to a dictionary
    """
    name_input = input("Enter Name: ")
    password_input = input("Enter Password: ")
    existing_user = 0

    for current_user in data:
        current_user = current_user.strip().split(",")
        name = current_user[0]
        password = current_user[1]
        full_name = current_user[2]
        balance = current_user[3]
        if name_input == name and password_input == password:
            existing_user = {"Full Name": full_name, "Balance": balance}

    return existing_user



def display_user_info(value):
    """
        Checks input for dictionary data and outputs a warning message or the contents of the dictionary
    """
    if value == 0:
        print("Unable to validate credentials")
    else:
        print(f'Name: {value["Full Name"]}\nBalance: {value["Balance"]}')

user_data = load_data("data.txt")
user_dict = login(user_data)
display_user_info(user_dict)
