import PIL
from PIL import Image
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='A python script to approximate an image using QuadTree')
parser.add_argument( 'img_path', action = 'store', type = str, help = 'The image to process.' )
args = parser.parse_args( )
img_path = args.img_path


img = Image.open(img_path)
# img.show()
pix = np.array(img) 



# References
# 1) https://medium.com/analytics-vidhya/transform-an-image-into-a-quadtree-39b3aa6e019a
# 2) https://estebanhufstedler.com/2020/05/05/image-quadrangulation/
