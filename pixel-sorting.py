import numpy as np
import scipy.misc as misc
import requests
from PIL import Image

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

def pixelize(image_url, timeout=30):
    img = Image.open(StringIO(requests.get(image_url.strip(), timeout=timeout, verify=False).content))
    img = misc.imresize(img, (24, 72), 'nearest')
    img = np.sort(img, axis=0)
    img = misc.imresize(img, (72, 72), 'nearest')
    misc.imsave('icon.png', img)



if __name__ == "__main__":

    pixelize('https://s3-us-west-2.amazonaws.com/sfmomamedia/media/t/collection_images/5l7d71_zC4Ow.jpg')
