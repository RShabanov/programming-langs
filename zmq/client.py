# import sys
# import zmq

# context = zmq.Context()
# socket = context.socket(zmq.REQ)

# for port in sys.argv[1:]:
#     socket.connect(f"tcp://127.0.0.1:{port}")

# for i in range(10):
#     socket.send((f"Message {i}").encode())
#     print(socket.recv())

# socket.close()

from numpy.core.numeric import indices
import zmq
import sys
import time
import matplotlib.pyplot as plt
import images_gen as ig
from concurrent.futures import ProcessPoolExecutor
import gc

# topic = sys.argv[1]

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
socket.connect("tcp://127.0.0.1:6556")

if __name__ == "__main__":
    with ProcessPoolExecutor() as ppe:
        tasks = []
        while True:
            print("Receiving data...")
            array = socket.recv_pyobj()

            # ppe.map(ig.median_filter, array)

            if len(tasks) == 0:
                gc.collect()
                for i in range(len(array)):
                    print(f"Processing image # {i}")
                    future = ppe.submit(ig.median_filter, array[i])
                    tasks.append(future)

            indices = []
            for i, task in enumerate(tasks):
                if task.done():
                    task.result()
                    indices.append(i)
                    print(f"Finished task # {i}")
            
            for i in indices[::-1]:
                tasks.pop(i)
                    
            time.sleep(1)

# for _ in range(10):
#     print(socket.recv())