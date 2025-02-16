#!/usr/bin/env python
# coding: utf-8

# # image process(edge detect,image translate,image rotate)

# In[1]:


import cv2


# # Detection Edges

# In[2]:


fname="img.jpg"
try:
    img=cv2.imread(fname)
    edges=cv2.Canny(img,100,200) #canny is a function use to translate image
    cv2.imwrite("ImageEdges.jpg",edges)
    print("DONEE")
except IOError:
    print("File Not Found")


# # Scaling

# In[3]:


fname="img.jpg"
try:
    img=cv2.imread(fname)
    (h,w)=img.shape[:2]
    res=cv2.resize(img,(int(w/2),int(h/2)),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("ScaleImg.jpg",res)
    print("DONEE")
except IOError:
    print("File Not Found")


# # Visualizing the different channels of Image

# In[4]:


fname="img.jpg"
img=cv2.imread(fname)
B,G,R=cv2.split(img)
cv2.imshow("Original",img)
cv2.waitKey(0)

cv2.imshow("Blue Image",B)
cv2.waitKey(0)

cv2.imshow("Green Image",G)
cv2.waitKey(0)

cv2.imshow("Red Image",R)
cv2.waitKey(0)

cv2.destroyAllWindows() 


# # Image Pyramid

# In[4]:


import matplotlib.pyplot as plt


# In[5]:


img=cv2.imread("img.jpg")
layer=img.copy()
for i in range(4):
    plt.subplot(2,2,i+1)
    layer=cv2.pyrDown(layer)
    plt.imshow(layer)
    cv2.imshow("Image",layer)
    cv2.waitKey(0)
cv2.destroyAllWindows()    


# In[2]:


import cv2
import numpy as np


# In[5]:


image=cv2.imread("img.jpg")
cv2.imshow("Original Image",image)
cv2.waitKey(0)

#Gaussian blur
Gaussian=cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("Gaussian Image",Gaussian)
cv2.waitKey(0)

#Median blur
Median=cv2.medianBlur(image ,5)
cv2.imshow("Median Image",Median)
cv2.waitKey(0)

#Bilateral blur
Bilateral=cv2.bilateralFilter(image ,9,75,57)
cv2.imshow("Bilateral Image",Bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()


# # Image Border

# In[12]:


image=cv2.imread("img.jpg")
borderimage=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_CONSTANT,value=[255,0,0])
cv2.imwrite("Border Image.jpg",borderimage)
print("DONEE")


# # Image border reflect
# 

# In[13]:


image=cv2.imread("img.jpg")
borderimage=cv2.copyMakeBorder(image,100,100,50,50,cv2.BORDER_REFLECT)
cv2.imwrite("Border_REFLECT_Image.jpg",borderimage)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[16]:


image=cv2.imread("scen.jpg")
borderimage=cv2.copyMakeBorder(image,100,100,50,50,cv2.BORDER_REFLECT)
cv2.imwrite("REFLECT_Image.png",borderimage)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # image rotation
# 

# In[23]:


fname="scen.jpg"
try:
    image=cv2.imread(fname)
    (r,c)=image.shape[:2]
    M=cv2.getRotationMatrix2D((c/2,r/2),280,1)
    res=cv2.warpAffine(image,M,(c,r))
    cv2.imshow("Rotate Image",res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except IOError:
    print("ERROR")
    cv2.destroyAllWindows()


# # Image Plots

# In[24]:


import matplotlib.pyplot as plt


# In[26]:


image=cv2.imread("scen.jpg",0)
plt.hist(image.ravel(),256,[0,256])
plt.show()


# In[ ]:




