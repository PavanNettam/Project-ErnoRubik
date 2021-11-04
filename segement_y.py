

""" PROJECT-ERNO_RUBIC """
''' In this project efforts are made to create a virtual RUBIC's CUBE '''
''' And thereby teach machine to solve it '''

''' Defining the cube '''
from tkinter import *
from tkmacosx import Button
root = Tk()
#x = 0

# Defining Faces(colours)
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

# Defining Movements
# NOTE: All the movements are defined with respect to default position
# Default position is WHITE TOWARD US RED TOP position
# There are overall 12 movements, which are defined as follows:
    
def right_up():#1
    global x
    x += 1
    temp1,temp2,temp3 = face1[0][2],face1[1][2],face1[2][2]
    face1[0][2],face1[1][2],face1[2][2] = face6[0][2],face6[1][2],face6[2][2]
    face6[0][2],face6[1][2],face6[2][2] = face3[2][0],face3[1][0],face3[0][0]
    face3[2][0],face3[1][0],face3[0][0] = face5[0][2],face5[1][2],face5[2][2]
    face5[0][2],face5[1][2],face5[2][2] = temp1,temp2,temp3 
    # The above code is to change last column elements of face1,3,5,6 cyclically up
     
    # Performing "square corner movement-clockwise" of face2 
    temp = face2[0][0]
    face2[0][0] = face2[2][0]
    face2[2][0] = face2[2][2]
    face2[2][2] = face2[0][2]
    face2[0][2] = temp
    
    # Performing "Diamond corner movement-clockwise" of face2 
    temp = face2[0][1]
    face2[0][1] = face2[1][0]
    face2[1][0] = face2[2][1]
    face2[2][1] = face2[1][2]
    face2[1][2] = temp
    temp = Label(root,text="RIGHT SIDE UP worked").grid(row=x,column=0,columnspan=3)
    
def right_down():#2
    global x
    x += 1
    temp1,temp2,temp3 = face1[0][2],face1[1][2],face1[2][2]
    face1[0][2],face1[1][2],face1[2][2] = face5[0][2],face5[1][2],face5[2][2]
    face5[0][2],face5[1][2],face5[2][2] = face3[2][0],face3[1][0],face3[0][0]
    face3[2][0],face3[1][0],face3[0][0] = face6[0][2],face6[1][2],face6[2][2]
    face6[0][2],face6[1][2],face6[2][2] = temp1,temp2,temp3 
    # The above code is to change last column elements of face1,3,5,6 cyclically down
     
    # Performing "square corner movement-anticlockwise" of face2 
    temp = face2[0][0]
    face2[0][0] = face2[0][2]
    face2[0][2] = face2[2][2]
    face2[2][2] = face2[2][0]
    face2[2][0] = temp
    
    # Performing "Diamond corner movement-anticlockwise" of face2 
    temp = face2[0][1]
    face2[0][1] = face2[1][2]
    face2[1][2] = face2[2][1]
    face2[2][1] = face2[1][0]
    face2[1][0] = temp
    temp = Label(root,text="RIGHT SIDE DOWN worked").grid(row=x,column=0,columnspan=3)
    
    
def left_up():#3
    global x
    x += 1
    temp1,temp2,temp3 = face1[0][0],face1[1][0],face1[2][0]
    face1[0][0],face1[1][0],face1[2][0] = face6[0][0],face6[1][0],face6[2][0]
    face6[0][0],face6[1][0],face6[2][0] = face3[2][2],face3[1][2],face3[0][2]
    face3[2][2],face3[1][2],face3[0][2] = face5[0][0],face5[1][0],face5[2][0]
    face5[0][0],face5[1][0],face5[2][0] = temp1,temp2,temp3 
    # The above code is to change first column elements of face1,3,5,6 cyclically up
     
     # Performing "square corner movement-anticlockwise" of face4
    temp = face4[0][0]
    face4[0][0] = face4[0][2]
    face4[0][2] = face4[2][2]
    face4[2][2] = face4[2][0]
    face4[2][0] = temp
    
    # Performing "Diamond corner movement-anticlockwise" of face4
    temp = face4[0][1]
    face4[0][1] = face4[1][2]
    face4[1][2] = face4[2][1]
    face4[2][1] = face4[1][0]
    face4[1][0] = temp
    temp = Label(root,text="LEFT SIDE UP worked").grid(row=x,column=0,columnspan=3)

