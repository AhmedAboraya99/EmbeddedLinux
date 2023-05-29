from tkinter import *

def ButtonPressTracker():
    ButtonPressTracker.counter += 1
    print("The Button Pressed", ButtonPressTracker.counter )
def ButtonPressName():
     print("Your name is Ahmed")
ButtonPressTracker.counter = 0
#construct main window through
window_1 = Tk()
#Name the window
window_1.title("Hello from tkinter")
#Add the label to the window

################################Controlling window geometery#########################################
# controlling window geometry in pixles 
window_1.geometry('1000x500')

Label_1 = Label(window_1, text = "Ahmed Calculator", font = ('Verdana', 10))
# using geomertry function to set the lable in a specific place [BOTTOM , LEFT , RIGHT] 
Label_1.pack(side = TOP)


# Adding a photo image object to use image 
CalcPhoto = PhotoImage(file='calculator.png')
# editing of the image resizing of it 
# resizing decreased by increasing the number 
CalcPhoto = CalcPhoto.subsample(10,10)

################################Adding widget [button] to the window ###############################
# Adding button to a specific window with a specific name and specific button name 

AddBut  =Button(window_1 , text = "Add",  bd = '5' , image = CalcPhoto,command = ButtonPressTracker)
AddBut.pack(side = TOP)
################################ Adding image to a button  ##########################################

SubBut  =Button(window_1 , text = "Sub")
SubBut.pack(side = LEFT)

MulBut  =Button(window_1 , text = "Mul", bd = 5, background="blue" , fg="white", command = ButtonPressName)
MulBut.pack(side = RIGHT)
# Adding button to a specific window with a specific name and specific button name 
################################Linking  widget [button] with actions ###############################
ResBut = Button(window_1, text = "Calculate", bd = '5', background="green" , fg="white", command = window_1.destroy)
ResBut.pack(side = BOTTOM)

################################     Usage of colours      ##########################################

# Call the main loop which is used when the application is ready to run to keep the code displaying 
window_1.mainloop()