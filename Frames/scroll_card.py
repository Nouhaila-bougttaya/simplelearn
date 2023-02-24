import tkinter as tk
import pandas as pd
from PIL import Image, ImageTk
from datetime import datetime, timedelta
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
        self.top_frame = tk.Frame(self, bg="white")
        self.top_frame.pack()
        # create canvas widget
        self.canvas = tk.Canvas(self.top_frame, width=self.winfo_screenwidth() * 0.7, height=self.winfo_screenheight() * 0.7)
        self.canvas.pack(fill="both", expand=True)

        # create image item and set as background
        img = Image.open("images/Rectangle 1.png")
        img = img.resize((900,500))
        img = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, image=img, anchor="nw")
        self.canvas.image = img

        # create label widgets
        #self.card_label =self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.card_label = tk.Label(self.canvas, text="",bg="#c19a6b")
        self.card_label.place(relx=0.5, rely=0.5, anchor="center")

        self.translation_label = tk.Label(self.canvas, text="")
        self.translation_label.place(relx=0.5, rely=0.6, anchor="center")
        # create timer label widget
        self.timer_label = tk.Label(self, text="", font=("Arial", 14))
        self.timer_label.pack(side="top", pady=10)

        # create buttons
        self.i_know_button = tk.Button(self, text="I Know", command=self.i_know_callback)
        self.i_know_button.pack(side="left", padx=10)

        self.i_dont_know_button = tk.Button(self, text="I Don't Know", command=self.i_dont_know_callback)
        self.i_dont_know_button.pack(side="right", padx=10)

        # update card and flip after 5 seconds
        self.update_timer_label(5)
        self.update_card()
        self.after(5000, self.flip_card)

    def update_timer_label(self, time_left):
        if time_left > 0:
            self.timer_label.configure(text=f"Translation in {time_left} seconds")
            self.after(1000, lambda: self.update_timer_label(time_left - 1))
        else:
            self.timer_label.configure(text="")

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
            self.update_timer_label(5)
        else:
            self.controller.show_frame("Home")

    def i_know_callback(self):

        # TODO: Implement behavior for when "I Know" button is clicked
        card = self.flashcard.cards[self.current_card_index]
        if card.Try:
            # update the try and date_of_notification fields based on the current try value
            if card.Try == 2:
                #TODO implement the code remove from the cards_notification

             date_of_notification = None

            elif card.Try == 0:
                card.Try += 1
                date_of_notification = datetime.now().date() + timedelta(days=7)
            elif card.Try == 1:
                card.Try += 1
                date_of_notification = datetime.now().date() + timedelta(days=30)


            # create a new DataFrame with the updated flashcard information
            new_row = {'word': card.word, 'translation': card.translation, 'Try': card.Try,
                       'date_of_notification': date_of_notification}

            # read the existing CSV file into a DataFrame
            try:
                df = pd.read_csv('data/user.csv')
            except FileNotFoundError:
                df = pd.DataFrame(columns=['word', 'translation', 'Try', 'date_of_notification'])

            # update the corresponding row in the DataFrame
            df.loc[df['word'] == card.word, ['Try', 'date_of_notification']] = [card.Try, date_of_notification]

            # write the updated DataFrame to the CSV file
            df.to_csv('data/user.csv', index=False)

            # go to the next card
            self.next_card()

    def i_dont_know_callback(self):
        # TODO: Implement behavior for when "I Don't Know" button is clicked
        card = self.flashcard.cards[self.current_card_index]
        if card.Try:
            date_of_notification = datetime.now().date() + timedelta(days=1)
            # create a new DataFrame with the flashcard information
            new_row = {'word': card.word, 'translation': card.translation, 'date_of_notification': date_of_notification,
                       'try': 0}
            # read the existing CSV file into a DataFrame
            try:
                df = pd.read_csv('data/user.csv')
            except FileNotFoundError:
                df = pd.DataFrame(columns=['word', 'translation', 'date_of_notification', 'try'])
            # append the new row to the DataFrame
            df = df.append(new_row, ignore_index=True)
            # write the updated DataFrame to the CSV file
            df.to_csv('data/user.csv', index=False)
            # go to the next card
            self.next_card()


