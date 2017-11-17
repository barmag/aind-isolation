Heuristic analysis:
First experiment:
Custom 1 is a variation of the Open heurisitc, but instead of the bias towards number of legal moves of the current player, the heurisitic is biased towards limiting number of moves of opponent by returning the negative value of opponet's legal moves. This heuristic performs well against the original Open heurisitc both with Minimax with score 42/8 and Alphabeta with score 27/3. This heurisitic is performing well against other competitiors as well with total win probability of 66% and a good performance against AB_Improved with score 30/20. The definsive nature of the strategy combined with simplicity and high performance gives a good advantage.

Custom 2 tries to enhance the provided improved heuristic by adding a bias towards moves with larger number of open blocks in a 5x5 square. In practice this heurisitic performed worse than improved evaluation with overall win rate of 59.7%

Custom 3 is using a hybrid approach with a strategy at the beginnig different from the end of game. In this experiment we used the number of legal moves for the first 6 moves, then used improved heurisitic for the rest. This heurisitc seemed to perform well with win rate of 64.7% but with room for enhancement especially against vanilla improved evaluation.

Table 1: first experiment
AB_Custom: negative open
AB_Custom_2: AB_Improved with open in proximity
AB_Custom_3: First 6 moves: number of legal moves of player, later AB_Improved
Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       MM_Open     39  |  11    42  |   8    36  |  14    37  |  13
    2      MM_Center    41  |   9    39  |  11    43  |   7    39  |  11
    3     MM_Improved   38  |  12    34  |  16    35  |  15    35  |  15
    4       AB_Open     31  |  19    27  |  23    22  |  28    24  |  26
    5      AB_Center    25  |  25    26  |  24    24  |  26    36  |  14
    6     AB_Improved   24  |  26    30  |  20    19  |  31    23  |  27
--------------------------------------------------------------------------
           Win Rate:      66.0%        66.0%        59.7%        64.7%

Second experiment
Changing the hybrid heurisitc by using the negative open moves as Custom_1 for the first 6 moves. This seems to enhance the results especially agains vanilla improved. The overall win rate is 65%
AB_Custom_3: First 6 moves: negative number of legal moves of opponent, later AB_Improved
 Match #   Opponent    AB_Custom_3
                        Won | Lost
    1       MM_Open     39  |  11
    2      MM_Center    42  |   8
    3     MM_Improved   36  |  14
    4       AB_Open     24  |  26
    5      AB_Center    28  |  22
    6     AB_Improved   26  |  24
--------------------------------------------------------------------------
           Win Rate:      65.0%

Third experiment
Changing the hybrid heurisitic by using a defensive strategy towards the game end by subtracting double the opponent's move from player moves. The end result did not enhance though.

AB_Custom_3: First 10 moves: negative number of legal moves of opponent, later defensive AB_Improved
 Match #   Opponent    AB_Custom_3
                        Won | Lost
    1       MM_Open     34  |  16
    2      MM_Center    44  |   6
    3     MM_Improved   40  |  10
    4       AB_Open     22  |  28
    5      AB_Center    27  |  23
    6     AB_Improved   26  |  24
--------------------------------------------------------------------------
           Win Rate:      64.3%

Fourth experiment
Trying a different configuration for the hybrid heuristic by strating with a strategy favoring center blocks at the beginning, then a defensive negative number of opponent's legal moves, and ending with a defensive variation to the improved heuristic. The overall win rate increased to 66.3%
 Match #   Opponent    AB_Custom_3
                        Won | Lost
    1       MM_Open     35  |  15
    2      MM_Center    46  |   4
    3     MM_Improved   38  |  12
    4       AB_Open     26  |  24
    5      AB_Center    27  |  23
    6     AB_Improved   27  |  23
--------------------------------------------------------------------------
           Win Rate:      66.3%

Fifth experiment
Running all agents at the same experiement with 50 matches against each of the provided heuristics. The hybrid heurisitic still seems to perform best with a small margin.
AB_Custom: negative open
AB_Custom_2: AB_Improved with open in proximity
AB_Custom_3: hybrid eval, center 6 moves, negative open 6 moves, then improved
 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       MM_Open     34  |  16    35  |  15    37  |  13    39  |  11
    2      MM_Center    46  |   4    41  |   9    40  |  10    46  |   4
    3     MM_Improved   32  |  18    30  |  20    34  |  16    33  |  17
    4       AB_Open     31  |  19    29  |  21    29  |  21    28  |  22
    5      AB_Center    28  |  22    26  |  24    20  |  30    25  |  25
    6     AB_Improved   20  |  30    30  |  20    22  |  28    24  |  26
--------------------------------------------------------------------------
           Win Rate:      63.7%        63.7%        60.7%        65.0%


Conclusion:
The hybrid approach is promising and make sense to adjust the strategy according to the game state. There is still rooom for improvement with further experimintation towards optimizing the hybrid evaluation function, but for now this is the selected function.