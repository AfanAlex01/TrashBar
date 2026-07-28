import platform, winshell, subprocess, os

def clean_trash():
        if platform.system() == 'Windows':
            winshell.recycle_bin().empty(confirm=True, show_progress=False, sound=True)

        elif platform.system() == 'Linux':

            if 'KDE' in os.environ.get('XDG_CURRENT_DESKTOP'):
                subprocess.run(['ktrash6', '--empty'])

            elif 'GNOME' in os.environ.get('XDG_CURRENT_DESKTOP'):
                subprocess.run(['gio', 'trash', '--empty'])
                 
            else:
                # subprocess.run(['rm', '-rf', '~/.local/share/Trash/files/*'])
                # subprocess.run(['rm', '-rf', '~/.local/share/Trash/info/*'])

                subprocess.run(['rm', '-rf', '~/.local/share/Trash/*'])

        elif platform.system() == 'Darwin':
            subprocess.run(['rm' '-rf' '~/.Trash/*']) #need to test this