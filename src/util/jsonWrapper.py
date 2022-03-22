import json
import os


def LoadFile(filename):
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
