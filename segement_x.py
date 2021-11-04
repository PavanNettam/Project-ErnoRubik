from tkinter import *
from tkmacosx import Button
root = Tk()
'''
face1 = [
         [3,1,4],               # face1 refers to white 
         [1,1,1],               # 1 = white
         [5,3,4]
         ]
face2 = [
         [1,1,6],               # face2 refers to green
         [5,2,2],               # 2 = green
         [1,6,2]
         ]
face3 = [
         [3,4,2],               # face3 refers to yellow
         [6,3,6],               # 3 = yellow
         [6,5,2]
         ]
face4 = [
         [3,5,4],               # face4 refers to blue
         [4,4,6],               # 4 = blue
         [1,3,3]
         ]
face5 = [
         [5,3,2],               # face5 refers to red
         [4,5,2],               # 5 = red
         [6,4,5]
         ]
face6 = [
         [4,5,6],               # face6 refers to orange
         [2,6,3],               # 6 = orange
         [5,2,1]
         ]
'''
face = [face1,face2,face3,face4,face5,face6]
#bt = Button(root,bg="yellow",padx=10,pady=10).grid(column=1,row=1)
def colour(a,b,c):
    if c == 1:
        face = face1
    elif c == 2:
        face = face2
    elif c == 3:
        face = face3
    elif c == 4:
        face = face4
    elif c == 5:
        face = face5
    elif c == 6:
        face = face6
        
    if face[a][b] == 1:
        return "white"
    elif face[a][b] == 2:
        return "green"
    elif face[a][b] == 3:
        return "yellow"
    elif face[a][b] == 4:
        return "blue"
    elif face[a][b] == 5:
        return "red"
    elif face[a][b] == 6:
        return "orange"

temp = Label(root,text="FACE1").grid(row = 0,column = 0,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        temp = Button(root,bg=colour(i,j,1),padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j)
        
temp = Label(root,text=" ").grid(row = 0,column = 3)
temp = Label(root,text="FACE2").grid(row = 0,column = 4,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        temp = Button(root,bg=colour(i,j,2),padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j+4)

temp = Label(root,text=" ").grid(row = 0,column = 7)       
temp = Label(root,text="FACE3").grid(row = 0,column = 8,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        temp = Button(root,bg=colour(i,j,3),padx=10,pady=10,height=80,width=80).grid(row=i+1,column=j+8)
        
temp = Label(root,text="FACE4").grid(row = 5,column = 0,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        temp = Button(root,bg=colour(i,j,4),padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j)

temp = Label(root,text=" ").grid(row = 5,column = 3)
temp = Label(root,text="FACE5").grid(row = 5,column = 4,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        temp = Button(root,bg=colour(i,j,5),padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j+4)

temp = Label(root,text=" ").grid(row = 5,column = 7)
temp = Label(root,text="FACE6").grid(row = 5,column = 8,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        temp = Button(root,bg=colour(i,j,6),padx=10,pady=10,height=80,width=80).grid(row=i+6,column=j+8)

root.mainloop()
