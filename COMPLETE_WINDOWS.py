from tkinter import *
#from tkmacosx import Button
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
            temp = Button(root,bg="white",padx=10,pady=10,height=3,width=6).grid(row=i+1,column=j)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=3,width=6).grid(row=i+1,column=j)
        
temp = Label(root,text=" ").grid(row = 0,column = 3)
temp = Label(root,text="FACE2").grid(row = 0,column = 4,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            temp = Button(root,bg="green",padx=10,pady=10,height=3,width=6).grid(row=i+1,column=j+4)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=3,width=6).grid(row=i+1,column=j+4)

temp = Label(root,text="               ").grid(row = 0,column = 7)       
temp = Label(root,text="FACE3").grid(row = 0,column = 8,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            temp = Button(root,bg="yellow",padx=10,pady=10,height=3,width=6).grid(row=i+1,column=j+8)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=3,width=6).grid(row=i+1,column=j+8)
        
temp = Label(root,text="FACE4").grid(row = 5,column = 0,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            temp = Button(root,bg="blue",padx=10,pady=10,height=3,width=6).grid(row=i+6,column=j)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=3,width=6).grid(row=i+6,column=j)

temp = Label(root,text=" ").grid(row = 5,column = 3)
temp = Label(root,text="FACE5").grid(row = 5,column = 4,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            temp = Button(root,bg="red",padx=10,pady=10,height=3,width=6).grid(row=i+6,column=j+4)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=3,width=6).grid(row=i+6,column=j+4)

temp = Label(root,text="                 ").grid(row = 5,column = 7)
temp = Label(root,text="FACE6").grid(row = 5,column = 8,columnspan = 3,padx = 10,pady = 10)
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            temp = Button(root,bg="orange",padx=10,pady=10,height=3,width=6).grid(row=i+6,column=j+8)
        else:
            temp = Button(root,bg="black",padx=10,pady=10,height=3,width=6).grid(row=i+6,column=j+8)

k = 1
i = 0
j = 0
temp = Label(root,text="Enter the colours as on the Rubics Cube").grid(row = 9,column = 0,columnspan = 4,padx = 10,pady = 10)

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
        temp = Button(root,bg=a,padx=10,pady=10,height=3,width=6).grid(row=i+1,column=j)
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
        temp = Button(root,bg=a,padx=10,pady=10,height=3,width=6).grid(row=i+1,column=j+4)
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
        temp = Button(root,bg=a,padx=10,pady=10,height=3,width=6).grid(row=i+1,column=j+8)
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
        temp = Button(root,bg=a,padx=10,pady=10,height=3,width=6).grid(row=i+6,column=j)
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
        temp = Button(root,bg=a,padx=10,pady=10,height=3,width=6).grid(row=i+6,column=j+4)
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
        temp = Button(root,bg=a,padx=10,pady=10,height=3,width=6).grid(row=i+6,column=j+8)
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
    
