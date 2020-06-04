from tkinter import * 

class Window:        
    def __init__(self, title):        
        self.window = Tk()
        self.window.resizable(False,False)
        #self.window.minsize(sizeX,sizeY)
        self.window.title("Crypter")

    def getEntryObject(self, row, column):
        return Entry(self.window).grid(row=row,column=column)

    def getTextArea(self,height,width,state):
        color = 'lightgrey' if state == 'disabled' else 'white'
        return Text(self.window,height = height, width = width,state = state,bg=color)

    def getLabel(self,text):
        return Label(self.window,text=text)

    def getDropDownMenu(self,options):
        var = StringVar(self.window)
        var.set(options[0])
        return OptionMenu(self.window,var,*options)
        