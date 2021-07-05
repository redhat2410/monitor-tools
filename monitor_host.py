import cv2
import sys
import pynvml as N
import numpy as np
import time
from check_gpu import GPUsystem
import psutil
from socket import socket
from multiprocessing import Process

def process_client(client : socket):
    print('\tAdd client')
    gpu = GPUsystem()
    ack = client.send(str.encode('client'))

    while True:
        buff = bytearray(10)
        nbytes = client.recv_into(buff, 10)
        buff = buff[0 : nbytes].decode('utf-8').lower()

        if buff == 'cpu':
            value = getCPU()
            client.send(str(value).encode('utf-8'))
        elif buff.find('gpu') != -1:
            index = buff.replace('gpu', '')
            value = getGPU(gpu, int(index))
            client.send(str(value).encode('utf-8'))
        elif buff == 'exit':
            client.close()
            break
        else:
            time.sleep(0.1)
        time.sleep(0.05)
    print('\tRemove client')

def createHost():
    host = '192.168.0.111'
    port = 7000

    server = socket()

    try:
        server.bind((host, port))
    except Exception as e:
        print(e)
        sys.exit()

    server.listen(5)

    print('\tSERVER ON')

    while True:
        try:
            client, _ = server.accept()

            pClient = Process(target=process_client, args=(client, ))
            pClient.start()
        except KeyboardInterrupt:
            break



def getCPU():
    cpu_precent = psutil.cpu_percent(interval=None, percpu=False)
    return cpu_precent

def getGPU(gpu : GPUsystem, index : int):
    gpu_precent = gpu.utilization(index).gpu
    return gpu_precent
    
if __name__ == '__main__':
    createHost()
