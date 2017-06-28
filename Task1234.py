# -*- coding: utf-8 -*-
"""
Jose Fernández Ortiz
"""
import numpy as np
import cv2
import os

path ='c:\\improc'
os.chdir(path)
#↓show an image
im = cv2.imread('lena.jpg')
print im.ndim, im.shape, im.dtype, im.itemsize
#cv2.imshow('Lena',im)

#read as an grayscale image 
im2 = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

#cv2.imshow('Lean grayscale', im2)
print im2.ndim, im2.shape, im2.dtype, im2.itemsize

#Task 1
im[:,:,0] = 0
         
#cv2.imshow('Lena Blue', im)

#Task 2 
im3 = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

im3[:,:,0] = 255
#cv2.imshow('Hue Chanel Max',im3)
im3[:,:,0] =  0   
#cv2.imshow('Hue Chanel Min',im3)
im3[:,:,1] = 255
#cv2.imshow('Saturation Max',im3)      
im3[:,:,1] = 0
#cv2.imshow('Saturation Min',im3) 
im3[:,:,2] = 255
#cv2.imshow('Value Max',im3)      
im3[:,:,2] = 0
#cv2.imshow('Value Min',im3)      
        
#Task 3
im4 = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

imageg = (255-im4)
#cv2.imshow('Lean grayscale', imageg)

#task4 
im5 = cv2.imread('lena.jpg')
#imagec = (255-im5)
cv2.imshow('Lean grayscale', imageg)
cv2.waitKey()
cv2.destroyAllWindows()
