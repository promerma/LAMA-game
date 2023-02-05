from Class_Table import Table
from Class_Hands import Hands

from numpy import where, unique, zeros,argmin, where, ones, zeros, array, mean, sum, divide, std, sqrt
from statsmodels.stats.weightstats import DescrStatsW



# Computes next move
def nextMove(table, hands, player, strat):
    # Strategy 1: throws the lowest card, if not draw from deck
    if strat == 1:
        # Get possible moves
        moves = hands.getPossibleMoves(table, player)
        # if he cannot play, then draw from deck
        if len(moves) == 2:
            return -1
        else:
            indexs = where(hands.cards[player] == table.pile[len(table.pile) - 1])
            if len(indexs[0]) > 0:
                return hands.cards[player][indexs[0][0]]
            else:
                if table.pile[len(table.pile) - 1] == 6:
                    return 0
                else:
                    return table.pile[len(table.pile) - 1] + 1

    if strat == 2:
        # Get possible moves
        moves = hands.getPossibleMoves(table, player)
        # if he cannot play, then draw from deck
        if len(moves) == 2:
            return -1
        else:
            if table.pile[len(table.pile) - 1] == 6:
                # If we have a Lama, throw it
                indexs = where(hands.cards[player] == 0)
                if len(indexs[0]) > 0:
                    return 0
                else:
                    return 6
            else:
                indexs = where(hands.cards[player] == table.pile[len(table.pile) - 1] + 1)
                if len(indexs[0]) > 0:
                    return table.pile[len(table.pile) - 1] + 1
                else:
                    return table.pile[len(table.pile) - 1]

    if strat == 3:
        # Get possible moves
        moves = hands.getPossibleMoves(table, player)
        #If he can play, then play
        if len(moves) > 2:
            #Same as in 1
            if hands.NPLAYERS < 7:
                indexs = where(hands.cards[player] == table.pile[len(table.pile) - 1])
                if len(indexs[0]) > 0:
                    return hands.cards[player][indexs[0][0]]
                else:
                    if table.pile[len(table.pile) - 1] == 6:
                        return 0
                    else:
                        return table.pile[len(table.pile) - 1] + 1

            #Same as in 3
            else:
                # If there is a 6 look for a 0
                if table.pile[len(table.pile) - 1] == 6:
                    ind0 = where(hands.cards[player] == 0)
                    if len(ind0[0]) > 0:
                        return 0
                    else:
                        return 6
                else:
                    indexs = where(hands.cards[player] == table.pile[len(table.pile) - 1])
                    if len(indexs[0]) > 0:
                        return hands.cards[player][indexs[0][0]]
                    else:
                        if table.pile[len(table.pile) - 1] == 6:
                            return 0
                        else:
                            return table.pile[len(table.pile) - 1] + 1

        #If he cannot play
        else:
            value = 0
            #Default parameters (useless here, just as reference)
            A = 10
            B = 5
            C = 4.4
            D = 1

            #Based on different cards
            dif_cards = len(unique(hands.cards[player]))
            if dif_cards == 1:
                #folding points
                value -= A
            else:
                value += B*dif_cards

            #Based on number of points
            nLamas = len(where(hands.cards[player] == 0)[0])
            nPoints = sum(hands.cards[player]) + nLamas * 10
            value += (nPoints-C)

            #Based on time to end round
            Ncards = zeros(hands.NPLAYERS, dtype=int)
            for i in range(hands.NPLAYERS):
                Ncards[i] = len(hands.cards[i])

            value += D*min(Ncards)

            if value >= 0:
                return -1
            else:
                return -2


# Play a game
def playGame(table, hands, strats):  # strats is a vector with the strategy of each player
    score = hands.evaluate(table)
    while (score == hands.CONTINUE):
        # Get player turn
        player = hands.getPlayerTurn()
        # Compute next move
        move = nextMove(table, hands, player, strats[player])
        # Make move
        hands.makeMove(table, player, move)
        # evaluate
        score = hands.evaluate(table)

    # HERE GAME ENDED
    # Return player(s) who win
    return where(hands.points == hands.points.min())[0]


#Computes the confidence intervals
def cal_confident_int(sim, zalpha=1.96):
    """
    Calculate the confident interval for sim data

    Parameters
    ----------
    sim : TYPE
        sample values
    zalpha : TYPE, optional
        # 97.5% quantile of the normal distribution. The default is 1.96.

    Returns
    -------
    Confidence interval

    """
    Xavg = mean(sim)  # estimate for E[X]
    Sn = std(sim)
    # 97.5% quantile of the normal distribution
    halfWidth = zalpha * Sn / sqrt(len(sim))
    ci = (Xavg - halfWidth, Xavg + halfWidth)  # confidence interval for E[X]
    #print(ci)
    #print('halfWidth = ' + str(halfWidth))
    ci1 = DescrStatsW(sim).tconfint_mean(alpha=0.05)
    #print('Confidence interval from scipy' + str(ci1))
    return ci