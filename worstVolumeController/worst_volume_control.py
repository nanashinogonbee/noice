from PIL import Image
from math import ceil
import sys
import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
try:
    import alsaaudio
except ImportError as e:
    messagebox.showerror(
        'No required modules!',
        '''Please install python3-alsaaudio:
"sudo pip3 install pyalsaaudio" or "sudo dnf install python3-alsaaudio"'''
        )
    sys.exit()


def sendNotify(message):
    subprocess.Popen(['notify-send', message])
    return


def setVolume():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        initialdir='.',
        title='The worst volume controller. Have fun.',
        filetypes=(
            ('JPEG', '*.jpg'),
            ('PNG', '*.png'),
            ('WEBP', '*.webp'),
            )
        )

    if not file_path:  # if no files specified ("Cancel" button pressed etc.)
        messagebox.showerror('oof', 'oof')
        sys.exit()

    im = Image.open(file_path).convert('1')
    W, H = im.size
    BRIGHTNESS = im.histogram()[-1] / (W * H) * 100
    VOLUME = ceil(BRIGHTNESS)  # volume in percents, 255 = 100%
    m = alsaaudio.Mixer()
    m.setmute(False)
    m.setvolume(VOLUME)
    sendNotify(f'Volume set to {VOLUME}%. ;)')


if __name__ == '__main__':
    if os.name == 'posix':
        setVolume()
    else:
        messagebox.showerror(
            'Unsupported OS!',
            'This thing runs only on Linux-based operating systems' +
            'at the moment.'
            )
else:
    print('Do not launch this from external scripts!')
    sys.exit()
