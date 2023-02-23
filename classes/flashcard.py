class Flashcard:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)