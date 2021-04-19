from alpha_beta_pruning import alpha_beta_pruning

# 7 1 1 2

# tokens = [1, 2, 3]
# depth = 0
# state = (tokens, None, depth)
# alpha = float("-inf")
# beta = float("+inf")
# max_depth = 0

# tokens = [2, 3, 4, 5, 6, 7]
# taken_tokens = 1
# list_of_taken_tokens = [1]

# last_token = 1
# depth = 1
# state = (tokens, last_token, depth)
# alpha = float("-inf")
# beta = float("+inf")
# max_depth = 3

# 10 3 4 2 6 4
# tokens = [1, 3, 5, 7, 8, 9, 10]
# taken_tokens = 3
# list_of_taken_tokens = [4, 2, 6]
# last_token = 6
# depth = 3
# state = (tokens, last_token, 3)
# alpha = float("-inf")
# beta = float("inf")
# max_depth = 4 + 3

# 8 3 3 1 2 0
# tokens = [4, 5, 6, 7, 8]
# taken_tokens = 3
# depth = 3
# list_of_taken_tokens = [3, 1, 2]
# max_depth = 0
# last_token = 2

# state = (tokens, last_token, depth)
# alpha = float("-inf")
# beta = float("inf")

# 10 5 3 1 8 4 2 0
tokens = [5, 6, 7, 9, 10]
taken_tokens = 5
depth = 5
list_of_taken_tokens = [3, 1, 8, 4, 2]
max_depth = 0
last_token = 2

state = (tokens, last_token, depth)
alpha = float("-inf")
beta = float("inf")


(move, value, nb_visited_nodes, nb_evaluated_nodes, max_depth_reached) = alpha_beta_pruning(
    state, alpha, beta, max_depth)
print("Value: " + str(value))
print("Move: " + str(move))
print("Number of Nodes Visited: " + str(nb_visited_nodes))
print("Number of Nodes Evaluated: " + str(nb_evaluated_nodes))
print("Max Depth Reached: " + str(max_depth_reached - depth))
print("Average Branching Factor: ")
