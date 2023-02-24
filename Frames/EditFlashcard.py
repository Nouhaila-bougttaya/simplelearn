import os
import tkinter as tk
import pandas as pd
from classes.flashcard import Flashcard as FlashcardClass
from classes.card import Card as CardClass
#todo regler le formulaire edit

class EditFlashCard(tk.Frame):
    def __init__(self, parent, controller, flashcard):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.flashcard_name = flashcard
        self.flashcard = self.load_flashcard()
        self.create_widgets()

    def load_flashcard(self):
        # Load the flashcard from the CSV file
        file_path = f"data/{self.flashcard_name}.csv"
        if not os.path.exists(file_path):
            return FlashcardClass("", "")

        df = pd.read_csv(file_path)
        cards = [CardClass(row["French"], row["English"]) for _, row in df.iterrows()]
        return FlashcardClass(self.flashcard_name, "", cards)

    def create_widgets(self):
        tk.Label(self, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)
        self.name_entry.insert(0, self.flashcard.name)

        tk.Label(self, text="Color:").grid(row=1, column=0)
        self.color_entry = tk.Entry(self)
        self.color_entry.grid(row=1, column=1)
        self.color_entry.insert(0, self.flashcard.color)

        tk.Label(self, text="Word:").grid(row=2, column=0)
        self.word_entry = tk.Entry(self)
        self.word_entry.grid(row=2, column=1)

        tk.Label(self, text="Translation:").grid(row=3, column=0)
        self.translation_entry = tk.Entry(self)
        self.translation_entry.grid(row=3, column=1)

        tk.Button(self, text="Add Card", command=self.add_card_callback).grid(row=4, column=1)

        tk.Label(self, text="Cards:").grid(row=5, column=0)
        self.card_listbox = tk.Listbox(self)
        self.card_listbox.grid(row=6, column=0, columnspan=2)

        tk.Button(self, text="Save Flashcard", command=self.save_flashcard).grid(row=7, column=0, columnspan=2)

        # Fill in the listbox with existing cards
        for card in self.flashcard.cards:
            self.card_listbox.insert(tk.END, f"{card.word} - {card.translation}")

    def add_card_callback(self):
        word = self.word_entry.get()
        translation = self.translation_entry.get()

        card = CardClass(word, translation)
        self.flashcard.add_card(card)

        self.card_listbox.insert(tk.END, f"{card.word} - {card.translation}")

    def save_flashcard(self):
        # Save the edited flashcard to the CSV file
        name = self.name_entry.get()
        color = self.color_entry.get()

        cards = self.flashcard.cards
        df = pd.DataFrame([[card.word, card.translation] for card in cards], columns=["French", "English"])
        df.to_csv(f"data/{name}.csv", index=False)

        # Update flashcard name and color in personalised.csv file
        personalised_df = pd.read_csv("data/personalised.csv")
        personalised_df.loc[personalised_df["name"] == self.flashcard_name, "name"] = name
        personalised_df.loc[personalised_df["name"] == name, "color"] = color
        personalised_df.to_csv("data/personalised.csv", index=False)

        # Switch back to home screen
        self.controller.show_frame("Home")
        
"""class EditFlashCard(tk.Frame):
    def __init__(self, parent, controller, flashcard):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.flashcard_name = flashcard
        self.flashcard = self.load_flashcard()
        self.create_widgets()

    def load_flashcard(self):
        # Load the flashcard from the CSV file
        file_path = f"data/{self.flashcard_name}.csv"
        if not os.path.exists(file_path):
            return FlashcardClass("", "")

        df = pd.read_csv(file_path)
        cards = [CardClass(row["French"], row["English"]) for _, row in df.iterrows()]
        return FlashcardClass(self.flashcard_name, "", cards)

    def create_widgets(self):
        tk.Label(self, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)
        self.name_entry.insert(0, self.flashcard.name)

        tk.Label(self, text="Color:").grid(row=1, column=0)
        self.color_entry = tk.Entry(self)
        self.color_entry.grid(row=1, column=1)
        self.color_entry.insert(0, self.flashcard.color)

        tk.Label(self, text="Word:").grid(row=2, column=0)
        self.word_entry = tk.Entry(self)
        self.word_entry.grid(row=2, column=1)

        tk.Label(self, text="Translation:").grid(row=3, column=0)
        self.translation_entry = tk.Entry(self)
        self.translation_entry.grid(row=3, column=1)

        tk.Button(self, text="Add Card", command=self.add_card_callback).grid(row=4, column=1)

        tk.Label(self, text="Cards:").grid(row=5, column=0)
        self.card_listbox = tk.Listbox(self)
        self.card_listbox.grid(row=6, column=0, columnspan=2)

        tk.Button(self, text="Delete Card", command=self.delete_card_callback).grid(row=7, column=0)
        tk.Button(self, text="Save Flashcard", command=self.save_flashcard).grid(row=7, column=1)

        # Fill in the listbox with existing cards
        for card in self.flashcard.cards:
            self.card_listbox.insert(tk.END, f"{card.word} - {card.translation}")

    def add_card_callback(self):
        word = self.word_entry.get()
        translation = self.translation_entry.get()

        card = CardClass(word, translation)
        self.flashcard.add_card(card)

        self.card_listbox.insert(tk.END, f"{card.word} - {card.translation}")

    def delete_card_callback(self):
        selection = self.card_listbox.curselection()
        if selection:
            index = selection[0]
            self.card_listbox.delete(index)
            self.flashcard.cards.pop(index)

    def save_flashcard(self):
        # Save the edited flashcard to the CSV file
        name = self.name_entry.get()
        color = self.color_entry.get()

       
        cards = self.flashcard.cards
        df = pd.DataFrame([[card.word, card.translation] for card in cards], columns=["French", "English"])
        df.to_csv(f"data/{name}.csv",index=False)
        
        # Update flashcard name and color in personalised.csv file
        personalised_df = pd.read_csv("data/personalised.csv")
        #Récupérer le nom de flashcard à modifier
        current_name = self.flashcard_name
        """""" personalised_df.loc[personalised_df["name"] == self.flashcard_name, "name"] = name
        personalised_df.loc[personalised_df["name"] == name, "color"] = color
        personalised_df.to_csv("data/personalised.csv", index=False)"""""
        #personalised_df.loc[personalised_df["name"] == current_name, ["name", "color"]] = [name, color]
        
         # If the color was changed, update the flashcard name in personalised.csv
        
        #if color != self.flashcard.color:
        #    personalised_df.loc[personalised_df["name"] == current_name, "name"] = name
        
        #personalised_df.to_csv("data/personalised.csv", index=False)
        
        # Switch back to home screen
        #self.controller.show_frame("Home")"""