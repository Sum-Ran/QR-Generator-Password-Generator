#!/usr/bin/env python
# coding: utf-8

# In[1]:


#to build the window where we generate a random password
from tkinter import * #Tkinter is a Graphical User Interface library

#random module generates the random numbers
#string module in python helps in creating and customizing strings
import random, string 

import pyperclip   #used for copying and pasting the text


# In[2]:


#Initialize Window

win = Tk()
win.geometry("500x500")  #to set width and height of window
win.title("Password Generator") 
win.configure(bg='#ffc252') #background color of window


# In[3]:


#Pack() function to arrange the widgets in the window
#ariel font with font size 15 in bold letters with same bg color
Label(win, text= 'Password Generator', font='ariel 15 bold', bg= "#ffc252").pack()


# In[4]:


pass_label = Label(win, text= 'Password Length', font='ariel 10 bold', bg="#ffc252").pack(pady=10)

#Using IntVar() function, we can set integer data as this function holds integer data
pass_len = IntVar()  

#Spinbox() provides a range of values for the user to input
#generates passwords from lengths 8 to 32.
length = Spinbox(win, from_=8, to_=32, textvariable= pass_len, width= 15).pack()


# In[5]:


#stringVar() function holds string data
pass_str = StringVar()

#defining a function Generator to generate random password
def Generator():
    password = " "
    
    #For the first four digits of the password, we set it to, a random uppercase letter, random lowercase letter, random digit, and random punctuation
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    
    #remaining values will be the random combination of uppercase, lowercase, digits, and punctuations.
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


# In[6]:


#Generate Buttons
Generate=Button(win, text = "GENERATE PASSWORD" , command = Generator,padx=5,pady=5 )
Generate.configure(background="blue", foreground='white',font=('ariel',10,'bold'))
Generate.pack(side=TOP,pady=20)
Entry(win , textvariable = pass_str).pack()


# In[7]:


#pyperclip to copy the password
def Copy_password():
    pyperclip.copy(pass_str.get())
copy=Button(win, text = 'COPY TO CLIPBOARD', command = Copy_password)
copy.configure(background="blue", foreground='white',font=('ariel',10,'bold'))
copy.pack(side=TOP,pady=20)


# In[8]:


#Final Execution
win.mainloop()

