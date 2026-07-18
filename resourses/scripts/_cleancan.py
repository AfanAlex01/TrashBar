import platform, winshell, subprocess

def clean_trash():
        if platform.system() == 'Windows':
            winshell.recycle_bin().empty(confirm=True, show_progress=False, sound=True)

        elif platform.system() == 'Linux':
            subprocess.run(['rm', '-rf', '~/.local/share/Trash/*'])

        # elif platform.system() == 'Darwin':
        #     winshell.recycle_bin().empty(confirm=True, show_progress=False, sound=True)
