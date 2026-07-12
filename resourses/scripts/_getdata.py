import os, json, platform, shutil

class GetTrash:

    def detect_os():

        if platform.system() == 'Windows':
            path = r"C:\$Recycle.Bin"

        elif platform.system() == 'Linux':
            path = "~/.local/share/Trash"

        else:
            #trow error
            print("error")


        #safe json
        with open('resourses/data.json', 'r') as file:
            data = json.load(file)

        data['settings']['path'] = path
        
        with open('resourses/data.json', 'w') as file:
            json.dump(data, file, indent=2)
    


    def get_5pr_ofdisk():

        size5 = shutil.disk_usage("/").total * 0.05

        #safe json
        with open('resourses/data.json', 'r') as file:
            data = json.load(file)

        data['settings']['limit'] = int(size5 / (1024 ** 2)) #to mb
        
        with open('resourses/data.json', 'w') as file:
            json.dump(data, file, indent=2)
    


    def get_trash_size():

        with open('resourses/data.json', 'r') as file:
            data = json.load(file)

        total = 0

        for root, _, files in os.walk(data['settings']['path']):
            for file in files:
                if file.startswith("$R"):

                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)

                    total += file_size
                    

        #safe json
        data['size'] = int(total / (1024 ** 2)) #to mb
        
        with open('resourses/data.json', 'w') as file:
            json.dump(data, file, indent=2)


gettrash = GetTrash()