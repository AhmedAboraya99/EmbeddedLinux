# import only system from os
from os import system, name
 
# import sleep to show output for some time period
from time import sleep
 

def Arrow_DrawLeft():
    for i in range(11):
        print("\t\t\t\t\t\n",end="")
    #draw upper part
    for row in range(5):
        for e in range (row, 6, 1):
           print(" ",end="") 
        for a in range (row, 0,-1):
           print("<",end="")
        print("\n",end="")
    # draw middle part
    for m in range (40):
        print("<",end="")
    print("\n", end = "")
    #draw lower part
    for row in range(5):
        for e in range (row+1,0,-1):
            print(" ",end="")
        for a in range (row+1,6,1):
            print("<",end="")
        print("\n", end = "")
    sleep(1)
    system("cls")

def Arrow_DrawUp():
    print("\n\n\n",end="")
    #draw upper part
    for row in range(7):
        print("\t\t\t\t",end="")
        for e in range (6-row):
            print(" ",end="")
        for a in range ((row*2)-1):
            print("^",end="")
        print("\n", end = "")
    # draw middle part


    #draw lower part
    for row in range(7):
        print("\t\t\t\t",end="")
        print("    ",end="") 
        print("^^^",end="")
        print("\n",end="")
    sleep(1)
    system("cls")


def Arrow_DrawDown():
    print("\n\n\n\n\n",end="")
    for i in range(11):
        print("\t\t\t\t\t\n",end="")
    #draw upper part
    for row in range(7):
        print("\t\t\t\t",end="")
        print("     ",end="") 
        print("\|/",end="")
        print("\n",end="")
    # draw middle part

    #draw lower part
    for row in range(6):
        print("\t\t\t\t",end="")
        for e in range (row):
            print(" ",end="")
        for a in range (6-row):
           
            print("\/",end="")
        print("\n", end = "")
    sleep(1)
    system("cls")

def Arrow_DrawRight():
    for i in range(11):
        print("\t\t\t\t\t\n",end="")
    #draw upper part
    for row in range(5):
        print("\t\t\t\t\t",end="")
        print("\t\t\t\t",end="")
        for a in range (row+1):
           print(">",end="")
        print("\n",end="")
    # draw middle part
    print("\t\t\t\t\t",end="")
    for m in range (39):
        print(">",end="")
    print("\n", end = "")
    #draw lower part
    for row in range(5):
        print("\t\t\t\t\t",end="")
        print("\t\t\t\t",end="")
        for a in range (5,row,-1):
            print(">",end="")
        print("\n", end = "")

    sleep(1)
    system("cls")

while True:
    Arrow_DrawUp()
    Arrow_DrawRight()
    Arrow_DrawDown()
    Arrow_DrawLeft()