from utilities import generate_children, game_over
from heuristic import e

'''
This function calculates the best move for a certain position of the game using Alpha-Beta Pruning
Arguments:
    - state: tuple (tokens: List of Numbers, last_token: Number, depth: Number)
    - alpha: Number
    - beta: Number
    - max_depth: Number
Returns tuple (result: Number, move: Number, nb_visited_nodes: Number, nb_evaluated_nodes: Number, max_depth_reached: Number)
'''


def alpha_beta_pruning(state, alpha, beta, max_depth):
    # Extract tokens (current state of the game), last token picked, and current depth from state
    (tokens, last_token, depth) = state

    # Determine if first move
    first_move = depth == 0

    # Determine if current player is MAX
    is_max = depth % 2 == 0

    nb_visited_nodes = 0
    nb_evaluated_nodes = 0
    max_depth_reached = 0
    parent_count = 0

    # Check if not the first move in order to proceed to base case
    if not first_move:
        # If max_depth = 0, we go as deep as the endgame (no heuristics)
        if max_depth == 0:
            # If game over, return results
            if game_over(tokens, last_token):
                result = -1 if is_max else 1
                return (result, None, 1, 1, depth, 0)
        # If max_depth exceeded or game over, return heuristic of state
        elif depth >= max_depth or game_over(tokens, last_token):
            heuristic = e(tokens, last_token, is_max, depth)
            return (heuristic, None, 1, 1, depth, 0)

    if is_max:
        # Set Max Result to -inf, and best move to None
        max_result = float("-inf")
        best_move = None
        children = generate_children(tokens, last_token, depth)
        for child in children:
            # Alpha Beta Pruning call
            (result, _, child_visited_nodes, total_evaluated_nodes, depth_reached, child_parent_count) = alpha_beta_pruning(
                child, alpha, beta, max_depth)
            # If result of alpha-beta pruning greater than max_result, update max_result and best move
            if result > max_result:
                max_result = result
                best_move = child[1]
            alpha = max(alpha, result)
            # Add the child's number of visited node to the current number of visited nodes
            nb_visited_nodes += child_visited_nodes
            # Add the child's number of evaluated node to the current number of evaluated nodes
            nb_evaluated_nodes += total_evaluated_nodes
            # Check if child's max_depth_reached is greater than current max_depth_reached
            max_depth_reached = max(max_depth_reached, depth_reached)
            # Add the child's total parent count
            parent_count += child_parent_count
            # If beta <= alpha -> Prune the rest of the branches
            if beta <= alpha:
                break
        # Increment nb of visited nodes and parent count
        return (max_result, best_move, nb_visited_nodes + 1, nb_evaluated_nodes, max_depth_reached, parent_count + 1)
    else:
        # Set Min Result to -inf, and best move to None
        min_result = float("infinity")
        best_move = None
        children = generate_children(tokens, last_token, depth)
        for child in children:
            # Alpha Beta Pruning call
            (result, _, child_visited_nodes, total_evaluated_nodes, depth_reached, child_parent_count) = alpha_beta_pruning(
                child, alpha, beta, max_depth)
            # If result of alpha-beta pruning less than min_result, update max_result and best move
            if result < min_result:
                min_result = result
                best_move = child[1]
            beta = min(beta, result)
            # Add the child's number of visited node to the current number of visited nodes
            nb_visited_nodes += child_visited_nodes
            # Add the child's number of evaluated node to the current number of evaluated nodes
            nb_evaluated_nodes += total_evaluated_nodes
            # Check if child's max_depth_reached is greater than current max_depth_reached
            max_depth_reached = max(max_depth_reached, depth_reached)
            # Add the child's total parent count
            parent_count += child_parent_count
            # If beta <= alpha -> Prune the rest of the branches
            if beta <= alpha:
                break
        # Increment nb of visited nodes and parent count
        return (min_result, best_move, nb_visited_nodes + 1, nb_evaluated_nodes, max_depth_reached, parent_count + 1)
