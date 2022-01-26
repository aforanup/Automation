import json
import sys
import clipboard

SAVED_FIlE = "clipboard_data.json"


def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file)


def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    function = sys.argv[1]
    data = load_data(SAVED_FIlE)

    if function == 'save':
        key = input("enter a key... ")
        data[key] = clipboard.paste()
        save_data(SAVED_FIlE, data)
        print("Done saving!")

    elif function == 'load':
        key = input("enter a key... ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard!")
        else:
            print("no such key found!")

    elif function == 'list':
        print(data)

    else:
        print('Function not supported.')
