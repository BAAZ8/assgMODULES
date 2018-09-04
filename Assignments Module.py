#Q.1- Print the current day using Datetime module.
print('Q.1- Print the current day using Datetime module.\n')
import datetime
print(datetime.datetime.now())




print('____________________')

#Q.2- Open your browser and play a video using webbrowser module in python.
print('Q.2- Open your browser and play a video using webbrowser module in python.')

import webbrowser
input('\tpress ENTER to open URL')
url="https://www.youtube.com/watch?v=tPMFAbhlDbU&index=14&t=0s&list=LLaJzHvjakNtAxxRqt6ficxw"
webbrowser.open_new(url)



print('____________________')

#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.
print('Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.')

import os
path = '/Users/Kanwal Sekhon/Desktop/3#/modules_ex'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1
