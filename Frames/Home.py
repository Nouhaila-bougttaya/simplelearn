import os
import sys
import tkinter as tk
import pandas as pd

from Frames.Fram_Flashcard import FlashCard as Flascard_widget
from classes.flashcard import Flashcard as FlashcardClass
from classes.card import Card as CardClass
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(file))))
import customtkinter as ctk


# from utils import COLORS, FONT


class Homepage(tk.Frame):
    # la création des widgets
    def __init__(self, parent: tk.Tk, controller: tk.Tk):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        """self.controller.columnconfigure(0, weight=1)
        self.controller.rowconfigure(0, weight=1)"""
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # variables
        self.cards_type = True
        self.flashcards = []
        self.configure(bg='beige')
        # top frame
        self.top_frame = tk.Frame(self, bg="white")
        self.top_frame.grid(row=0, column=0, sticky="ew")
        # floating button to add flashcard
        self.addbtn_frame = tk.Frame(self, bg="white")
        self.addbtn = tk.PhotoImage(file="images/Bouton+.png")
        self.addbtn = self.addbtn.subsample(1, 1)
        self.addbtn_label = tk.Label(self.addbtn_frame, image=self.addbtn, bg="beige", cursor="hand2")
        self.addbtn_label.grid()
        self.addbtn_label.bind("<Button-1>", lambda e: self.controller.show_frame("AddFlashCard"))
        # self.addbtn_frame.grid(column=2)
        self.addbtn_frame.grid(column=10, row=15, sticky="se")

        # self.dpbtn_image = tk.PhotoImage(file='./assets/default_fc.png')
        # self.dpbtn_image = self.dpbtn_image.subsample(3, 3)
        # self.dpbtn_label = tk.Label(self.top_frame, image=self.dpbtn_image, bg="white", cursor="hand2")
        # self.dpbtn_label.bind("<Button-1>", lambda e: self.switch_default_personalized_cards())

        # self.dpbtn = tk.Button(self.top_frame, text="Default cards", bg=COLORS['primary'],relief = "groove", fg="white", font=FONT["button"])
        # self.dpbtn.config(command=self.switch_default_personalized_cards)
        # self.dpbtn.pack(side="right", padx=10, pady=10)
        # self.dpbtn_label.pack(side="right", padx=10, pady=10)

        # self.top_frame.pack(side="top", fill="x", expand=False)

        # flashcard frame
        self.flashcard_frame = tk.Frame(self, bg="beige")
        self.flashcard_frame.grid(row=1, column=0, sticky="nsew")
        self.load_flashcards()

    def clear_flashcards_frame(self):
        for widget in self.flashcard_frame.winfo_children():
            widget.destroy()

    def load_flashcards(self):

        # Define the window and grid dimensions

        num_rows = 3
        num_cols = 4

        # Read in the CSV file using pandas
        df = pd.read_csv('data/personalised.csv')

        # Create the grid list of flashcards
        for i in range(num_rows):
            for j in range(num_cols):
                # Calculate the index for the current flashcard
                index = i * num_cols + j
                if index < len(df):

                    # Get the name and color attributes from the data
                    name = df.loc[index, 'name']
                    color = df.loc[index, 'color']
                    # Instanciation de Flashcard
                    flashcard_objet = FlashcardClass(name, color)

                    # L ouverture du fichier file.csv qui contient les cartes
                    file_name = 'data/' + name + '.csv'
                    sub_df = pd.read_csv(file_name)
                    for index, row in sub_df.iterrows():
                        word = row['French']
                        translation = row['English']
                        card = CardClass(word, translation)
                        flashcard_objet.add_card(card)

                    flashcard_widget = Flascard_widget(self.flashcard_frame, flashcard=flashcard_objet,
                                                       controller=self.controller)
                    flashcard_widget.grid(row=i, column=j, padx=10, pady=10)

                    # Add a canvas with the color attribute to the frame
                    # self.canvas = tk.Canvas(self.frame, width=50, height=50, bg=color)
                    # Create a text object inside the canvas
                    # Todo 9adi les parametre bax text yji center name of the flashcards
                    # self.canvas.create_text(20, 10, text=name, anchor="center")

        self.flashcard_frame.grid(row=1, column=0, sticky="nsew")