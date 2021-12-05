# import sys
# import time

# import zmq

# port = sys.argv[1]
# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind(f"tcp://*:{port}")

# while True:
#     message = socket.recv()
#     print(f"Received message: {message}")
#     time.sleep(0.5)
#     message = f"Reply from {port} for message: {message.decode()}"
#     socket.send(message.encode())

# import zmq
# import random
# import time

# context = zmq.Context()
# socket = context.socket(zmq.PUB)
# socket.bind("tcp://*:6556")
# while True:
#     temp = f"temp {random.randint(15, 25)}"
#     socket.send(temp.encode())
#     volt = f"volt {random.randint(0, 500) / 100}"
#     socket.send(volt.encode())
#     time.sleep(1)

import numpy as np
import matplotlib.pyplot as plt
import zmq
from skimage import draw
import time

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

imgs = gen3d()

t = time.perf_counter()
filtered = median_filter(imgs[0])
print(f"Elapse: {time.perf_counter() - t} s")

plt.subplot(121)
plt.imshow(imgs[0])
plt.subplot(122)
plt.imshow(filtered)
plt.show()