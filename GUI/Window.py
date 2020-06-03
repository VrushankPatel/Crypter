import tkinter as tk

class Window:
    def __init__(self,title,isFullScreen):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen',isFullScreen)
        self.window.title("Crypter")
        