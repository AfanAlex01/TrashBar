import platform, winshell, subprocess, os, playsound

def clean_trash():

        if platform.system() == 'Windows':
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

        elif platform.system() == 'Linux': # TODO: except error

                if 'KDE' in os.environ.get('XDG_CURRENT_DESKTOP'):
                        subprocess.run(['ktrash6', '--empty'])

                elif 'GNOME' in os.environ.get('XDG_CURRENT_DESKTOP'):
                        subprocess.run(['gio', 'trash', '--empty'])
                        
                else:
                        subprocess.run(['trash-empty'])
                        # subprocess.run(['rm', '-rf', '~/.local/share/Trash/*'])

        elif platform.system() == 'Darwin':
                subprocess.run(['rm' '-rf' '~/.Trash/*']) #need to test this

        playsound.playsound("assets/sounds/drop_sound.wav")    