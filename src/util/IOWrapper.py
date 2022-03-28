import json
import os


def LoadFileJSON(filename):
    """Load JSON file with path start from root directory

    Args:
        filename (string): file path in program directory, e.g. /db/items.json

    Returns:
        list<...dict>: list(s) of dict of file content
    """
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
    """Write JSON file with path start from root directory

    Args:
        filename (string): file path in program directory, e.g. /db/items.json
    """

    realFilePath = f'/../../{filename}'
    dir = os.path.dirname(__file__) + realFilePath

    json_obj = json.dumps(data, indent=4)
    with open(dir, 'w+') as outfile:
        print(f'\nWriting JSON data to {filename}\n')
        outfile.write(json_obj)


def WriteFile(filename, data):
    """Write file with path start from root directory

    Args:
        filename (string): file path in program directory, e.g. /output/output.txt
    """

    realFilePath = f'/../../{filename}'
    dir = os.path.dirname(__file__) + realFilePath

    with open(dir, 'w+') as outfile:
        print(f'\nWriting data to {filename}\n')
        outfile.write(data)


def ReadFile(filename):
    """Load file with path start from root directory

    Args:
        filename (string): file path in program directory, e.g. /db/items.txt

    Returns:
        string: file content
    """

    realFilePath = f'/../../{filename}'
    dir = os.path.dirname(__file__) + realFilePath

    with open(dir) as infile:
        try:
            return infile.read()
        except:
            print("error in file reading")
            return None
