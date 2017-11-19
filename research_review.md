# Research Review
I have read the three papers and in this summary will provide a brief review of all of them, but with emphasis on AlphaGo as it presents the state of the art in gameplay AI.

## Game Tree Searching by Min/Max Approximation
This paper uses a different search algorithm from the techniques presented during the course. In Minimax all the options are explored to find the best action, Alphabeta optimizes Minimax by ignoring nodes that will not impact the final decision. Instead this paper uses iterative search, which iteratively tries to select a single best course of action, explores it then backpropagate the result of exploration and see if that course of action is still the best or another path should be explored. This paper uses a Minimax approximation with generalized mean-valued operator to guide the selection of next leaf node to expand.
Generalized mean values is an approximation to min/max values, but is derivable, which is more suitabe to sensitivity analysis. It is used to calculate weights to determine which node, the value in the parent node depends the most on, and selects it for expansion.
After trying this technique with 1000 games of Connect-Four the Min/Max approximation with iterative search proved to be superior to Alphabeta for the same number of calls to the basic move subroutine, but Alphabeta wins if the bound resource is time, because it is faster and could explore more nodes for the same allotted time.

## Deep Blue
This paper describes Deep Blue system, which defeated the chess world champion Garry Kasparov