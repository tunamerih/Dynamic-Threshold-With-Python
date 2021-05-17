#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Word Yöntem 1

import cv2
import numpy 

test_image = cv2.imread("adaptive2.png") # windowsize_r = 36, C = 10
#test_image = cv2.imread("local_threshold_1.png") # windowsize_r = 3, C = 2
#test_image = cv2.imread("adaptive5.jpg") # windowsize_r = 6, C = 8
#test_image = cv2.imread("adaptive4.jpg") # windowsize_r = 6, C = 17

# Original image
orig_image = test_image.copy()

# Grayscale
test_image = cv2.cvtColor(test_image,cv2.COLOR_BGR2GRAY)

# finding global otsu value
ret_otsu,thresh_otsu = cv2.threshold(test_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# TH 127
ret,th127 = cv2.threshold(test_image,127,255,cv2.THRESH_BINARY)

a = test_image.shape
print(a)

# Define the window size and constant
windowsize_r = windowsize_c = 6
C = 17

# list of local threshold values
threshold_list = []

for r in range(0,test_image.shape[0] - windowsize_r, windowsize_r):
    for c in range(0,test_image.shape[1] - windowsize_c, windowsize_c):
        
        window = test_image[r:r+windowsize_r, c:c+windowsize_c]        
        local_thresh = numpy.round(numpy.sum(window)/windowsize_r**2) - C
        threshold_list.append(int(local_thresh))
        
        # static threshold ile
        ret,thresh1 = cv2.threshold(window,local_thresh,255,cv2.THRESH_BINARY)
        
        # gaussian blur ile
        #blur = cv2.GaussianBlur(window,(5,5),0)
        
        # otsu metodu ile
        #ret_otsu,thresh_otsu = cv2.threshold(window,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        # adaptive gaussian threshold ile
        #thresh1 = cv2.adaptiveThreshold(window,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        
        #birlestirme islemi
        test_image[r:r+windowsize_r, c:c+windowsize_c] = thresh1               
        
        #print(window)
        
cv2.imshow("orig_image",orig_image)
cv2.imshow("TH 127",th127)
cv2.imshow("Otsu",thresh_otsu)
cv2.imshow("Yontem 1",test_image)
cv2.waitKey(0)


# In[2]:


# Word Yöntem 2

import cv2
import numpy 

test_image = cv2.imread("adaptive2.png") # windowsize_r = 36, C = 10
#test_image = cv2.imread("local_threshold_1.png") # windowsize_r = 3, C = 2
#test_image = cv2.imread("adaptive4.jpg")
#test_image = cv2.imread("adaptive5.jpg")

# Morph islemleri icin kernel tanimlanir
#kernel = numpy.ones((7,7),numpy.uint8)  # dikdortgen
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(30,30)) # cember

#Original image
orig_image = test_image.copy()

# Grayscale
test_image = cv2.cvtColor(test_image,cv2.COLOR_BGR2GRAY)

# finding global otsu value
ret_otsu,thresh_otsu = cv2.threshold(test_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# TH 127
ret,th127 = cv2.threshold(test_image,127,255,cv2.THRESH_BINARY)

test_image_gray = test_image.copy()
test_image_gray_2 = test_image_gray.copy()

test_image_closing = cv2.morphologyEx(test_image_gray_2, cv2.MORPH_CLOSE, kernel)

test_image4 = test_image_gray/test_image_closing
#test_image5 = numpy.array(test_image4, dtype=numpy.uint8)

# c ve d iki ayrı normalizasyon işlemi [0,1] -> [0,255]
c = (255*(test_image4 - numpy.min(test_image4))/numpy.ptp(test_image4)).astype(int)
d = test_image4/(test_image4.max()/255.0)
# c2 ve d2 uint8 e donusturur
d2 =  numpy.array(d, dtype=numpy.uint8)
c2 = numpy.array(c, dtype=numpy.uint8)

print(test_image4)
print("****")

print(c)
print(d)

ret,otsu = cv2.threshold(c2, 0,255, cv2.THRESH_OTSU)
ret,static_thresh = cv2.threshold(test_image4,0.8,1,cv2.THRESH_BINARY)


'''
with open("output.txt", "w") as txt_file:
    for line in test_image3:
        txt_file.write(" ".join(str(line))+ "\n") 
'''      


cv2.imshow("orig_image",orig_image)
cv2.imshow("TH 127",th127)
cv2.imshow("Otsu",thresh_otsu)
cv2.imshow("Yontem 2 sonrasi statik_thresh",static_thresh)
cv2.imshow("Yontem 2 sonrasi Otsu",otsu)
cv2.waitKey(0)


# In[ ]:




