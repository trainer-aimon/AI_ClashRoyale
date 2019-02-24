# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:03:32 2019

@author: Aimon
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui as pag
import win32api as wpi


def process_img(image):#处理图像函数，输入图像，返回处理后的图像
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    # edge detection
#    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    processed_img = cv2.resize(processed_img,(300,500))
    return processed_img

def main():#主程序
    last_time = time.time()
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(0,40,530,1000)))
        frames = 1/(time.time()-last_time)
        currentMouseX, currentMouseY = pag.position()
#        c = -1
        click = wpi.GetKeyState(0x01)
        if click >= 0:
            click=0
        else:
            click=1
        print('{:.0f},{},{},{}'
        .format(frames, currentMouseX, currentMouseY, click))
        
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if currentMouseX >=600:
            cv2.destroyAllWindows()
            break

def countdown():
    for i in range(5,-1,-1):
        print('\r','距离游戏开始还有 %s 秒！' % str(i).zfill(2),end='')
        time.sleep(1)
    print('\r','{:^20}'.format('计时开始！'))



###
countdown()

main()