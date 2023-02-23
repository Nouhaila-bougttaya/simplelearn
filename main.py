#import os
import tkinter as tk
from tkinter import *

import customtkinter as ctk

#from frames.AddFlashCard import AddFlashCard
#from frames.Cards import Cards
#from frames.EditFlashCard import EditFlashCard
from Frames.scroll_card import ScrollCards
from Frames.Home import Homepage
from Frames.addflashcard import AddFlashCard
from Frames.EditFlashcard import EditFlashCard




class App(tk.Tk):
    def __init__(self):
        super().__init__()
       # last_time = last_time_visited()
        # Setting up Initial parameters


        # Setting up Initial parameters
        self.title(f"Easylearn")
        #self.geometry("800x600")
        self.state("zoomed")
        self.minsize(480,360)
        self.resizable(False, False)
        self.center_win()

        ## Creating a container



        self.container = tk.Frame(self, bg="white")
        self.container.pack(side="top", fill="both", expand = True)

        self.show_frame("Home")

    def show_frame(self, page_name ,*args):

        for widget in self.container.winfo_children():
            widget.destroy()
        self.geometry("800x600")
        # center the window
        if page_name == "Home":

            frame = Homepage(parent=self.container, controller=self)
        elif page_name == "AddFlashCard":
            frame = AddFlashCard(parent=self.container, controller=self)
        elif page_name == "EditFlashCard":
            frame = EditFlashCard(parent=self.container, controller=self, flashcard=args[0])
        elif page_name == "ScrollCards":
            frame = ScrollCards(parent=self.container, controller=self, flashcard=args[0])

        frame.pack(side="top", fill="both", expand=True)
        frame.tkraise()
        self.center_win()


    def center_win(self):
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.deiconify()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    app = App()
    app.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
