import os, json, platform, shutil

class GetTrash():

    def trash_size():

        total = 0

        with open('resourses/data.json', 'r') as file:
            data = json.load(file)
            path = data['settings']['path']

        for root, _, files in os.walk(path):
            for file in files:
                if file.startswith("$R"):

                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)

                    total += file_size

        total = int(total / (1024 ** 2)) #to mb

        print('get_trash_size ', total)
        return total


    def deafult_path():

        if platform.system() == 'Windows':
            path = r"C:\$Recycle.Bin"

        elif platform.system() == 'Linux':
            path = "~/.local/share/Trash"

        else:
            #trow error
            print("error")

        print("detect_os ", path)
        return path


    def deafult_limit():

        limit = shutil.disk_usage("/").total * 0.05

        limit = int(limit / (1024 ** 2)) #to mb

        print("get_5pr_ofdisk ", limit)
        return limit