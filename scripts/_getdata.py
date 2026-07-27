import os, json, platform, shutil, subprocess, sys

class GetTrash():

    def trash_size():

        total = 0

        with open('data.json', 'r') as file:
            data = json.load(file)
            path = data['settings']['path']

        for root, _, files in os.walk(path):
            for file in files:
                if file.startswith("$R"):

                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)

                    total += file_size

        print("trash_size() ", total)
        
        total = int(total / (1024 ** 2)) #to mb

        return total


    def deafult_path():

        if platform.system() == 'Windows':
            path = r"C:\$Recycle.Bin"

        elif platform.system() == 'Linux':
            path = "~/.local/share/Trash"

        elif platform.system() == 'Darwin':
            path = '~/.Trash'

        print("detect_os() ", path)
        return path


    def deafult_limit():

        limit = shutil.disk_usage("/").total * 0.05

        print("get_5pr_ofdisk()  ", limit)

        limit = int(limit / (1024 ** 2)) #to mb

        return limit