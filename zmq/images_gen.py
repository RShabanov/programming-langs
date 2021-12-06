import numpy as np
from skimage import draw

def gen2d():
    x, y = np.mgrid[0:1:400j, 0:1:400j]
    f1 = np.random.randint(2, 10)
    f2 = np.random.randint(2, 10)
    return x*(1-x)*np.cos(f1*np.pi*x)*np.sin(f2*np.pi*y**2)**2

def gen3d():
    imgs = []
    for _ in range(10):
        img = gen2d()

        for _ in range(10):
            padding = 5
            x1, y1, x2, y2 = np.random.randint(padding, img.shape[0] - padding, size=4)

            rr, cc = draw.line(x1, y1, x2, y2)
            img[rr, cc] = img.max() * 0.95

        imgs.append(img)
    return imgs

def median_filter(img):
    result = img.copy()

    padding = 3
    for i in range(padding, img.shape[0] - padding):
        for j in range(padding, img.shape[0] - padding):
            sub = img[i-padding: i+padding+1, j-padding:j+padding+1]
            result[i, j] = np.median(sub)
    return result