# LAMA-game

![alt text](https://github.com/promerma/LAMA-game/blob/main/Lama.webp)

This repository contains an implementation of a Dicrete-Event simulation of the LAMA game in Python. This project was done as an assignment from the MSc level course "Advanced Simulation" at the Eindhoven University of Technology on February 21st, 2022.


# Description of the files

(1) Class_Hands.py: Contains the definition of the class Hands, which performs the actions involving the cards in each player's hands.

(2) Class_Table.py: Contains the definition of the class Table, which performs the actions involving the cards that in the table where the game is being played.

(3) Functs.py: Contains the implementation of the strategies that the players can follow, the implementation of the game itself and the implementation of a function to perform a statistical analysis of the game outcomes.

(4) main.py: Executes the games and compute winning rates.

(5) LAMA-game.pdf: Contains a full explanation of the code and an analysis of the different strategies.


# Description of the possible strategies

Strategy 1: In this strategy, the players never fold. They will only draw a new card from the deck, if they cannot discard any of the cards they are holding. If they can choose between multiple cards to discard, they will discard the lowest card number (which is equal to the number of the card that is lying on top of the discard pile). 

Strategy 2: Same as Strategy 1 , but now if a player can choose between multiple cards to discard, they will discard the highest card number (which is 1 higher than the number of the card that is lying on top of the discard pile).

Strategy 3: A Monte Carlo-based approach that includes folding as a possible action.  
