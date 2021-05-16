import glob
from moviepy.editor import *
from collections import OrderedDict
from PIL import Image
import numpy

imgs = {}
clip = []
count = 0

for path in glob.glob("images/*.png"):
    num = int(path.replace("images/img","").replace(".png",""))
    imgs[num] = path

imgs = OrderedDict(sorted(imgs.items()))

clip = ImageSequenceClip([numpy.array(Image.open(m)) for m in imgs.values()], 30)

clip.write_videofile("result.mp4")


