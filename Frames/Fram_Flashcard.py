import tkinter as tk

from classes.flashcard import Flashcard as FlashcardClass
class FlashCard(tk.Frame):
    def __init__(self, parent, controller,flashcard: FlashcardClass):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.flashcard = flashcard

        self.create_widgets()

    def create_widgets(self):
        # Create a label for the flashcard's name
        name_label = tk.Label(self, text=self.flashcard.name, font=("TkDefaultFont", 18, "bold"))
        name_label.pack(side=tk.TOP, padx=10, pady=10)

        # Create a rectangle with the flashcard's color
        color_rect = tk.Canvas(self, width=50, height=50, bg=self.flashcard.color, highlightthickness=0)
        color_rect.pack(side=tk.TOP, padx=10, pady=10)

        # Create a label for modifying the flashcard
        modify_label = tk.Label(self, text="Modify", fg="blue", cursor="hand2")
        modify_label.pack(side=tk.TOP, padx=10, pady=10)

        modify_label.bind("<Button-1>", lambda e: self.controller.show_frame("EditFlashCard",self.flashcard))
        self.bind("<Button-1>", lambda e: self.controller.show_frame("ScrollCards", self.flashcard))