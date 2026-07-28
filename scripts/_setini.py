from scripts._getdata import GetTrash

import configparser

def sset_INI():

    config = configparser.ConfigParser()

    try:
        config.read('assets/configdontouch.ini')

        if not config.has_section('trash'):
            config.add_section('trash')

        config.set('trash', 'trash', str(GetTrash.trash_size()))

        if config.has_section('settings'):

            if not config.has_option('settings', 'path'):
                config.set('settings', 'path', GetTrash.deafult_path())

            if not config.has_option('settings', 'limit'):
                config.set('settings', 'limit', str(GetTrash.deafult_limit()))

        else:
            config.add_section('settings')
            config.set('settings', 'path', GetTrash.deafult_path())
            config.set('settings', 'limit', str(GetTrash.deafult_limit()))


    except FileNotFoundError, configparser.MissingSectionHeaderError:

        config.add_section('trash')
        config.set('trash', 'trash', str(GetTrash.trash_size()))

        config.add_section('settings')
        config.set('settings', 'path', GetTrash.deafult_path())
        config.set('settings', 'limit', str(GetTrash.deafult_limit()))


    with open('assets/configdontouch.ini', 'w') as configfile:
        config.write(configfile)