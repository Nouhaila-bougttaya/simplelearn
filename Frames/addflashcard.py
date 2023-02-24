import tkinter as tk
import pandas as pd


from classes.flashcard import Flashcard as FlashcardClass
from classes.card import Card as CardClass


class AddFlashCard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.flashcard = FlashcardClass("", "")
        self.create_widgets()
        # Create input fields for flashcard name and color

    def create_widgets(self):
        #TODO fixe the ui here
        tk.Label(self, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self, text="Color:").grid(row=1, column=0)
        self.color_entry = tk.Entry(self)
        self.color_entry.grid(row=1, column=1)

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
    def add_card(self):
        # Create input fields for the card's word and translation
        word_label = tk.Label(self, text="Word:")
        word_entry = tk.Entry(self)
        translation_label = tk.Label(self, text="Translation:")
        translation_entry = tk.Entry(self)

        # Pack the input fields onto the frame
        word_label.pack()
        word_entry.pack()
        translation_label.pack()
        translation_entry.pack()


        # Create a button to add the card and bind it to the add_card_callback function
        add_card_button = tk.Button(self, text="Add", command=self.add_card_callback)
        add_card_button.pack()

    
    def add_card_callback(self):
        word = self.word_entry.get()
        translation = self.translation_entry.get()
        if not word and not translation:
            tk.messagebox.showerror("Erreur", "S'il vous plait enter les deux un mot et sa traduction.")
            return
        if not word :
            tk.messagebox.showerror("Erreur", "Veuillez entrer un mot .")
            return
        if not translation:
            tk.messagebox.showerror("Erreur", "Veuillez entrer une traduction de mot.")
            return

        if self.flashcard is None:
            name = self.name_entry.get()
            color = self.color_entry.get()
            #self.flashcard = FlashcardClass(name, color)

        card = CardClass(word, translation)
        self.flashcard.add_card(card)

        #self.card_list.append(card)
        self.card_listbox.insert(tk.END, f"{card.word} - {card.translation}")
    
    def save_flashcard(self):
        # Create a Flashcard object from the input fields and save it to a CSV file
        name = self.name_entry.get()
        color = self.color_entry.get()
        if not name  and not color:
            tk.messagebox.showerror("Erreur", "Veuillez entrer le nom et la couleur de la nouvelle flashcard à créer.")
            return
        if not name :
            tk.messagebox.showerror("Erreur", "Veuillez entrer le nom de la flashcard que vous voulez créer.")
            return
        if not color:
            tk.messagebox.showerror("Erreur", "Veuillez choisir une couleur.")
            return
                
        # Afficher un message de confirmation
        else:
            tk.messagebox.showinfo("Succès", f"Le mot et sa traduction sont bien stocker dans la flashcard")
                
        cards = self.flashcard.cards
        print(cards)
        df = pd.DataFrame([[card.word, card.translation] for card in cards], columns=["French", "English"])
        df.to_csv(f"data/{name}.csv", index=False)

        ###going back home
        self.controller.show_frame("Home")
