#receive input from cmd
My_Name = input("Please Enter your name \n")
My_Faculty = input("Please Enter your Faculty \n")
My_Age = input("Please Enter your Age \n")

f1 = open("My_Info.txt","a+") #open file and append to it
f1.write(My_Name)     #Append name to file
f1.write("\n")
f1.write(My_Faculty)  #Append Faculty to file
f1.write("\n")
f1.write(My_Age)      #Append Age to file
f1.write("\n")
f1.close()             #close file

f1 = open("My_Info.txt","r")  #open file and read from it
print("Your Info from File \n"+f1.read())

f1.close()