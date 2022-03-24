from util import IOWrapper


def GetDataByID(id, filename):
    allData = IOWrapper.LoadFileJSON(f'/testdata/{filename}.json')
    for data in allData:

        if data['id'] == str(id):
            return data


def GetObjectByID(id, filename, type):
    data = GetDataByID(id, filename)
    return type(**data)


def GetAllData(filename):
    return IOWrapper.LoadFileJSON(f'/testdata/{filename}.json')
