# type: ignore
import time #import time
x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0      #Declare point values

def Triangle(Inputv):
    try:
        listvalues = Inputv.split(",")  #split Inputed vaue
        x1 = float(listvalues[0])   #assign each input value its position according to the order of the number in the list
        x2 = float(listvalues[2])
        x3 = float(listvalues[4])
        y1 = float(listvalues[1])
        y2 = float(listvalues[3])
        y3 = float(listvalues[5])
        area = abs(x1*(y2-y3) + x2*(y3 - y1) + x3*(y1 - y2))*.5 #calculate triangle area
        return area
    except ValueError:  #bad triangle
        area = -1
        return area
while True:
    Inputv = input('Enter triangle points in x1,y2,x2,y2,x3,y3') #asks for user input
    PrintValue = Triangle(Inputv)
    if PrintValue > 0:  #state machine asking wether the value is 1:a triangle,2: A wrong user input or 3: correct triangle
        print(PrintValue)
    elif PrintValue == 0:
        print('not valid triangle')   
    elif PrintValue < 0:
        print('Worng user input')    