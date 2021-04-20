from utilities import game_over, is_prime, is_multiple, is_factor, generate_children

'''
Function that calculates the Static Board Evaluation
Arguments:
    - tokens: List of Numbers
    - last_picked_token: Number
    - is_max: Boolean
    - Depth: Number
Returns a Number between -1 and 1
'''


def e(tokens, last_picked_token, is_max, depth):
    # The output calculated below indicate the advantage of each player
    # If the number is negative, the output favors MIN
    # If the number is positive, the output favors MAX
    # factor determines whether the output should favor MIN or MAX
    factor = 1 if is_max else -1

    if 1 in tokens:
        return 0

    if game_over(tokens, last_picked_token):
        return - factor

    if last_picked_token == 1:
        odd_valid_moves = len(tokens) % 2 != 0
        return factor * 0.5 if odd_valid_moves else -0.5 * factor
    if is_prime(last_picked_token):
        children = generate_children(
            tokens, last_picked_token, depth)
        count = 0
        for child in children:
            for element in child[0]:
                if is_multiple(element, last_picked_token):
                    count += 1
        odd_count = count % 2 != 0
        return factor * 0.7 if odd_count else factor * -0.7
    else:
        for token in reversed(tokens):
            if is_prime(token) and is_factor(token, last_picked_token):
                children = generate_children(
                    tokens, last_picked_token, depth)
                count = 0
                for child in children:
                    for element in child[0]:
                        if is_multiple(element, token):
                            count += 1
                odd_count = count % 2 != 0
                return factor * 0.6 if odd_count else factor * -0.6
