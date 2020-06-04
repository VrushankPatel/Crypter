from tkinter import * 
import GUI.Constants as constants
class Window: 
    def __init__(self, title):        
        self.window = Tk()
        self.selection = IntVar()
        self.selection.set(1)
        self.window.resizable(False, False)
        self.window.title(title)

    def getEntryObject(self, row, column):
        return Entry(self.window).grid(row=row,column=column)

    def getTextArea(self,height,width,state):
        color = constants.LIGHTGREY if state == constants.DISABLED else constants.WHITE
        return Text(self.window,height = height, width = width,state = state,bg=color,borderwidth=2,relief="solid")

    def getLabel(self,text):
        return Label(self.window,text=text)

    def getRadioButton(self,text,value,command):
        return Radiobutton(self.window,text=text,variable=self.selection,value=value,command=command,indicatoron=0)

    def radioValueGetter(self):
        if self.selection.get() == 2:
            self.encdeclabel.config(text="Enter the cipher to be decrypted")
        else:
            self.encdeclabel.config(text="Enter the String to be encrypted")

    def getDropDownMenu(self,options):
        var = StringVar(self.window)
        var.set(options[0])
        return OptionMenu(self.window,var,*options)
        