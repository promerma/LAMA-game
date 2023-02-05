from numpy import zeros, append, delete, arange, where, insert, sum
from random import shuffle


class Table:
    NCARDS = 56
    pile = zeros(1,
                 dtype=int)  # pile is initially an int, we append more cards (from 0-6). The top card is pile[len(pile)-1]

    # Constructor
    def __init__(self):
        self.restartTable()

    # Check if there are cards on deck. Trues=yes, False=no
    def cardsOnDeck(self):
        if len(self.deck) > 0:
            return True
        else:
            return False

    # Shuffle cards from pile and add to deck
    def shuffleDeck(self):
        # PUT THE CARDS OF THE PILE IN THE DECK AND SHUFFLE
        if len(self.pile) == 1:
            print("Game cannot continue: not enough cards on the deck")
            exit()

        self.deck = self.pile
        # Delete the top card in the pile
        self.deck = delete(self.deck, len(self.deck) - 1)
        shuffle(self.deck)
        # Restart pile
        self.pile = zeros(1, dtype=int)
        self.pile[0] = self.pile[len(self.pile) - 1]

    # Set table to initialise the round
    def restartTable(self):
        # Create the deck
        self.deck = zeros(self.NCARDS, dtype=int)
        count = 0
        for i in range(7):
            for j in range(8):
                self.deck[j + count * 8] = i
            count += 1

        # Shuffle
        shuffle(self.deck)

        # Put the first into the pile and delete it from deck
        self.pile = zeros(1, dtype=int)
        self.pile[0] = self.deck[0]
        self.deck = delete(self.deck, 0)

    # Remove the first card from deck
    def removeFromDeck(self):
        self.deck = delete(self.deck, 0)

    # Add a given card to pile
    def addToPile(self, card):
        self.pile = append(self.pile, card)