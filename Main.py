import csv
from ctypes.wintypes import SIZE
import os
import random
from tkinter import *

dictEnglish = []
dictThai = []

Dict = open('Dict.csv', 'r+', encoding='UTF-8')
csv_Reader = csv.reader(Dict, delimiter = ',')  
next(Dict)

for row in csv_Reader:
    English,Thai = row   
    dictEnglish.append(English)
    dictThai.append(Thai)

##print(dictEnglish)
##print(dictThai)

def delete():
    qWord.config(text="")
    aWord.config(text="")


def testMe():
    global temp
    questionString = random.choice(dictEnglish)
    qWord.config(text= questionString)
    Dict = open('Dict.csv', 'r+', encoding='UTF-8')
    csv_Reader = csv.reader(Dict, delimiter = ',')  
    next(Dict)
    for row in csv_Reader:
        English,Thai = row   
        if questionString == English:
            temp = Thai
    

def answer():
    aWord.config(text = temp)

root = Tk()
root.geometry("1080x600")
root.option_add("*font", "Arial 28")

qWord = Label(root, text="Question Here", font=("Arial", 70))
qWord.pack()

aWord = Label(root, text="Answer Here", font=("Arial", 70))
aWord.pack()

startButton = Button(root, text="Start" , fg="blue",command=testMe)##from tkinter import *
startButton.pack()
deleteButton = Button(root, text="Delete" , fg="red",command=delete)
deleteButton.pack()

Answer = Button(root, text="Answer" , fg="Black",command=answer)
Answer.pack()

##print(type(dictEnglish))
##print(random.choice(dictEnglish))


root.mainloop()