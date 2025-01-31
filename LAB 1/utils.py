import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def line_draw(line, canv, size, color=(255,255,255)):
    def get_y(t):
        return -(line[0] * t + line[2]) / line[1]

    def get_x(t):
        return -(line[1] * t + line[2]) / line[0]

    w, h = size

    if line[0] != 0 and abs(get_x(0) - get_x(w)) < w:
        beg = (get_x(0), 0)
        end = (get_x(h), h)
    else:
        beg = (0, get_y(0))
        end = (w, get_y(w))
    canv.line([beg, end], width=4, fill=color)


def plot_img(img):
    h,w,_  = np.array(img).shape
    plt.figure(figsize=(w / 200, h / 200))
    plt.tight_layout(pad=0.0)
    plt.imshow(img,aspect='auto')
    plt.show()
