import platform, subprocess, configparser

def open_trash():

    config = configparser.ConfigParser()
    config.read('assets/configdontouch.ini')

    if platform.system() == 'Windows':
        subprocess.Popen(['explorer', 'shell:RecycleBinFolder'])

    elif platform.system() == 'Linux':
        subprocess.Popen(['xdg-open', 'trash:/'])

    elif platform.system() == 'Darwin':
        subprocess.run(['open' '~/.Trash']) #need to test this