# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:39:22 2019

@author: Amy
"""
import numpy as np
import cv2
 
ak1=cv2.imread('C:/Users/Amy/Desktop/20180918144649700.jpg');
ak2=cv2.imread('C:/Users/Amy/Desktop/20180918144529320.jpg');
h,w,s=ak1.shape
print('高度%d,宽度%d,图层数%d'%(h,w,s))
ak2=cv2.resize(ak2,(w,h),interpolation=cv2.INTER_LINEAR)
b, g, r = cv2.split(ak2)#通道拆分函数
b_a=np.asarray(b)
g_a=np.asarray(g)
r_a=np.asarray(r)
print(r_a.shape)
print(b_a[0][0])
print(g_a[0][0])
print(r_a[0][0])
mc=np.zeros((h,w))
print(mc.shape)
for i in range(h):
    for j in range(w):
        mc[i][j]=int(b_a[i][j])+int(g_a[i][j])+int(r_a[i][j])
 
h,w=mc.shape
avarege=int((np.sum(mc)/(w*h))*0.75)
gatesize=avarege
print(gatesize)
for i in range(h):
    for j in range(w):
        if mc[i][j]>=gatesize:
            ak2[i][j][0]=ak1[i][j][0]
            ak2[i][j][1] = ak1[i][j][1]
            ak2[i][j][2] = ak1[i][j][2]
cv2.namedWindow("img_add",cv2.WINDOW_NORMAL);
cv2.imshow('img_add',ak2)
cv2.imshow('ak1',ak1)
cv2.imwrite('C:/Users/Amy/Desktop/11.jpg',ak2)
cv2.waitKey()

