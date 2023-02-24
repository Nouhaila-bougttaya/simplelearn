import tkinter as tk

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        
        # Ajouter une étiquette de salutation
        greeting = tk.Label(self, text="Bonjour! Bienvenue sur mon programme!", font=("Helvetica", 20))
        greeting.pack(pady=50)
        
        # Ajouter un bouton pour passer à la page HomePage
        button = tk.Button(self, text="Passer à HomePage", font=("Helvetica", 16), command=self.show_homepage)
        button.pack(pady=50)
        
    def show_homepage(self):
        self.controller.show_frame("Home")