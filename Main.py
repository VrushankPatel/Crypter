from GUI import Window
import GUI.Constants as constants
options = [
    "SHA256",
    "SHA384",
    "SHA224",
    "SHA512",
    "SHA1",
    "MD5",
    "RC4"
]
if __name__ == "__main__":
    window = Window(constants.TITLE)        
    
    window.getRadioButton(constants.ENCRYPTER,1,window.radioValueGetter).grid(row=0,column=0)
    window.getRadioButton(constants.DECRYPTER,2,window.radioValueGetter).grid(row=0,column=1)
    
    window.getLabel(constants.CHOOSEALGORITHMTEXT).grid(row=1,column=0)
    window.getDropDownMenu(options).grid(row=1,column=1)

    window.encdeclabel = window.getLabel(constants.ENCRYPTIONTEXT)
    window.encdeclabel.grid(row=3,column=0)
    entry1 = window.getTextArea(3,25,constants.NORMAL).grid(row=4,column=0)
    
    window.keylabel = window.getLabel(constants.KEYFIELDTEXT)
    window.keylabel.grid(row=3,column=1)
    entry2 = window.getTextArea(3,25,constants.DISABLED).grid(row=4,column=1)

    window.window.mainloop()