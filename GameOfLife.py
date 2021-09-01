from tkinter import *
import tkinter
import time
 
window = Tk()
window.title("Game of Life")
window.resizable(width=False, height=False)
window.geometry("800x900")
window.update()
#-------------V-----------------#
celldensity = 30
activecolor = "black"
#-------------------------------#
#Live Cell   >2 live neighbours dies
#Live Cell   =2 or 3 neighbours lives
#Live Cell   <3 live neighbours dies
#Dead Cell   =3 live neighbours lives
#-------------------------------------------------------------------------------------------------------# 
 
def NextGeneration(sender):
    if (sender == "ForwardButton" and automaticgo.cget('text') == ">>") or (sender == "Automatic" and automaticgo.cget('text') == "="):
        generationlabel.config( text= "Generation "+  str( int( generationlabel.cget('text').split(" ",1)[1])+1))
        alivelist = []
        deadlist = []                   
        indexpositions = [  [-1,-1],   [0,-1],   [1,-1],
                            [-1,0],              [1,0],
                            [-1,1],    [0,1],    [1,1]   ]
        for yindex in range(0,celldensity):
            for xindex in range(0,celldensity):
                neighbours = 0
                for index in indexpositions: #Counting Neighbours
                    try:
                        if (xindex+index[0]) != -1 and (xindex+index[0]) != celldensity and (yindex+index[1]) != -1 and (yindex+index[1]) != celldensity:
                            if window.nametowidget(str(xindex+index[0])+","+str(yindex+index[1])).cget('bg') == activecolor:
                                neighbours = neighbours + 1
                    except:
                        pass
                #-----------------------------------------------#
                if (neighbours < 2 and window.nametowidget(str(xindex)+","+str(yindex)).cget('bg') != "white") or (neighbours > 3 and window.nametowidget(str(xindex)+","+str(yindex)).cget('bg') != "white"):
                    deadlist.append( str(xindex)+","+str(yindex)   )
                if (neighbours == 3 and window.nametowidget(str(xindex)+","+str(yindex)).cget('bg') == "white"):
                    alivelist.append( str(xindex)+","+str(yindex))
 
        for itemlist in alivelist:
            window.nametowidget(itemlist).config(bg=activecolor)
        for itemlist in deadlist:
            window.nametowidget(itemlist).config(bg="white")
#-------------------------------------------------------------------------------------------------------#                
 
def ChangeCell(item): #Clicking on a Cell
    if window.nametowidget(item).cget('bg') == "white":
        window.nametowidget(item).config(bg=activecolor)
    else:
        window.nametowidget(item).config(bg="white")
    window.update()
 
for yindex in range(0,celldensity): #Amount of Vertical Cells
    for xindex in range(0,celldensity): #Amount of Horizontal Cells
        Cell = Button(window,bd=1,relief=SUNKEN,bg="white",activebackground="grey80",name=str(xindex)+","+str(yindex)
                      ,command=lambda xindex=xindex, yindex=yindex: ChangeCell(str(xindex)+","+str(yindex)) )
        Cell.place(x=(xindex*(800/celldensity)),y=(100+(yindex*(800/celldensity))),width=(800/celldensity),height=(800/celldensity))
#-------------------------------------------------------------------------------------------------------#
 
def AutomaticPlay(action): #Clicking the >> button (Fast Forward mode)
    print(action)
    if action == ">>":
        automaticgo.config(text="=")
        forwardbutton.config(state=DISABLED)
        while automaticgo.cget('text') == "=":
            time.sleep(0.001)
            window.update()
            NextGeneration("Automatic")
    if action == "=":
        forwardbutton.config(state=NORMAL
                             )
        automaticgo.config(text=">>")
 
#------------------------------------------------------------------------------------------------------#
 
def ResetBoard(): #(Clears all active cells
    if automaticgo.cget('text') == ">>":
        generationlabel.config(text="Generation 1")
        for yindex in range(0,celldensity):
                for xindex in range(0,celldensity):
                    if window.nametowidget(str(xindex)+","+str(yindex)).cget('bg') == activecolor:
                        window.nametowidget(str(xindex)+","+str(yindex)).config(bg="white")
                
#------------>>>>>>>>>>>>>>>>>>---------------#
generationlabel = Label(window,text="Generation 1",font=("Verdana",20))
generationlabel.place(x=280,y=55,width=240,height=40)
 
forwardbutton = Button(window,text="Next",justify=CENTER,bd=3,font=("Verdana",20),command= lambda: NextGeneration("ForwardButton"))
forwardbutton.place(x=520,y=55,width=90,height=40)
 
alivekey = Label(window,text="Alive:",font=("Verdana",15))
alivekey.place(x=20,y=10,width=80,height=25)
alivecolor = Label(window,bg=activecolor)
alivecolor.place(x=100,y=10,width=25,height=25)
 
deadkey = Label(window,text="Dead:",font=("Verdana",15))
deadkey.place(x=20,y=40,width=80,height=25)
deadcolor = Label(window,bg="white",relief=SOLID,bd=1)
deadcolor.place(x=100,y=40,width=25,height=25)
 
automaticgo = Button(window,text=">>",justify=CENTER,bd=3,font=("Verdana",20))
automaticgo.place(x=730,y=55,width=60,height=40)
automaticgo.config(command= lambda: AutomaticPlay(automaticgo.cget('text')))
 
resetbutton = Button(window,text="Reset",justify=CENTER,bd=3,font=("Verdana",12),command=lambda: ResetBoard())
resetbutton.place(x=730,y=15,width=60,height=40)
 
window.update()
