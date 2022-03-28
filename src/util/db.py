from util import IOWrapper


def GetDataByID(id, filename):
    """Get data by object id stored in <__dirname__>/db/<__filename__>.json

    Args:
        id (string): item id in db
        filename (string): JSON filename in db directory

    Returns:
        dict: dictionary of data read from JSON file
    """
    allData = IOWrapper.LoadFileJSON(f'/db/{filename}.json')
    for data in allData:

        if data['id'] == str(id):
            return data


def GetAllData(filename):
    """Get all data stored in <__dirname__>/db/<__filename__>.json

    Args:
        filename (string): JSON filename in db directory

    Returns:
        list<dict>: all data read from JSON file
    """

    return IOWrapper.LoadFileJSON(f'/db/{filename}.json')
