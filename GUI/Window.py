from tkinter import * 
import tkinter.font as font
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

    def getButton(self,text):
        return Button(self.window,text=text,width = 20,borderwidth=1,relief="solid",font=font.Font(size=10))

    def getRadioButton(self,text,value,command,state):        
        return Radiobutton(self.window,text=text,variable=self.selection,value=value,command=command,indicatoron=0,state = state)

    def getDropDownMenu(self):
        self.var = StringVar(self.window)
        self.var.set(self.options[0])
        self.var.trace("w",self.dropDownListener)        
        return OptionMenu(self.window,self.var,*self.options)
        
    def encDecKeyLabelChanger(self):        
        self.encdeclabel.config(text = constants.DECRYPTION_TEXT if self.selection.get() == 2 else constants.ENCRYPTION_TEXT)
        self.keylabel.config(text= constants.DECRYPT_KEY_FIELD_TEXT if self.selection.get() == 2 else constants.ENCRYPT_KEY_FIELD_TEXT)
        self.strCipherOutputLabel.config(text = constants.STRING_LBL if self.selection.get() == 2 else constants.CIPHER_LBL)

    def dropDownListener(self,*args):
        if self.var.get() in constants.KEY_BASED_ENCRYPTIONS:
            self.enableDecryptRadio()
            self.enableKeyField(self.keyEntry)
        else:
            self.disableDecryptRadio()
            self.disableKeyField(self.keyEntry)

    

    def enableDecryptRadio(self):
        self.decrypter_radio.config(state=constants.NORMAL)

    def disableDecryptRadio(self):
        self.selection.set(1)
        self.encDecKeyLabelChanger()
        self.decrypter_radio.config(state=constants.DISABLED)

    def disableKeyField(self,field):        
        field.delete("1.0","end")
        field.config(state=constants.DISABLED,bg=constants.LIGHTGREY)
    
    def enableKeyField(self,field):
        field.config(state=constants.NORMAL,bg=constants.WHITE)

        