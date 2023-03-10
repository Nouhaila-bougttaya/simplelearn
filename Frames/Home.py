import os
import sys
import tkinter as tk
import pandas as pd
from datetime import datetime, timedelta
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

        # variabes
        self.cards_type = True
        self.flashcards = []
        self.configure(bg='beige')
        self.notification = FlashcardClass("notification", "")

        # top frame
        self.top_frame = tk.Frame(self, bg="white")
        self.top_frame.grid(row=0, column=0, sticky="ew")
        # floating button to add flashcard
        self.addbtn_frame = tk.Frame(self, bg="white")
        self.addbtn = tk.PhotoImage(file="images/Bouton+.png")
        self.addbtn_hover = tk.PhotoImage(file="images/Bouton+ (2).png")
        self.addbtn = self.addbtn.subsample(1, 1)
        self.addbtn_hover = self.addbtn_hover.subsample(1, 1)
        self.addbtn_label = tk.Label(self.addbtn_frame, image=self.addbtn, bg="beige", cursor="hand2")
        self.addbtn_label.grid()
        self.addbtn_label.bind("<Button-1>", lambda e: self.controller.show_frame("AddFlashCard"))
        # self.addbtn_frame.grid(column=2)
        self.addbtn_frame.grid(column=10, row=15, sticky="se")






        # flashcard fram
        
        self.flashcard_frame = tk.Frame(self, bg="beige")
        self.flashcard_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.load_flashcards()
        self.loead_notification()
    def loead_notification(self):

        # Load flashcards from file
        try:
            df = pd.read_csv('data/user.csv')
        except FileNotFoundError:
            return []

            # convert date_of_notification column to datetime
        df['date_of_notification'] = pd.to_datetime(df['date_of_notification'])

        # get today's date
        today = datetime.now().date()

        # filter the DataFrame to only include cards that have a date_of_notification equal to today
        df = df[df['date_of_notification'].dt.date == today]

        # list of Card objects from the filtered DataFrame

        for _, row in df.iterrows():

            card = CardClass(row['word'], row['translation'], row['try'], row['date_of_notification'])

            self.notification.add_card(card)


    def clear_flashcards_frame(self):
        for widget in self.flashcard_frame.winfo_children():
            widget.destroy()

    def load_flashcards(self):

        # Define the window and grid dimensions

        num_rows = 5
        num_cols = 3

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
                    #la taille des flashcards
                    flashcard_widget.grid(row=i, column=j, padx=5, pady=5,ipady=50,ipadx=150)

                    # Add a canvas with the color attribute to the frame
                    # self.canvas = tk.Canvas(self.frame, width=50, height=50, bg=color)
                    # Create a text object inside the canvas
                    # Todo 9adi les parametre bax text yji center name of the flashcards
                    # self.canvas.create_text(20, 10, text=name, anchor="center")
        
        #self.flashcard_frame.grid(row=1, column=0, sticky="nsew")
        # Set the size of the flashcard frame
        frame_width = num_cols * 200  # adjust as needed
        frame_height = num_rows * 200  # adjust as needed
        self.flashcard_frame.config(width=frame_width, height=frame_height)