def inputit():
    """ PROJECT-ERNO_RUBIC """
    
    ''' In this project efforts are made to create a virtual RUBIC's CUBE '''
    
    ''' And thereby teach machine to solve it '''
    
    
    
    ''' Defining the cube '''
    
    #from tkinter import *
    
    #from tkmacosx import Button
    
    root = Tk()
    
    #x = 0
    
    
    
    # Defining Faces(colours)
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
    # Defining Movements

    # NOTE: All the movements are defined with respect to default position

    # Default position is WHITE TOWARD US RED TOP position

    # There are overall 12 movements, which are defined as follows:

    
    temp = Label(root,text="ERNO RUBIC'S CUBE").grid(row=0,column=0,columnspan=3)
    temp = Label(root,text="PRESS 1 -RIGHT SIDE UP").grid(row=1,column=0,columnspan=3)
    temp = Label(root,text="PRESS 2 -RIGHT SIDE DOWN").grid(row=2,column=0,columnspan=3)
    temp = Label(root,text="PRESS 3 -LEFT SIDE UP").grid(row=3,column=0,columnspan=3)
    temp = Label(root,text="PRESS 4 -LEFT SIDE DOWN").grid(row=4,column=0,columnspan=3)
    temp = Label(root,text="PRESS 5 -TOP FACE LEFT").grid(row=5,column=0,columnspan=3)
    temp = Label(root,text="PRESS 6 -TOP FACE RIGHT").grid(row=6,column=0,columnspan=3)
    temp = Label(root,text="PRESS 7 -BOTTOM FACE LEFT").grid(row=7,column=0,columnspan=3)
    temp = Label(root,text="PRESS 8 -BOTTOM FACE RIGHT").grid(row=8,column=0,columnspan=3)
    temp = Label(root,text="PRESS 9 -FRONT FACE CLOCKWISE").grid(row=9,column=0,columnspan=3)
    temp = Label(root,text="PRESS 10 -FRONT FACE ANTICLOCKWISE").grid(row=10,column=0,columnspan=3)
    temp = Label(root,text="PRESS 11 -BACK FACE CLOCKWISE").grid(row=11,column=0,columnspan=3)
    temp = Label(root,text="PRESS 12 -BACK FACE ANTICLOCKWISE").grid(row=12,column=0,columnspan=3)
    temp = Label(root,text="PRESS 'GENERATE OUTPUT' -TO SEE THE RESULT").grid(row=14,column=0,columnspan=3)


    def right_up():#1

        

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

        temp = Label(root,text="RIGHT SIDE UP worked").grid(row=15,column=0,columnspan=3)

    

    def right_down():#2

        #x += 1

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

        temp = Label(root,text="RIGHT SIDE DOWN worked").grid(row=16,column=0,columnspan=3)

    

    

    def left_up():#3

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

        temp = Label(root,text="LEFT SIDE UP worked").grid(row=17,column=0,columnspan=3)



    def left_down():#4

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
     
        temp = Label(root,text="LEFT SIDE DOWN worked").grid(row=18,column=0,columnspan=3)



    def top_left():#5

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

        temp = Label(root,text="TOP FACE LEFT worked").grid(row=19,column=0,columnspan=3)



    def top_right():#6

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

        temp = Label(root,text="TOP FACE RIGHT worked").grid(row=20,column=0,columnspan=3)



    def bottom_left():#7

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

        temp = Label(root,text="BOTTOM FACE LEFT worked").grid(row=21,column=0,columnspan=3)



    def bottom_right():#8

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

        temp = Label(root,text="BOTTOM FACE RIGHT worked").grid(row=22,column=0,columnspan=3)



    def front_clock():#9

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

        temp = Label(root,text="FRONT FACE CLOCKWISE worked").grid(row=23,column=0,columnspan=3)

    

    def front_anti():#10

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

        temp = Label(root,text="FRONT FACE ANTICLOCKWISE worked").grid(row=24,column=0,columnspan=3)



    def back_clock():#11

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
 
        temp = Label(root,text="BACK FACE CLOCKWISE worked").grid(row=25,column=0,columnspan=3)



    def back_anti():#12

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

        temp = Label(root,text="BACK FACE ANTICLOCKWISE worked").grid(row=26,column=0,columnspan=3)



    m1 = right_up
 
    m2 = right_down

    m3 = left_up

    m4 = left_down

    m5 = top_left

    m6 = top_right
  
    m7 = bottom_left

    m8 = bottom_right

    m9 = front_clock

    m10 = front_anti

    m11 = back_clock

    m12 = back_anti

    move = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]

    j = 0



    for i in move:

        temp = Button(root,text = j+1,height = 4,width = 8,padx = 10,pady = 10,command = i).grid(row = 13,column = j)

        j += 1

    def outt():
        #import segement_x
        #from tkinter import *
        #from tkmacosx import Button
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
                temp = Button(root,bg=colour(i,j,1),padx=10,pady=10,height=4,width=8).grid(row=i+1,column=j)
        
        temp = Label(root,text=" ").grid(row = 0,column = 3)
        temp = Label(root,text="FACE2").grid(row = 0,column = 4,columnspan = 3,padx = 10,pady = 10)
        for i in range(3):
             for j in range(3):
                temp = Button(root,bg=colour(i,j,2),padx=10,pady=10,height=4,width=8).grid(row=i+1,column=j+4)
     
        temp = Label(root,text=" ").grid(row = 0,column = 7)       
        temp = Label(root,text="FACE3").grid(row = 0,column = 8,columnspan = 3,padx = 10,pady = 10)
        for i in range(3):
            for j in range(3):
                temp = Button(root,bg=colour(i,j,3),padx=10,pady=10,height=4,width=8).grid(row=i+1,column=j+8)
            
        temp = Label(root,text="FACE4").grid(row = 5,column = 0,columnspan = 3,padx = 10,pady = 10)
        for i in range(3):
            for j in range(3):
                temp = Button(root,bg=colour(i,j,4),padx=10,pady=10,height=4,width=8).grid(row=i+6,column=j)

        temp = Label(root,text=" ").grid(row = 5,column = 3)
        temp = Label(root,text="FACE5").grid(row = 5,column = 4,columnspan = 3,padx = 10,pady = 10)
        for i in range(3):
            for j in range(3):
                temp = Button(root,bg=colour(i,j,5),padx=10,pady=10,height=4,width=8).grid(row=i+6,column=j+4)
 
        temp = Label(root,text=" ").grid(row = 5,column = 7)
        temp = Label(root,text="FACE6").grid(row = 5,column = 8,columnspan = 3,padx = 10,pady = 10)
        for i in range(3):
            for j in range(3):
                temp = Button(root,bg=colour(i,j,6),padx=10,pady=10,height=4,width=8).grid(row=i+6,column=j+8)

        root.mainloop()


    temp = Button(root,text="Genarate Output",height = 4,width =12 ,padx = 10,pady = 10,command=outt).grid(row = 14,column = j,columnspan = 3)
        
    root.mainloop()        
        
white = Button(root,bg="white",padx=10,pady=10,height=3,width=6,command=lambda: appender("white")).grid(row=10,column=0)
green = Button(root,bg="green",padx=10,pady=10,height=3,width=6,command=lambda: appender("green")).grid(row=10,column=1)
yellow = Button(root,bg="yellow",padx=10,pady=10,height=3,width=6,command=lambda: appender("yellow")).grid(row=10,column=2)
blue = Button(root,bg="blue",padx=10,pady=10,height=3,width=6,command=lambda: appender("blue")).grid(row=10,column=3)
red = Button(root,bg="red",padx=10,pady=10,height=3,width=6,command=lambda: appender("red")).grid(row=10,column=4)
orange = Button(root,bg="orange",padx=10,pady=10,height=3,width=6,command=lambda: appender("orange")).grid(row=10,column=5)
dele = Button(root,text="DEL",bg="grey",padx=10,pady=10,height=4,width=16,command=lambda: appender("!")).grid(row=10,column=6,columnspan=3)
nex = Button(root,text="NEXT",bg="grey",padx=10,pady=10,height=4,width=16,command=inputit).grid(row=10,column=9,columnspan=3)

#root.mainloop()
'''
print(face1)
print(face2)
print(face3)
print(face4)
print(face5)
print(face6)
'''


root.mainloop()

