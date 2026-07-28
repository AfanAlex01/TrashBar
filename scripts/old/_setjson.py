# from _getdata import GetTrash
from scripts._getdata import GetTrash

import json

def set_trash():

    print("set_trash()")

    try:

        with open('data.json', 'r') as file:
            data = json.load(file)

    except FileNotFoundError:

        print("FileNotFoundError")
        set_settings()

        with open('data.json', 'r') as file:
            data = json.load(file)


    data['size'] = GetTrash.trash_size()

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)


def set_settings():

    print("set_settings()")

    # try:
        
    #     with open('data.json', 'r') as file:
    #         data = json.load(file)

    #         path = data['settings']['path']
    #         limit = data['settings']['limit']

    #         if path == "":
    #             path = GetTrash.deafult_path()
    #         if limit <= 0:
    #             limit = GetTrash.deafult_limit()

    # except FileNotFoundError:

    path = GetTrash.deafult_path()
    limit = GetTrash.deafult_limit()

    # total = GetTrash.trash_size()

    data = {
            "size": 0,
            "settings": {
                "path": path,
                "limit": limit
            }
        }

    
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)
