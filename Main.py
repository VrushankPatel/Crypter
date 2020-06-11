from GUI import Window
import GUI.Constants as constants
import tkinter.font as font

def buildwindow():    
    window = Window(constants.TITLE)        
    window.options = constants.NON_KEY_BASED_ENCRYPTIONS + constants.KEY_BASED_ENCRYPTIONS

    window.getLabel(constants.CHOOSE_ALGORITHM_TEXT).grid(row=0,column=0)
    encDecType = window.getDropDownMenu()
    encDecType.grid(row=0,column=1)
    
    window.encrypter_radio = window.getRadioButton(constants.ENCRYPTER,1,window.encDecKeyLabelChanger,constants.NORMAL)
    window.encrypter_radio.grid(row=1,column=0)
    window.decrypter_radio = window.getRadioButton(constants.DECRYPTER,2,window.encDecKeyLabelChanger,constants.DISABLED)
    window.decrypter_radio.grid(row=1,column=1)

    window.encdeclabel = window.getLabel(constants.ENCRYPTION_TEXT)
    window.encdeclabel.grid(row=3,column=0)
    window.strCipherEntry = window.getTextArea(3,25,constants.NORMAL)
    window.strCipherEntry.grid(row=4,column=0)
    
    window.keylabel = window.getLabel(constants.ENCRYPT_KEY_FIELD_TEXT)
    window.keylabel.grid(row=3,column=1)
    window.keyEntry = window.getTextArea(3,25,constants.DISABLED)
    window.keyEntry.grid(row=4,column=1)

    window.strCipherOutputLabel = window.getLabel(constants.CIPHER_LBL)
    window.strCipherOutputLabel.grid(row=5,column=0)
    window.strCipherOutputLabel.config(font=font.Font(size=15))

    window.calculateBtn = window.getButton(constants.CALCULATE)
    window.calculateBtn.grid(row=5,column=1,pady=(10,10))
    window.encDecOpEntry = window.getTextArea(4,51,constants.DISABLED)
    window.encDecOpEntry.grid(row=6,column=0,columnspan=2)
    window.encDecOpEntry.config(state=constants.DISABLED)
    window.window.mainloop()
    
if __name__ == "__main__":
    buildwindow()
