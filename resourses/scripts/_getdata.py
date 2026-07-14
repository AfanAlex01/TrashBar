import os, json, platform, shutil

class GetTrash():

    def __init__(self):

        with open('resourses/data.json', 'r') as file:
            data = json.load(file)
        
        self.total = 0

        self.path = data['settings']['path']
        self.limit = data['settings']['limit']


    def get_update(self):

        print("get_update")

        if self.path == "":
            self.deafult_path()
        if self.limit <= 0:
            self.deafult_limit()

        self.trash_size()

        data = {
            "size": self.total,
            "settings": {
                "path": self.path,
                "limit": self.limit
            }
        }

        with open('resourses/data.json', 'w') as file:
            json.dump(data, file, indent=2)


    def trash_size(self):

        for root, _, files in os.walk(self.path):
            for file in files:
                if file.startswith("$R"):

                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)

                    self.total += file_size

        self.total = int(self.total / (1024 ** 2)) #to mb

        print('get_trash_size ', self.total)


    def deafult_path(self):

        if platform.system() == 'Windows':
            self.path = r"C:\$Recycle.Bin"

        elif platform.system() == 'Linux':
            self.path = "~/.local/share/Trash"

        else:
            #trow error
            print("error")

        print("detect_os ", self.path)


    def deafult_limit(self):

        self.limit = shutil.disk_usage("/").total * 0.05

        self.limit = int(self.limit / (1024 ** 2)) #to mb

        print("get_5pr_ofdisk ", self.limit)
