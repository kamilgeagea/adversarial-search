from alpha_beta_pruning import alpha_beta_pruning
from utilities import generate_test_case_file, generate_output, extract_input

# TEST CASES

# Extract input from testcase.txt
filename = "./testcases/testcase.txt"
inputs = extract_input(filename)

# Call Alpha-Beta-Pruning on inputs
ab = [alpha_beta_pruning((x[0], x[1], x[2]), float(
    "-inf"), float("inf"), x[3]) for x in inputs]

# Generate output into testcases.txt
generate_output("./results/testcases.txt", ab)


# RANDOM TEST CASES

# Extract input from random_testcases.txt
filename = "./testcases/random_testcases.txt"
inputs = extract_input(filename)

# Call Alpha-Beta-Pruning on inputs
ab = [alpha_beta_pruning((x[0], x[1], x[2]), float(
    "-inf"), float("inf"), x[3]) for x in inputs]

# Generate output into random_testcases.txt
generate_output("./results/random_testcases.txt", ab)
