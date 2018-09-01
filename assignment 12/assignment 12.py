#Q.1- Print the current day using Datetime module.
import datetime
day = datetime.datetime.now()
print("today is "+day.strftime("%A")) #%A prints the current weekday 


#Q.2- Open your browser and play a video using webbrowser module in python.\
import webbrowser as web
web.open_new_tab("https://www.youtube.com/watch?v=y03u_QlI2gM")


#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format
import os

path = 'C:\\Users\\Pranav\\Desktop\\assignment'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, 'changed'+str(i)+'.jpg'))
    i = i+1
