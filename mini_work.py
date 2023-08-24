import cv2 as cv
import numpy as np

image_path='images_py/RGB lena.ppm'
gray_image=cv.imread(image_path,cv.IMREAD_GRAYSCALE)
cv.imshow('lena gray',gray_image)


rgb_image=cv.imread(image_path)
cv.imshow('rgb',rgb_image)
# splitting it into the individual color channels 
r,g,b=cv.split(rgb_image)
cv.imshow('red',r)
cv.imshow('green',g)
cv.imshow('blue',b)
# merging 
merged=cv.merge([r,g,b])
cv.imshow('merged image',merged)



cv.waitKey(0)