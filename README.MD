# Chess AI

A Chess AI program utilizing **Minimax** and **Alpha Beta Pruning** algorithms to optimize chess moves.

* **Minimax** – The Minimax algorithm uses recursion to search through the game tree and returns the optimal move for the player. The algorithm assumes that the opponent (the minimizer) is rational and will attempt to minimize our utility. Taking this into account, the algorithm will return a move that maximizes the utility for the maximizer.

* **Alpha Beta Pruning** – Alpha Beta Pruning is more efficient than Minimax because it does not evaluate branches that will not be searched, which occurs when there is already a better move available. To do so, we track two extra variables, *alpha* and *beta*. 

    Alpha is the best already-explored value for the maximizer, while beta is the best already-explored value for the minimizer. If the value presented to the maximizer at a given level is greater than beta, then we would not continue to explore that branch, as that branch will not be chosen by the minimizer. Conversely, if the value presented to the minimizer is smaller than alpha, we will stop, because the maximizer will not choose that branch.

**Utility** – The utility will be calculated using a weighted sum of the remaining chess pieces for each player.

### Usage

- To run test_chess.py: `python3 test_chess.py`

    - Note: Feel free to change the player or the depth. MinimaxAI, AlphaBetaAI, and IDS_MinimaxAI take an integer as depth.
