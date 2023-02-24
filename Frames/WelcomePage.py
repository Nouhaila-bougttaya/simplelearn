import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        
        # Ajouter une étiquette de salutation
        greeting = tk.Label(self, text="Bonjour! Bienvenue sur mon programme!", font=("Helvetica", 20))
        greeting.pack(pady=50)
        
        # Ajouter un bouton pour passer à la page HomePage
        #button = tk.Button(self, text="Passer à HomePage", font=("Helvetica", 16), command=self.show_homepage)
        #button.pack(pady=50)
        #
        
        self.btnAcc = tk.PhotoImage(file="images/Bouton+.png")
        self.btnAcc_hover = tk.PhotoImage(file="images/Bouton+ (2).png")
        self.btnAcc = self.addbtn.subsample(1, 1)
        self.btnAcc_hover = self.addbtn_hover.subsample(1, 1)
        self.btnAcc_label = tk.Label(self.addbtn_frame, image=self.addbtn, bg="beige", cursor="hand2")
        self.btnAcc_label.grid()
        self.btnAcc_label.bind("<Button-1>", lambda e: self.controller.show_frame("AddFlashCard"))
        self.addbtn_label.bind("<Enter>", lambda e: self.addbtn_label.config(image=self.addbtn_hover))
        self.addbtn_label.bind("<Leave>", lambda e: self.addbtn_label.config(image=self.addbtn))
        # self.addbtn_frame.grid(column=2)
        self.addbtn_frame.grid(column=10, row=15, sticky="se")
        
    def show_homepage(self):
        self.controller.show_frame("Home")