def left_down():#4
    global x
    x += 1
    temp1,temp2,temp3 = face1[0][0],face1[1][0],face1[2][0]
    face1[0][0],face1[1][0],face1[2][0] = face5[0][0],face5[1][0],face5[2][0]
    face5[0][0],face5[1][0],face5[2][0] = face3[2][2],face3[1][2],face3[0][2]
    face3[2][2],face3[1][2],face3[0][2] = face6[0][0],face6[1][0],face6[2][0]
    face6[0][0],face6[1][0],face6[2][0] = temp1,temp2,temp3 
    # The above code is to change last column elements of face1,3,5,6 cyclically down

    # Performing "square corner movement-clockwise" of face4 
    temp = face4[0][0]
    face4[0][0] = face4[2][0]
    face4[2][0] = face4[2][2]
    face4[2][2] = face4[0][2]
    face4[0][2] = temp
    
    # Performing "Diamond corner movement-clockwise" of face4
    temp = face4[0][1]
    face4[0][1] = face4[1][0]
    face4[1][0] = face4[2][1]
    face4[2][1] = face4[1][2]
    face4[1][2] = temp
    temp = Label(root,text="LEFT SIDE DOWN worked").grid(row=x,column=0,columnspan=3)

def top_left():#5
    global x
    x += 1
    temp1,temp2,temp3 = face1[0][0],face1[0][1],face1[0][2]
    face1[0][0],face1[0][1],face1[0][2] = face2[0][0],face2[0][1],face2[0][2]
    face2[0][0],face2[0][1],face2[0][2] = face3[0][0],face3[0][1],face3[0][2]
    face3[0][0],face3[0][1],face3[0][2] = face4[0][0],face4[0][1],face4[0][2]
    face4[0][0],face4[0][1],face4[0][2] = temp1,temp2,temp3 
    # The above code is to change first row elements of face1,2,3,4 cyclically left
     
    # Performing "square corner movement-clockwise" of face5 
    temp = face5[0][0]
    face5[0][0] = face5[2][0]
    face5[2][0] = face5[2][2]
    face5[2][2] = face5[0][2]
    face5[0][2] = temp
    
    # Performing "Diamond corner movement-clockwise" of face2 
    temp = face5[0][1]
    face5[0][1] = face5[1][0]
    face5[1][0] = face5[2][1]
    face5[2][1] = face5[1][2]
    face5[1][2] = temp
    temp = Label(root,text="TOP TOWORDS LEFT worked").grid(row=x,column=0,columnspan=3)

def top_right():#6
    global x
    x += 1
    temp1,temp2,temp3 = face1[0][0],face1[0][1],face1[0][2]
    face1[0][0],face1[0][1],face1[0][2] = face4[0][0],face4[0][1],face4[0][2]
    face4[0][0],face4[0][1],face4[0][2] = face3[0][0],face3[0][1],face3[0][2]
    face3[0][0],face3[0][1],face3[0][2] = face2[0][0],face2[0][1],face2[0][2]
    face2[0][0],face2[0][1],face2[0][2] = temp1,temp2,temp3 
    # The above code is to change first row elements of face1,2,3,4 cyclically right
     
    # Performing "square corner movement-anticlockwise" of face5
    temp = face5[0][0]
    face5[0][0] = face5[0][2]
    face5[0][2] = face5[2][2]
    face5[2][2] = face5[2][0]
    face5[2][0] = temp
    
    # Performing "Diamond corner movement-anticlockwise" of face5 
    temp = face5[0][1]
    face5[0][1] = face5[1][2]
    face5[1][2] = face5[2][1]
    face5[2][1] = face5[1][0]
    face5[1][0] = temp
    temp = Label(root,text="TOP TOWARDS RIGHT worked").grid(row=x,column=0,columnspan=3)

