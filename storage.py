import json

FILE_NAME = "data.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_expense(expense):
    data = load_data()
    data.append(expense)
    save_data(data)