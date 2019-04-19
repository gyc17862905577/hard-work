# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
#图像方差的计算函数
def getImageVar(imgPath):    
    image = cv2.imread(imgPath)    
    img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    
    imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()    
    return imageVar
imageVar = getImageVar("C:/Users/Amy/Desktop/test.jpg")
print(imageVar)

#图像清晰度判别函数
def distinct(imgPath):
    imageVar = getImageVar(imgPath)
    if imageVar>500:
        print "图像清晰"
    else:
        print "图像模糊"