def bottom_left():#7
    global x
    x += 1
    temp1,temp2,temp3 = face1[2][0],face1[2][1],face1[2][2]
    face1[2][0],face1[2][1],face1[2][2] = face2[2][0],face2[2][1],face2[2][2]
    face2[2][0],face2[2][1],face2[2][2] = face3[2][0],face3[2][1],face3[2][2]
    face3[2][0],face3[2][1],face3[2][2] = face4[2][0],face4[2][1],face4[2][2]
    face4[2][0],face4[2][1],face4[2][2] = temp1,temp2,temp3 
    # The above code is to change last row elements of face1,2,3,4 cyclically left
     
    # Performing "square corner movement-anticlockwise" of face6 
    temp = face6[0][0]
    face6[0][0] = face6[0][2]
    face6[0][2] = face6[2][2]
    face6[2][2] = face6[2][0]
    face6[2][0] = temp
    
    # Performing "Diamond corner movement-anticlockwise" of face6
    temp = face6[0][1]
    face6[0][1] = face6[1][2]
    face6[1][2] = face6[2][1]
    face6[2][1] = face6[1][0]
    face6[1][0] = temp
    temp = Label(root,text="BOTTON TOWARDS LEFT worked").grid(row=x,column=0,columnspan=3)

def bottom_right():#8
    global x
    x += 1
    temp1,temp2,temp3 = face1[2][0],face1[2][1],face1[2][2]
    face1[2][0],face1[2][1],face1[2][2] = face4[2][0],face4[2][1],face4[2][2]
    face4[2][0],face4[2][1],face4[2][2] = face3[2][0],face3[2][1],face3[2][2]
    face3[2][0],face3[2][1],face3[2][2] = face2[2][0],face2[2][1],face2[2][2]
    face2[2][0],face2[2][1],face2[2][2] = temp1,temp2,temp3 
    # The above code is to change last row elements of face1,2,3,4 cyclically right
     
    # Performing "square corner movement-clockwise" of face6 
    temp = face6[0][0]
    face6[0][0] = face6[2][0]
    face6[2][0] = face6[2][2]
    face6[2][2] = face6[0][2]
    face6[0][2] = temp
    
    # Performing "Diamond corner movement-clockwise" of face6
    temp = face6[0][1]
    face6[0][1] = face6[1][0]
    face6[1][0] = face6[2][1]
    face6[2][1] = face6[1][2]
    face6[1][2] = temp
    temp = Label(root,text="BOTTON TOWARDS RIGHT worked").grid(row=x,column=0,columnspan=3)

def front_clock():#9
    global x
    x += 1
    temp1,temp2,temp3 = face5[2][0],face5[2][1],face5[2][2]
    face5[2][0],face5[2][1],face5[2][2] = face4[2][2],face4[1][2],face4[0][2]
    face4[0][2],face4[1][2],face4[2][2] = face6[0][0],face6[0][1],face6[0][2]
    face6[0][0],face6[0][1],face6[0][2] = face2[2][0],face2[1][0],face2[0][0]
    face2[0][0],face2[1][0],face2[2][0] = temp1,temp2,temp3 
    # The above code is to turn front clockwise
    
     # Performing "square corner movement-clockwise" of face1
    temp = face1[0][0]
    face1[0][0] = face1[2][0]
    face1[2][0] = face1[2][2]
    face1[2][2] = face1[0][2]
    face1[0][2] = temp
    
    # Performing "Diamond corner movement-clockwise" of face1
    temp = face1[0][1]
    face1[0][1] = face1[1][0]
    face1[1][0] = face1[2][1]
    face1[2][1] = face1[1][2]
    face1[1][2] = temp
    temp = Label(root,text="FRONT CLOCKWISE worked").grid(row=x,column=0,columnspan=3)
    
def front_anti():#10
    global x
    x += 1
    temp1,temp2,temp3 = face5[2][0],face5[2][1],face5[2][2]
    face5[2][0],face5[2][1],face5[2][2] = face2[0][0],face2[1][0],face2[2][0]
    face2[2][0],face2[1][0],face2[0][0] = face6[0][0],face6[0][1],face6[0][2]
    face6[0][0],face6[0][1],face6[0][2] = face4[0][2],face4[1][2],face4[2][2]
    face4[0][2],face4[1][2],face4[2][2] = temp3,temp2,temp1 
    # The above code is to turn front anti-clockwise
    
    # Performing "square corner movement-anticlockwise" of face1
    temp = face1[0][0]
    face1[0][0] = face1[0][2]
    face1[0][2] = face1[2][2]
    face1[2][2] = face1[2][0]
    face1[2][0] = temp
    
    # Performing "Diamond corner movement-anticlockwise" of face6
    temp = face1[0][1]
    face1[0][1] = face1[1][2]
    face1[1][2] = face1[2][1]
    face1[2][1] = face1[1][0]
    face1[1][0] = temp
    temp = Label(root,text="FRONT ANTI-CLOCKWISE worked").grid(row=x,column=0,columnspan=3)

