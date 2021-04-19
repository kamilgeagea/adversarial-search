'''
Determines if n is a factor of m
Arguments:
    - n: Number
    - m: Number
Returns Boolean
'''


def is_factor(n, m):
    return m % n == 0


'''
Determines if n is a multiple of m
Arguments:
    - n: Number
    - m: Number
Returns Boolean
'''


def is_multiple(n, m):
    return n % m == 0


'''
Determines if n is prime
Arguments:
    - n: Number
Returns Boolean
'''


def is_prime(n):
    return all(n % i for i in range(2, n))


'''
Determines if a token is valid to be picked up
Arguments:
    - token: Number
    - last_picked_token: Number
Returns Boolean
'''


def is_valid(token, last_picked_token):
    return is_factor(token, last_picked_token) or is_multiple(token, last_picked_token)


'''
Determines if the game is over (no more available moves)
Arguments:
    - token: List of Numbers
    - last_picked_token: Number
Returns Boolean  
'''


def game_over(tokens, last_picked_token):
    # Loop through all the tokens
    for token in tokens:
        # If any token is valid, then the game is not over
        if is_valid(token, last_picked_token):
            return False

    return True


'''
Generates all possible states, by generating a state after picking each valid token
Arguments:
    - tokens: List of Numbers
    - last_picked_token: Number
    - depth: Number
Returns List of tuples (new_tokens: List of Numbers, picked_token: Number, new_depth: Number)
'''


def generate_children(tokens, last_picked_token, depth):
    # Determines if it is the first move by checking depth
    first_move = depth == 0

    children = []

    if first_move:
        # Computing half of the length of tokens
        n = len(tokens) / 2.0

        # If the token is less than n, and token is odd, then it is a valid move
        valid_moves = [token for token in tokens if token <
                       n and token % 2 != 0]

        # For each valid move, append a tuple with the new state after removing the move
        for move in valid_moves:
            children.append(
                ([token for token in tokens if token != move], move, depth + 1))
    else:
        # If not first move
        # For each token, if token is valid, append a tuple with the new state after removing the token
        for token in tokens:
            if is_valid(token, last_picked_token):
                children.append(
                    ([element for element in tokens if element != token], token, depth + 1))

    return children
