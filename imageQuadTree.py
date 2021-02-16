'''
Image quadtree art implementation.

References:
    1) https://medium.com/analytics-vidhya/transform-an-image-into-a-quadtree-39b3aa6e019a
    2) https://estebanhufstedler.com/2020/05/05/image-quadrangulation/
'''

import imageio
import numpy as np
from PIL import Image, ImageDraw

# TODO
# 1) Output scale (?) -> also max size should be proportional to max recursion
    # the maximum number of quadrants is 4^n where n is the maximum recursion level

def ensure_square(img):
        '''Ensures that the input image is square. If not, it tries to square it'''

        h, w = img.shape[:2]
        if h != w:
            if h < w:
                diff = w - h
                left_border = diff//2
                right_border = diff - left_border
                img = img[:, left_border: -right_border ]
            elif h > w:
                diff = h - w
                left_border = diff//2
                right_border = diff - left_border
                img = img[:, left_border: -right_border ]
        return img

class ImageQuad:
    def __init__(self, filename, epsilon=30, max_recurse=100,
                draw_outine=False):
   
        self.img = ensure_square(imageio.imread(filename)) 
        self.canvas = None
        self.draw = None
        self.epsilon = epsilon
        self.recurse_depth = 0
        self.max_depth = max_recurse
        self.height, self.width = self.img.shape[0], self.img.shape[1]
        self.draw_outine = draw_outine

    def recursive_draw(self, x:int, y:int, w:int, h:int):
        '''Draw the QuadArt recursively
        '''
        x, y, w, h = int(x), int(y), int(w), int(h)
        # Split the img into 4 quadrants if the distribution of color differs "too much" from mean color
        if self.should_split(x, y, w, h):
            self.recurse_depth += 1
            self.recursive_draw(x, y, w//2, h//2)
            self.recursive_draw(x + w//2, y, w//2, h//2)
            self.recursive_draw(x, y + h//2, w//2, h//2)
            self.recursive_draw(x + w//2, y + h//2, w/2, h//2)
            self.recurse_depth -= 1

        else: # otherwise draw the quadrant
            self.draw_avg(x, y, w, h)

    def should_split(self, x: int, y: int, w: int, h: int) -> bool:
        '''
        Returns boolean wheter you should split a quadrant or not
        '''

        if self.recurse_depth > self.max_depth:
            return False

        # check the size of the quadrant
        if w <= 2 or h <= 2:
            return False

        # Compute the standard deviation for the color distribution
        # and check wheter it is larger than some threshold. In other
        # words, it estimates how close the image (the quadrant) is
        # similar to its mean color
        quadrant = self.img[y:y+h,x:x+w]
        std = np.std(quadrant, axis=(0,1))
        if np.any(std > self.epsilon):
            return True
    
    def draw_avg(self, x:int, y:int, w:int, h:int) -> None:
            
        quadrant = self.img[y:y+h,x:x+w]
        mean_color = np.mean(quadrant, axis=(0,1), dtype=int)
        # mean_color = np.append(mean_color, 255)
        if self.draw_outine:
            self.draw.rectangle((x, y, x+w, y+h), 
                            fill=tuple(mean_color),
                            outline="black")
        else:
            self.draw.rectangle((x, y, x+w, y+h), 
                            fill=tuple(mean_color))
    def generate(self):
        self.canvas = Image.new("RGBA", (self.width, self.height), (255,255,255))
        self.draw = ImageDraw.Draw(self.canvas)
        self.recursive_draw(0, 0, self.width, self.height)
        del self.draw

    def display(self):
        display(self.canvas)

    def save(self, filename):
        self.canvas.save(filename, "PNG")