def back_clock():#11
    global x
    x += 1
    temp1,temp2,temp3 = face5[0][0],face5[0][1],face5[0][2]
    face5[0][0],face5[0][1],face5[0][2] = face4[2][0],face4[1][0],face4[0][0]
    face4[0][0],face4[1][0],face4[2][0] = face6[2][0],face6[2][1],face6[2][2]
    face6[2][0],face6[2][1],face6[2][2] = face2[2][2],face2[1][2],face2[0][2]
    face2[0][2],face2[1][2],face2[2][2] = temp1,temp2,temp3 
    # The above code is to turn back clockwise
    
    # Performing "square corner movement-anticlockwise" of face3
    temp = face3[0][0]
    face3[0][0] = face3[0][2]
    face3[0][2] = face3[2][2]
    face3[2][2] = face3[2][0]
    face3[2][0] = temp
    
    # Performing "Diamond corner movement-anticlockwise" of face3
    temp = face3[0][1]
    face3[0][1] = face3[1][2]
    face3[1][2] = face3[2][1]
    face3[2][1] = face3[1][0]
    face3[1][0] = temp
    temp = Label(root,text="BACK CLOCKWISE worked").grid(row=x,column=0,columnspan=3)

def back_anti():#12
    global x
    x += 1
    temp1,temp2,temp3 = face5[0][0],face5[0][1],face5[0][2]
    face5[0][0],face5[0][1],face5[0][2] = face2[0][2],face2[1][2],face2[2][2]
    face2[0][2],face2[1][2],face2[2][2] = face6[2][2],face6[2][1],face6[2][0]
    face6[2][0],face6[2][1],face6[2][2] = face4[0][0],face4[1][0],face4[2][0]
    face4[0][0],face4[1][0],face4[2][0] = temp3,temp2,temp1
    # The above code is to turn back anti-clockwise

    # Performing "square corner movement-clockwise" of face3 
    temp = face3[0][0]
    face3[0][0] = face3[2][0]
    face3[2][0] = face3[2][2]
    face3[2][2] = face3[0][2]
    face3[0][2] = temp
    
    # Performing "Diamond corner movement-clockwise" of face3
    temp = face3[0][1]
    face3[0][1] = face3[1][0]
    face3[1][0] = face3[2][1]
    face3[2][1] = face3[1][2]
    face3[1][2] = temp
    temp = Label(root,text="BACK ANTI-CLOCKWISE worked").grid(row=x,column=0,columnspan=3)

x = 0
bt1 = Button(root,text = "1",height = 60,width = 60,padx = 10,pady = 10,command = right_up).grid(row = 0,column = 0)
bt2 = Button(root,text = "2",height = 60,width = 60,padx = 10,pady = 10,command = right_down).grid(row = 0,column = 1)
bt3 = Button(root,text = "3",height = 60,width = 60,padx = 10,pady = 10,command = left_up).grid(row = 0,column = 2)
bt4 = Button(root,text = "4",height = 60,width = 60,padx = 10,pady = 10,command = left_down).grid(row = 0,column = 3)
bt5 = Button(root,text = "5",height = 60,width = 60,padx = 10,pady = 10,command = top_left).grid(row = 0,column = 4)
bt6 = Button(root,text = "6",height = 60,width = 60,padx = 10,pady = 10,command = top_right).grid(row = 0,column = 5)
bt7 = Button(root,text = "7",height = 60,width = 60,padx = 10,pady = 10,command = bottom_left).grid(row = 0,column = 6)
bt8 = Button(root,text = "8",height = 60,width = 60,padx = 10,pady = 10,command = bottom_right).grid(row = 0,column = 7)
bt9 = Button(root,text = "9",height = 60,width = 60,padx = 10,pady = 10,command = front_clock).grid(row = 0,column = 8)
bt10 = Button(root,text = "10",height = 60,width = 60,padx = 10,pady = 10,command = front_anti).grid(row = 0,column = 9)
bt11 = Button(root,text = "11",height = 60,width = 60,padx = 10,pady = 10,command = back_clock).grid(row = 0,column = 10)
bt12 = Button(root,text = "12",height = 60,width = 60,padx = 10,pady = 10,command = back_anti).grid(row = 0,column = 11)


output = Button(root,text="Genarate Output",height = 60,width = 150,padx = 10,pady = 10).grid(row = 0,column = 12,columnspan = 3)
root.mainloop()
