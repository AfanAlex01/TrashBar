# from _getdata import GetTrash
from resourses.scripts._getdata import GetTrash

import json

def set_json():

    print("set_json")

    total = GetTrash.trash_size()
        
    with open('resourses/data.json', 'r') as file:
        data = json.load(file)

        path = data['settings']['path']
        limit = data['settings']['limit']

        if path == "":
            path = GetTrash.deafult_path()
        if limit <= 0:
            limit = GetTrash.deafult_limit()

    data = {
            "size": total,
            "settings": {
                "path": path,
                "limit": limit
            }
        }
        
    with open('resourses/data.json', 'w') as file:
        json.dump(data, file, indent=2)

set_json()