from GUI import Window

if __name__ == "__main__":
    window = Window("Crypter")        
    
    window.getLabel("Choose the Encryption Angorithm : ").grid(row=0,column=0)
    window.getDropDownMenu(["Jan","Feb","Mar"]).grid(row=0,column=1)
    window.getLabel("Enter String to be encrypted : ").grid(row=2,column=0)
    entry1 = window.getTextArea(3,16).grid(row=2,column=1)
    
    window.getLabel("Enter Key to encrypt the string : ").grid(row=4,column=0)
    entry2 = window.getTextArea(3,16).grid(row=4,column=1)

    window.window.mainloop()