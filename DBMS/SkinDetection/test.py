from cgi import test
from PIL import Image
import os
import glob
from cmath import pi
import numpy as NP

prob = NP.zeros([256,256,256])
f = open('D:/Coding/5th-Sem/DBMS/SkinDetection/data.txt', 'r')
threshold = 1.0
count = 0
for i in range(256):
    for j in range(256):
        for k in range(256):
            line = f.readline()
            prob[i][j][k]=float(line)

testImage = Image.open('D:/Coding/5th-Sem/DBMS/SkinDetection/ibtd/0257.jpg')
pixel = testImage.load()
pixel_out = testImage.load()

for y in range(testImage.size[1]):
    for x in range(testImage.size[0]):
        if prob[pixel[x,y][0]][pixel[x,y][1]][pixel[x,y][2]]>=threshold:
            pixel_out[x,y]=pixel[x,y]
        else:
            pixel_out[x,y]=(255,255,255)

testImage.save('D:/Coding/5th-Sem/DBMS/SkinDetection/output.bmp')
