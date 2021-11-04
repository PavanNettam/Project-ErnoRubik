from tkinter import *
from tkmacosx import Button

root = Tk()

face1 = [
         [1,1,1],
         [1,1,1],
         [1,1,1]
         ]
face2 = [
         [2,2,2],
         [2,2,2],
         [2,2,2]
         ]
face3 = [
         [3,3,3],
         [3,3,3],
         [3,3,3]
         ]
face4 = [
         [4,4,4],
         [4,4,4],
         [4,4,4]
         ]
face5 = [
         [5,5,5],
         [5,5,5],
         [5,5,5]
         ]
face6 = [
         [6,6,6],
         [6,6,6],
         [6,6,6]
         ]

temp = Label(root,text="FACE1").grid(row = 0,column = 0,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            temp = Button(root,bg="white",padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j)
        
temp = Label(root,text=" ").grid(row = 0,column = 3)
temp = Label(root,text="FACE2").grid(row = 0,column = 4,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            temp = Button(root,bg="green",padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j+4)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j+4)

temp = Label(root,text="               ").grid(row = 0,column = 7)       
temp = Label(root,text="FACE3").grid(row = 0,column = 8,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            temp = Button(root,bg="yellow",padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j+8)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j+8)
        
temp = Label(root,text="FACE4").grid(row = 5,column = 0,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            temp = Button(root,bg="blue",padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j)

temp = Label(root,text=" ").grid(row = 5,column = 3)
temp = Label(root,text="FACE5").grid(row = 5,column = 4,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            temp = Button(root,bg="red",padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j+4)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j+4)

temp = Label(root,text="                 ").grid(row = 5,column = 7)
temp = Label(root,text="FACE6").grid(row = 5,column = 8,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            temp = Button(root,bg="orange",padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j+8)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j+8)

k = 1
i = 0
j = 0
temp = Label(root,text="something").grid(row = 9,column = 0,columnspan = 3,padx = 10,pady = 10)

def number(color):
    if color == "white":
        return 1
    elif color == "green":
        return 2
    elif color == "yellow":
        return 3
    elif color == "blue":
        return 4
    elif color == "red":
        return 5
    elif color == "orange":
        return 6
    elif color == "black":
        return 7
    
"""
The below function is named appender it does two tasks:
1. It adds colours to the black boxes of the GUI window
2. It changes the cube from solved configuration (default configuration) to current configuration
"""
                    
def appender(a):
    global k,i,j
    if a == "!":
        k -= 1
        if j == 0:
            i -= 1
            j = 2
        else:
            j -= 1
        appender("black")
        k -= 1
        if j == 0:
            i -= 1
            j = 2
        else:
            j -= 1
        return
    
    if k <= 9:
        temp = Button(root,bg=a,padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j)
        face1[i][j] = number(a)
        j += 1
        if j == 3:
            j = 0
            i += 1
        if i == 3:
            i = 0
        k += 1
        if j == 1 and i == 1:
            j += 1
            k += 1
        
    elif k <= 18:
        temp = Button(root,bg=a,padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j+4)
        face2[i][j] = number(a)
        j += 1
        if j == 3:
            j = 0
            i += 1
        if i == 3:
            i = 0
        k += 1
        if j == 1 and i == 1:
            j += 1
            k += 1
        
    elif k <= 27:
        temp = Button(root,bg=a,padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j+8)
        face3[i][j] = number(a)
        j += 1
        if j == 3:
            j = 0
            i += 1
        if i == 3:
            i = 0
        k += 1
        if j == 1 and i == 1:
            j += 1
            k += 1
            
    elif k <= 36:
        temp = Button(root,bg=a,padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j)
        face4[i][j] = number(a)
        j += 1
        if j == 3:
            j = 0
            i += 1
        if i == 3:
            i = 0
        k += 1
        if j == 1 and i == 1:
            j += 1
            k += 1
        
    elif k <= 45:
        temp = Button(root,bg=a,padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j+4)
        face5[i][j] = number(a)
        j += 1
        if j == 3:
            j = 0
            i += 1
        if i == 3:
            i = 0
        k += 1
        if j == 1 and i == 1:
            j += 1
            k += 1
        
    elif k <= 54:
        temp = Button(root,bg=a,padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j+8)
        face6[i][j] = number(a)
        j += 1
        if j == 3:
            j = 0
            i += 1
        if i == 3:
            i = 0
        k += 1
        if j == 1 and i == 1:
            j += 1
            k += 1
    
        
        
white = Button(root,bg="white",padx=10,pady=10,height=80,width=80,command=lambda: appender("white")).grid(row=10,column=0)
green = Button(root,bg="green",padx=10,pady=10,height=80,width=80,command=lambda: appender("green")).grid(row=10,column=1)
yellow = Button(root,bg="yellow",padx=10,pady=10,height=80,width=80,command=lambda: appender("yellow")).grid(row=10,column=2)
blue = Button(root,bg="blue",padx=10,pady=10,height=80,width=80,command=lambda: appender("blue")).grid(row=10,column=3)
red = Button(root,bg="red",padx=10,pady=10,height=80,width=80,command=lambda: appender("red")).grid(row=10,column=4)
orange = Button(root,bg="orange",padx=10,pady=10,height=80,width=80,command=lambda: appender("orange")).grid(row=10,column=5)
dele = Button(root,text="DEL",bg="grey",padx=10,pady=10,height=80,width=160,command=lambda: appender("!")).grid(row=10,column=6,columnspan=3)


nex = Button(root,text="NEXT",bg="grey",padx=10,pady=10,height=80,width=160).grid(row=10,column=9,columnspan=3)

root.mainloop()
from segement_y import *
from segement_x import *
'''
print(face1)
print(face2)
print(face3)
print(face4)
print(face5)
print(face6)
'''
