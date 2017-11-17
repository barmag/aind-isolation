"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_winner(player) or game.is_loser(player):
        return game.utility(player) 

    # moves = len(game.get_legal_moves())

    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(-opp_moves)


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_winner(player) or game.is_loser(player):
        #print('end of tree')
        return game.utility(player) 

    moves = len(game.get_legal_moves())
    opponent = game.get_opponent(player)
    opp_moves = len(game.get_legal_moves(opponent))
    # w, h = game.width / 2., game.height / 2.
    # y, x = game.get_player_location(player)
    # center_w = float((h - y)**2 + (w - x)**2)/4
    my_loc_x, my_loc_y = game.get_player_location(player)
    opp_loc_x, opp_loc_y = game.get_player_location(opponent)
    # distance = ((my_loc_x-opp_loc_x) ** 2) + ((my_loc_y-opp_loc_y) ** 2)
    open_locations = game.get_blank_spaces()
    #print("open locations {}".format(len(open_locations)))
    blanks_in_proximity = len([(i, j) for i in range(-2,2) for j in range(-2,2) if (my_loc_x+i, my_loc_y+j) in open_locations])
    opp_blanks_in_proximity = len([(i, j) for i in range(-2,2) for j in range(-2,2) if (opp_loc_x+i, opp_loc_y+j) in open_locations])
    #print("blanks {}".format(blanks_in_proximity))
    # return (float(2*moves - opp_moves) + float(moves - 2*opp_moves) + float(moves-opp_moves))
    # moves_ahead = sum([len(game.forecast_move(m).get_legal_moves(opponent)) for m in game.get_legal_moves()])
    # opp_moves_head = sum([len(game.forecast_move(m).get_legal_moves(player)) for m in game.get_legal_moves(opponent)])
    # use only blanks in proximity, win rate 45% against AB_Improved (bad)
    return float(moves-opp_moves) + float(blanks_in_proximity-opp_blanks_in_proximity)
    # return float(moves-opp_moves) + float(moves_ahead-opp_moves_head)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_winner(player) or game.is_loser(player):
        return game.utility(player) 
    # moves = len(game.get_legal_moves())
    open_locations = game.get_blank_spaces()
    opponent = game.get_opponent(player)

    #beginning of the game
    if len(open_locations) > (game.width*game.height)-12:
        return len(game.get_legal_moves(player))

    # mid game
    # if len(open_locations) > game.width*game.height/2:
    else:
        return float(len(game.get_legal_moves(player))-len(game.get_legal_moves(opponent)))


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            print('minimax timeout')
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        #print (game.active_player)
        player = game.get_opponent(game.active_player)
        moves = game.get_legal_moves()
        # print(moves)
        if not moves:
            return (-1, -1)
        best_move = moves[0]
        best_move = max(moves, key=lambda m: self.min_value(game.forecast_move(m), depth))
        #print(move)
        return best_move

    def max_value(self, game, depth):
        """ Return the value of score if the game is over,
        otherwise return the max value over all legal children
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        depth = depth - 1
        if self.terminal_state(game, depth):
            return self.score(game, self)

        v = max(map(lambda m : self.min_value(game.forecast_move(m), depth), game.get_legal_moves()))
        return v
    
    def min_value(self, game, depth):
        """ Return the value of score if the game is over,
        otherwise return the min value over all legal children
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        depth = depth - 1
        if self.terminal_state(game, depth):
            return self.score(game, self)
        
        v = min(map(lambda m : self.max_value(game.forecast_move(m), depth), game.get_legal_moves()))
        return v
    
    def terminal_state(self, game, depth):
        """ Return true if we reached maximum depth
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth <= 0:
            return True
        moves = game.get_legal_moves()
        if not moves:
            return True
        return False

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        self.best_move = (-1, -1)
        max_depth = 49
        self.d = 0
        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            # return self.alphabeta(game, self.search_depth)
            for d in range(1, max_depth):
                self.best_move = self.alphabeta(game, d)
                if self.best_move == (-1,-1):
                    # print('out of moves')
                    break
                self.d = d

        except SearchTimeout:
            # print ("explored depth {}".format(self.d))
            return self.best_move  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return self.best_move


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        moves = game.get_legal_moves()
        if not moves:
            return (-1, -1)
        best_action = moves[0]
        for a in moves:
            v = self.min_value(game.forecast_move(a), depth-1, alpha, beta)
            if v > alpha:
                alpha = v
                best_action = a

        return best_action

    def max_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_state(game, depth):
            return self.score(game, self)
        v = float('-inf')
        for a in game.get_legal_moves():
            v = max(v, self.min_value(game.forecast_move(a), depth-1, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
    
    def min_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_state(game, depth):
            return self.score(game, self)
        v = float('inf')
        for a in game.get_legal_moves():
            v = min(v, self.max_value(game.forecast_move(a), depth-1, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def terminal_state(self, game, depth):
        """ Return true if we reached maximum depth
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth <= 0:
            return True
        moves = game.get_legal_moves()
        if not moves:
            return True
        return False
