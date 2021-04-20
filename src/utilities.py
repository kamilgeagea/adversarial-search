import random
import re

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


'''
Generates a test case by playing the game with random values
Arguments: None
Returns tuple (m, move, list_of_picked_tokens, max_depth)
'''


def generate_test_case():
    # Step 1 - Generate tokens
    n = random.randint(10, 30)
    tokens = list(range(1, n))

    # Step 2 - Generate nb of moves
    nb_moves = random.randint(0, 5)

    # Step 3 - Generate max_depth
    max_depth = random.randint(0, 5)

    # Step 4 - Play n moves
    move = 0
    last_token = None
    list_of_picked_tokens = []
    while move < nb_moves:
        children = generate_children(tokens, last_token, move)
        random.shuffle(children)
        (new_tokens, picked_token, depth) = children[0]
        tokens = new_tokens
        list_of_picked_tokens.append(picked_token)
        last_token = picked_token
        move = depth
    return (n, move, list_of_picked_tokens, max_depth)


'''
Generates multiple test cases
Argument:
    - n: number
Returns list of tuples (m, move, list_of_picked_tokens, max_depth)
'''


def generate_test_cases(n):
    test_cases = []
    for i in range(0, n):
        try:
            test_cases.append(generate_test_case())
        except:
            ""
    return test_cases


'''
Generates the output of generate_test_cases and put it into a file
Arguments:
    - filename: string
    - n: number
Returns void
'''


def generate_test_case_file(filename, n):
    test_cases = generate_test_cases(n)
    with open(filename, mode="w") as f:
        for (n, move, list_of_picked_tokens, max_depth) in test_cases:
            f.write("TakeTokens " + str(n) + " " + str(move) + " " +
                    "".join([str(picked_token) + " " for picked_token in list_of_picked_tokens]) + str(max_depth) + "\n")
        f.close()


'''
Generates a file containing formatted output of the alpha beta pruning algorithm
Arguments:
    - filename: string
    - abp_list: list of alpha beta results - (result: number, move: number, visited_nodes: number, evaluated_nodes: number, max_depth_reached: number, parent_count: number)
Returns void
'''


def generate_output(filename, abp_list):
    with open(filename, mode="w") as f:
        for idx, abp in enumerate(abp_list):
            (result, move, visited_nodes, evaluated_nodes,
             max_depth_reached, parent_count) = abp
            # Calculate Average Effective Branching Factor
            avg_effective_branching_factor = float(
                (visited_nodes-1)) / parent_count
            f.write("Case " + str(idx)
                    + "\nMove: " + str(move)
                    + "\nValue: " + str(float(result))
                    + "\nNumber of Nodes Visited " + str(visited_nodes)
                    + "\nNumber of Nodes Evaluated " + str(evaluated_nodes)
                    + "\nMax Depth Reached: " + str(max_depth_reached)
                    + "\nAvg Effective Branching Factor: " +
                    str(avg_effective_branching_factor)
                    + "\n\n")


'''
Function that extracts the input from formatted text files
Arguments:
    - filename: string
Returns list tuple: (tokens: list of numbers, last_token: number, depth: number, max_depth: number)
'''


def extract_input(filename):
    inputs = []
    with open(filename) as f:
        # Extract test cases from file
        test_cases = list(f)
        # Remove \n
        test_cases = [case.strip("\n") for case in test_cases]
        # From "TakeTokens 1 2 3 4 5" -> [1, 2, 3, 4, 5]
        test_cases = [[ele for ele in case.split(" ") if ele.isdigit()]
                      for case in test_cases if "TakeTokens" in case]
        for case in test_cases:
            case = [int(c) for c in case]
            tokens = range(1, case.pop(0)+1)
            depth = case.pop(0)
            max_depth = case.pop() + depth
            list_of_taken_tokens = case
            last_token = list_of_taken_tokens[-1] if len(
                list_of_taken_tokens) > 0 else None
            tokens = list(set(tokens) - set(list_of_taken_tokens))
            inputs.append((tokens, last_token, depth, max_depth))
    return inputs
