import tkinter as tk
import pandas as pd


from classes.flashcard import Flashcard as FlashcardClass
from classes.card import Card as CardClass
class ScrollCards(tk.Frame):
    def __init__(self, parent, flashcard:FlashcardClass, controller):
        tk.Frame.__init__(self, parent)
        self. controller= controller
        self.flashcard = flashcard
        self.current_card_index = 0
        self.create_widgets()

    def create_widgets(self):
        self.card_label = tk.Label(self, text="")
        self.card_label.pack(fill="both", expand=True)

        self.translation_label = tk.Label(self, text="")
        self.translation_label.pack()

        self.i_know_button = tk.Button(self, text="I Know", command=self.i_know_callback)
        self.i_know_button.pack(side="left")

        self.i_dont_know_button = tk.Button(self, text="I Don't Know", command=self.i_dont_know_callback)
        self.i_dont_know_button.pack(side="right")

        self.update_card()
        self.after(5000, self.flip_card)

    def update_card(self):
        card = self.flashcard.cards[self.current_card_index]
        self.card_label.configure(text=card.word)
        self.translation_label.configure(text="")
        self.i_know_button.configure(state="normal")
        self.i_dont_know_button.configure(state="normal")

    def flip_card(self):
        card = self.flashcard.cards[self.current_card_index]
        self.card_label.configure(text="")
        self.translation_label.configure(text=card.translation)
        self.i_know_button.configure(state="disabled")
        self.i_dont_know_button.configure(state="disabled")
        self.after(5000, self.next_card)

    def next_card(self):
        self.current_card_index += 1
        if self.current_card_index < len(self.flashcard.cards):
            self.update_card()
            self.after(5000, self.flip_card)
        else:
            self.controller.show_frame("Home")

    def i_know_callback(self):
        # TODO: Implement behavior for when "I Know" button is clicked
        pass

    def i_dont_know_callback(self):
        # TODO: Implement behavior for when "I Don't Know" button is clicked
        pass
