from multiprocessing import get_logger
import cv2
import sys
import numpy as np
import time
from socket import socket

from numpy.core.fromnumeric import size

mode = True
drawing = False

def drawNet(img : np.ndarray, scale : int):
    Vertical = 104
    Horizontal = 50

    Height = 480
    Width = 1028

    count_Veritcal = 0
    count_Horizontal = 0

    for i in range(0, Vertical):
        if count_Veritcal == scale:
            cv2.line(img, (10 * i + 10, 0), (10 * i + 10, Height), (0, 0, 0), 1)
            count_Veritcal = 0
        count_Veritcal += 1

    for i in range(0, Horizontal):
        if i == 23:
            cv2.line(img, (0, 10 * i + 10), (Width, 10 * i + 10), (0, 0, 0), 2)
        elif i == 13:
            cv2.line(img, (0, 10 * i + 10), (Width, 10 * i + 10), (0, 0, 255), 2)
        else:
            count_Horizontal += 1
            if count_Horizontal == scale:
                cv2.line(img, (0, 10 * i + 10), (Width, 10 * i + 10), (0, 0, 0), 1)
                count_Horizontal = 0
            

    return img

def drawButton(img : np.ndarray):
    wButton = 90
    hButton = 30

    cv2.rectangle(img, (1048, 10), (1048 + wButton, 10 + hButton), (0, 255, 255), -1)
    cv2.rectangle(img, (1048, 10), (1048 + wButton, 10 + hButton), (0, 0, 0), 1)
    cv2.putText(img, 'snapshot', (1058, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    return img

def initDisplay(scale : int, device : str):
    image = np.ones((480, 1150, 3), np.uint8)
    image = image * 255

    image = drawNet(image, scale)
    image = drawButton(image)

    return image


yEx = 240
eF = 100

def draw(plot : np.ndarray, value : float, points : list, scale : int, device : str):
    x1, y1, x, y2 = points

    y2 = (-value) / 100
    percent_show = y2 * (-100)

    cv2.line(plot, (int(x1 * eF), int(y1 * eF + yEx)), (int(x * eF), int(y2 * eF + yEx)), (255, 0, 0), 2)
    cv2.rectangle(plot, (0, 0), (200, 80), (255, 255, 255), -1)
    cv2.rectangle(plot, (0, 0), (200, 80), (0, 0, 0), 1)
    cv2.putText(plot, f'{device.upper()} (%): {round(percent_show, 2)}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    #cv2.putText(plot, f'Core: {core_number}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    x1 = x
    y1 = y2

    x += 0.03

    if int(x * eF) >= 1028:
        x = 0
        x1 = 0
        y1 = 0
        y2 = 0

        plot = initDisplay(scale, device)

    points.clear()
    points.append(x1)
    points.append(y1)
    points.append(x)
    points.append(y2)

    return plot

def process_handle(img : np.ndarray, point : list):
    loc_btn = [1048, 10]
    size_btn = [90, 30]

    if ((point[0] > loc_btn[0]) and (point[0] < loc_btn[0] + size_btn[0])) and ((point[1] > loc_btn[1]) and (point[1] < loc_btn[1] + size_btn[1])):
        t_img = img[:, 0 : 1028, :]
        cv2.imwrite('snapshot.jpg', t_img)

def client(device : str, scale : int):
    host = '192.168.0.111'
    port = 7000

    client = socket()

    try:
        client.connect((host, port))
    except Exception as e:
        sys.exit()

    buff = bytearray(10)
    nbytes = client.recv_into(buff, 10)
    buff = buff[0: nbytes].decode('utf-8')

    image = initDisplay(scale, device)

    def interactive_drawing(event, x, y, flags, param):
        global ix, iy, drawing, mode
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv2.EVENT_LBUTTONUP:
            if mode == True:
                # cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
                process_handle(image, (x, y))

    cv2.namedWindow(f'Monitor: {device}')
    cv2.setMouseCallback(f'Monitor: {device}',interactive_drawing)

    points = [0, 0, 0, 0]
    while True:
        client.send(device.encode('utf-8'))
        #
        value = bytearray(50)
        nbytes = client.recv_into(value, 50)
        value = value[0:nbytes].decode('utf-8')
        #
        image = draw(image, float(value), points, scale, device)

        cv2.imshow('Monitor: ' + device, image)
        if cv2.waitKey(40) == 27:
            client.send(str.encode('exit'))
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) > 0:
        client(sys.argv[1], int(sys.argv[2]))