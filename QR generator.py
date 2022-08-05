#!/usr/bin/env python
# coding: utf-8

# In[46]:


pip install pyqrcode 


# In[47]:


import pyqrcode  #to generating QR codes


# In[48]:


pip install pypng


# In[49]:


import png #to create a png file for the QR codes


# In[50]:


#changing folder location
import os
os.chdir("D:\Anaconda work")


# In[51]:


#QR Generation
link = "https://indianmemetemplates.com/wp-content/uploads/dekho-yeh-zinda-hai.jpg"
qr_code = pyqrcode.create(link)
qr_code.png("Scan if you are free.jpg",scale=10)
print(qr_code.terminal(module_color="white",background="black")) #to generate a QR code in the console itself

