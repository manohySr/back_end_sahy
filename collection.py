import json
import numpy as np
from recognition.face import make_collection

collection1 = make_collection('./recognition/unknown/Danielyh.jpg')
collection2 = make_collection('./recognition/unknown/Manohy.jpg')


def save_image_known_in_database(collection):
    with open('./dic.json', 'r') as dic:
        data = json.load(dic)
        collection[1] = collection[1].tolist()
        if data == {}:
            with open('./dic.json', 'w') as f:
                collection = [collection]
                json.dump(collection, f)
        else:
            data.append(collection)
            with open('./dic.json', 'w') as f:
                json.dump(data, f)
    return "saved"


"""
    function that take the collection in the database, the last collection in the database

"""

def get_collection():
    # read from JSON file
    with open('./dic.json', 'r') as f:
        dic = json.load(f)
        for item in dic:
            item[1] = np.array(item[1])
    return dic