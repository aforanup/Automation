import json
import sys
import clipboard

SAVED_FIlE = "clipboard_data.json"


def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file)


def load_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        return data


print("Loading data")
print(sys.argv)


if len(sys.argv) == 2:
    function = sys.argv[1]
    data = load_data(SAVED_FIlE)

    if function == 'save':
        key = input("enter a key... ")
        data[key] = clipboard.paste()
        save_data(SAVED_FIlE, data)

    elif function == 'load':
        pass

    elif function == 'list':
        print('list')

    else:
        print('Function not supported.')
