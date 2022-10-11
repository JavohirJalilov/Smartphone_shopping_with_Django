import enum
from tinydb import TinyDB,Query 

db = TinyDB('data.json')


def getData(table_name):
    table = db.table(table_name)
    data = table.all()
    for i,d in enumerate(data):
        data[i] = dict(d)
    return data
