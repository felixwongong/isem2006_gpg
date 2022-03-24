import json
import os


def LoadFileJSON(filename):
    realFilePath = f'/../../{filename}'
    dir = os.path.dirname(__file__) + realFilePath
    try:
        file = open(dir)
        data = json.load(file)
        file.close()
    except FileNotFoundError:
        print(f"File with path ({dir}) not found")
        return None
    return data


def WriteFileJSON(filename, data):
    realFilePath = f'/../../{filename}'
    dir = os.path.dirname(__file__) + realFilePath

    json_obj = json.dumps(data, indent=4)
    with open(dir, 'w+') as outfile:
        print(f'\nWriting JSON data to {filename}\n')
        outfile.write(json_obj)


def WriteFile(filename, data):
    realFilePath = f'/../../{filename}'
    dir = os.path.dirname(__file__) + realFilePath

    with open(dir, 'w+') as outfile:
        print(f'\nWriting data to {filename}\n')
        outfile.write(data)


def ReadFile(filename):
    realFilePath = f'/../../{filename}'
    dir = os.path.dirname(__file__) + realFilePath

    with open(dir) as infile:
        try:
            return infile.read()
        except:
            print("error in file reading")
            return None
