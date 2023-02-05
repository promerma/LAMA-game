from numpy import zeros, append, delete, arange, where, insert, sum
from random import shuffle
from Class_Table import Table

class Hands:
    # Variables
    NPLAYERS = 6
    CARDSXPLAYER = 6

    # Turn count
    index = 0

    # moves
    DRAW = -1
    FOLD = -2

    # States of the game
    CONTINUE = 1
    FINISHED = 2

    def __init__(self, num, table):
        self.NPLAYERS = num
        self.points = zeros(self.NPLAYERS, dtype=int)  # Counts the number of points of each player
        self.rounds = zeros(self.NPLAYERS, dtype=int)  # Counts the number of rounds won by each player
        self.restartHands(table)

    # Set hands to initialise the round
    def restartHands(self, table):
        self.cards = [-1, -1, -1, -1, -1, -1, -1, -1, -1]  # Max. 9 players
        # Set turns back to starting point
        self.turns = arange(0, self.NPLAYERS)
        self.index = 0
        # Give 6 random cards to players and remove from deck
        for i in range(self.NPLAYERS):
            self.cards[i] = table.deck[0]
            table.deck = delete(table.deck, 0)
            for j in range(5):
                self.cards[i] = append(self.cards[i], table.deck[0])
                table.deck = delete(table.deck, 0)

                # Returns player's turn

    def getPlayerTurn(self):
        return self.turns[self.index]  # player goes from 0 to NPLAYERS-1

    # Returns vector of moves (elements from -2 to 6)
    def getPossibleMoves(self, table, player):
        # RETURNS A VECTOR moves which contains numbers from -2 to 6
        # Trivial moves
        moves = zeros(2, dtype=int)
        moves[0] = -2
        moves[1] = -1

        # Check for possible cards throws
        for i in range(len(self.cards[player])):
            if table.pile[len(table.pile) - 1] == 6:
                if self.cards[player][i] == 6 or self.cards[player][i] == 0:
                    # Check if this move has been added before
                    if len(where(moves == self.cards[player][i])[0]) == 0:
                        moves = append(moves, self.cards[player][i])
            else:
                if self.cards[player][i] == table.pile[len(table.pile) - 1] or self.cards[player][i] == table.pile[
                    len(table.pile) - 1] + 1:
                    # Check if this move has been added before
                    if len(where(moves == self.cards[player][i])[0]) == 0:
                        moves = append(moves, self.cards[player][i])

        return moves  # Contains at least two elements (-2, -1) and maximum 4.

    # Returns the state of the game
    def evaluate(self, table):
        # Check if there is only one player playing
        if len(self.turns) == 1:
            res = self.endRound(table, self.turns[0])
            return res

        for i in range(self.NPLAYERS):
            # Check if player i run out of cards
            if len(self.cards[i]) == 0:
                res = self.endRound(table, i)
                return res

        return self.CONTINUE

        # Add points and restart a new round if game has not finished

    def endRound(self, table, winner):
        # Add the win of the round to the player who won
        self.rounds[winner] += 1

        # Add the points
        for j in range(self.NPLAYERS):
            nLamas = len(where(self.cards[j] == 0)[0])
            nPoints = sum(self.cards[j]) + nLamas * 10
            self.points[j] += nPoints

        # Check if game ended
        if len(where(self.points >= 40)[0]):
            return self.FINISHED

        else:
            # Restart round
            table.restartTable()
            self.restartHands(table)
            return self.CONTINUE

            # Make move and update turn

    def makeMove(self, table, player, move):
        # Fold
        if move == -2:
            # Fold
            i = where(self.turns == player)
            self.turns = delete(self.turns, i)  # This already updates the turn
            # We removed one player, so we need to check if we are at the end of the vector turns
            if self.index == len(self.turns):
                self.index = 0

        # Take a card from deck
        elif move == -1:
            # See if there are cards in deck
            if table.cardsOnDeck() == False:
                table.shuffleDeck()

            # Get card from deck
            self.cards[player] = append(self.cards[player], table.deck[0])
            table.removeFromDeck()

            # Update turn
            if self.index == len(self.turns) - 1:
                self.index = 0
            else:
                self.index += 1

        # Add card to pile
        else:
            # Add card to pile
            table.addToPile(move)
            # Remove card from hand
            j = where(self.cards[player] == move)
            self.cards[player] = delete(self.cards[player],
                                        j[0][0])  # Remove the card from the hand (only one if there are multiple)

            # Update turn
            if self.index == len(self.turns) - 1:
                self.index = 0
            else:
                self.index += 1