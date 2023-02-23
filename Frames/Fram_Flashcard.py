import tkinter as tk

from classes.flashcard import Flashcard as FlashcardClass
class FlashCard(tk.Frame):
    def __init__(self, parent, controller,flashcard: FlashcardClass):
        tk.Frame.__init__(self, parent ,bg=flashcard.color)
        self.controller = controller
        self.flashcard = flashcard

        self.create_widgets()

    def create_widgets(self):
        # Create a canvas with the flashcard's color
        color_canvas = tk.Canvas(self, width=100, height=100, highlightthickness=0, bg=self.flashcard.color)
        color_canvas.pack(side=tk.TOP, padx=10, pady=10)

        # Create a label for the flashcard's name
        name_label = tk.Label(color_canvas, text=self.flashcard.name, font=("TkDefaultFont", 18, "bold"), bg=self.flashcard.color)
        name_label.pack(side=tk.TOP, padx=10, pady=10)

        # Create a label for modifying the flashcard
        modify_label = tk.Label(color_canvas, text="Modify", fg="blue", cursor="hand2", bg=self.flashcard.color)
        modify_label.pack(side=tk.TOP, padx=10, pady=10)

        modify_label.bind("<Button-1>", lambda e: self.controller.show_frame("EditFlashCard",self.flashcard))
        self.bind("<Button-1>", lambda e: self.controller.show_frame("ScrollCards", self.flashcard))
