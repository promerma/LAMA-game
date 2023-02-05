from Class_Table import Table
from Class_Hands import Hands
from Functs import nextMove, playGame
from numpy import ones, zeros, where, mean

#Number of players
Nplay = 4
#Strategies
strats = ones(4)
res=zeros(Nplay, dtype=int)
Ngames=10
for i in range(Ngames):
    #create objects
    table = Table()
    hands = Hands(Nplay, table)
    #Play a game
    game = playGame(table, hands, strats)
    res[game] += 1
print(res)

print(res[0]/Ngames)
print(res[1]/Ngames)
print(res[2]/Ngames)
print(res[3]/Ngames)