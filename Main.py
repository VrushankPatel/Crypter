from GUI import Window
import GUI.Constants as constants

if __name__ == "__main__":
    
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
    window.strCipherEntry = window.getTextArea(3,25,constants.NORMAL).grid(row=4,column=0)
    
    window.keylabel = window.getLabel(constants.ENCRYPT_KEY_FIELD_TEXT)
    window.keylabel.grid(row=3,column=1)
    window.keyEntry = window.getTextArea(3,25,constants.DISABLED)
    window.keyEntry.grid(row=4,column=1)
    window.window.mainloop()