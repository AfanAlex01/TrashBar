from _getdata import GetTrash

import configparser

def sset_deafult():

    config = configparser.ConfigParser()

    config.add_section('trash')
    config.set('trash', 'trash', str(GetTrash.trash_size()))

    config.add_section('settings')
    config.set('settings', 'path', GetTrash.deafult_path())
    config.set('settings', 'limit', str(GetTrash.deafult_limit()))

    with open('assets/configdontouch.ini', 'w') as configfile:
        config.write(configfile)

sset_deafult()