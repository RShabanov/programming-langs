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

import zmq
import time
import images_gen as ig

# imgs = gen3d()

# t = time.perf_counter()
# filtered = median_filter(imgs[0])
# print(f"Elapse: {time.perf_counter() - t} s")

# plt.subplot(121)
# plt.imshow(imgs[0])
# plt.subplot(122)
# plt.imshow(filtered)
# plt.show()

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:6556")

    c = 0
    while True:
        imgs = ig.gen3d()
        socket.send_pyobj(imgs)
        print(f"Sent images #{c}")
        time.sleep(1)
        c += 1