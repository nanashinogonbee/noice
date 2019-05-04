from PIL import Image
from math import ceil
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
try:
    import alsaaudio
except ImportError as e:
    print('''Please install python3-alsaaudio:
sudo pip3 install pyalsaaudio
or
sudo dnf install python3-alsaaudio''')


def okDialog(msg):
    confirm = messagebox.showerror(
        'Do I look like I know what a JPEG is?',
        msg
        )
    return confirm


def sendNotify(message):
    subprocess.Popen(['notify-send', message])
    return


def setVolume():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    if not file_path:  # if no files specified ("Cancel" button pressed etc.)
        sys.exit()

    ext = file_path.split('.')[-1]
    if ext in ('jpg', 'png', 'webp'):
        try:
            im = Image.open(file_path).convert('RGB')
        except OSError:
            print('Image is empty!')

        RGBsum = 0
        POINTS = im.size[0] * im.size[1]  # quantity of pixels in an image
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                pix = im.getpixel((x, y))  # RGB of a pixel
                midRGBval = sum(pix) // len(pix)  # mid RGB val ("brightness")
                RGBsum += midRGBval
        RGBsum //= POINTS  # middle RGB value ("brightness") of a picture

        bw = im.convert('1')
        hist = bw.histogram()
        print(hist)

        """
        VOLUME = ceil(100 / 255 * RGBsum)  # volume in percents, 255 = 100%
        m = alsaaudio.Mixer()
        m.setmute(False)
        m.setvolume(VOLUME)
        sendNotify(f'Volume set to {VOLUME}%. ;)')
        """
    else:
        okDialog('Not an image!')


if __name__ == '__main__':
    setVolume()
else:
    print('Do not launch this from external scripts!')
