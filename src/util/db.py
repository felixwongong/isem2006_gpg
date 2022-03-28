from util import IOWrapper


def GetDataByID(id, filename):
    allData = IOWrapper.LoadFileJSON(f'/testdata/{filename}.json')
    for data in allData:

        if data['id'] == str(id):
            return data


def GetAllData(filename):
    return IOWrapper.LoadFileJSON(f'/testdata/{filename}.json')
