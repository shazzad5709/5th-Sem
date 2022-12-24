import glob
import os
import random
import time
from cgi import test
from cmath import pi
import numpy as NP
from PIL import Image

start_time = time.time()
accuracy_file = open('DBMS/Accuracy_data.txt', 'w')
k_fold = 10
train = 500
test = 55

true_pos, true_neg, false_pos, false_neg = 0, 0, 0, 0

image_folder = 'DBMS/ibtd'
mask_folder = 'DBMS/ibtd/mask'

images = os.listdir(image_folder)
images = images[:len(images)-2]
masks = os.listdir(mask_folder)
masks = masks[:len(masks)-1]

for ki in range(k_fold):
    print(f'Iter {ki+1} started...')
    indices = ["%04d" % x for x in range(555)]
    random.shuffle(indices)
    file = open('DBMS/data_v2.txt', 'w')
    skin_pix_count = NP.zeros([256,256,256])
    non_skin_pix_count = NP.zeros([256,256,256])
    prob_skin = NP.zeros([256,256,256])
    prob_non_skin = NP.zeros([256,256,256])
    total_skin = 0
    total_non_skin = 0

    for index in range(train):
        img = Image.open('DBMS/ibtd/'+str(indices[index])+'.jpg')
        mask = Image.open('DBMS/ibtd/Mask/'+str(indices[index])+'.bmp')
        for(pixel, pix_mask) in zip(img.getdata(), mask.getdata()):
            if pix_mask[0]<255 or pix_mask[1]<255 or pix_mask[2]<255:
                skin_pix_count[pixel[0]][pixel[1]][pixel[2]] += 1
                total_skin += 1
            else:
                non_skin_pix_count[pixel[0]][pixel[1]][pixel[2]] += 1
                total_non_skin += 1

    for i in range(0, 256):
        for j in range(0, 256):
            for k in range(0, 256):
                prob_skin[i][j][k] = skin_pix_count[i][j][k]/total_skin
                prob_non_skin[i][j][k] = non_skin_pix_count[i][j][k]/total_non_skin
                if prob_non_skin[i][j][k]==0 and prob_skin[i][j][k]==0:
                    file.write(str(0)+"\n")
                elif prob_non_skin[i][j][k]==0:
                    file.write(str(100)+'\n')
                else:
                    prob_skin[i][j][k] = prob_skin[i][j][k]/prob_non_skin[i][j][k]
                    file.write(str(prob_skin[i][j][k])+'\n')
    file.close()


    prob = NP.zeros([256,256,256])
    f = open('DBMS/data.txt', 'r')
    threshold = 1.0
    count = 0
    for i in range(256):
        for j in range(256):
            for k in range(256):
                line = f.readline()
                prob[i][j][k]=float(line)
    
    for index in range(test):                                     
        testImg = Image.open('DBMS/ibtd/'+str(indices[index+train])+'.jpg')
        testMask = Image.open('DBMS/ibtd/Mask/'+str(indices[index+train])+'.bmp')
        pixel = testImg.load()
        mask_pix = testMask.load()
        for y in range(testImg.size[1]):
            for x in range(testImg.size[0]):
                if prob[pixel[x,y][0]][pixel[x,y][1]][pixel[x,y][2]]>=threshold:
                    pred=1
                else:
                    pred=0
        
                
                if mask_pix[x,y][0]>250 and mask_pix[x,y][1]>250 and mask_pix[x,y][2]>250:
                    actual = 0
                else:
                    actual = 1

                if pred==1 and actual==1:
                    true_pos+=1
                elif pred==1 and actual==0:
                    false_pos+=1
                elif pred==0 and actual==1:
                    false_neg+=1
                elif pred==0 and actual==0:
                    true_neg+=1


    accuracy_file.write(f'Iteration {ki+1}: \nTP: {true_pos} \nFP: {false_pos} \nTN: {true_neg} \nFN: {false_neg}\n')
    accuracy_file.write(f'Accuracy: {(true_pos + true_neg) / (true_pos+true_neg+false_pos+false_neg)}\n')

accuracy = (true_pos + true_neg) / (true_pos+true_neg+false_pos+false_neg)
end_time=time.time()
print(f'Time taken: {end_time-start_time}\n')
print(f'Accuracy: {accuracy}')
accuracy_file.write(f'\n\nFinal Accuracy: {accuracy}\n')