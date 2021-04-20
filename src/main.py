from alpha_beta_pruning import alpha_beta_pruning
from utilities import generate_test_case_file, generate_output, extract_input

# TEST CASES

filename = "./testcases/testcase.txt"
inputs = extract_input(filename)

ab = [alpha_beta_pruning((x[0], x[1], x[2]), float(
    "-inf"), float("inf"), x[3]) for x in inputs]


generate_output("./results/testcases.txt", ab)


# RANDOM TEST CASES

filename = "./testcases/random_testcases.txt"
# generate_test_case_file(filename, 10)
inputs = extract_input(filename)

ab = [alpha_beta_pruning((x[0], x[1], x[2]), float(
    "-inf"), float("inf"), x[3]) for x in inputs]

generate_output("./results/random_testcases.txt", ab)
