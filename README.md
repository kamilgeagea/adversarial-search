# COMP472-Assignment 3
COMP 472 - Assignment 3 - The PNT-Game

# Game Description
The PNT-Game is a two player game that begins with n tokens (labelled with numbers from 1 --> n). Players are to take turns removing a legal numbered tokens. On any given turn, a legal token is defined as: 

       > A Token whose number is a multiple of the last token that was removed.
       > A Token whose number is a factor of the last token that was removed.

If a player cannot pick up a legal token, The game is over and that player is the LOSER.

The <ins>**FIRST**</ins> token to be removed from the game: 
<pre><code>
       > MUST be an ODD number
       > MUST be strickly <ins>LESS THAN</ins> n/2
</code></pre>
### Example Game  
Here is an example of the game being played where n = 7:

<pre><code>
|   MOVE       |  Tokens Left   |
|--------------|----------------|
| Player A: 3  |  1 2 <s><b>3</s></b> 4 5 6 7 |   
| Player B: 6  |  1 2 4 5 <s><b>6</s></b> 7   |
| Player A: 2  |  1 <s><b>2</s></b> 4 5 7     |
| Player B: 4  |  1 <s><b>4</s></b> 5 7       |
| Player A: 1  |  <s><b>1</s></b> 5 7         |
| Player B: 7  |  5 <s><b>7</s></b>           |


Winner: Player B
</code></pre>
 
## Getting Started
**Step 1:** Open a new project on Pycharm (Make sure you have **Python Version 3.8** installed on your computer).\
**Step 2:** Navigate to Pycharm settings

       > (Mac OS: Pycharm -> Preferences -> Project -> Python Interpretor -> "+")
       
       > (Windows OS: File -> Settings -> Project -> Python Interpretor -> "+")

**Step 3:** Clone Project

       > Import this project from Version Control
       
### Import Usage:
Ensure the following Imports are in Main.py File:
```
from alpha_beta_pruning import alpha_beta_pruning
```

## Overall code process and code snippets

**Input:** 
```
The function generate_input('Path_to_file')extracts the following information:
       <#tokens>              --> Number of Tokens in the game
       <#taken_tokens>        --> Number of tokens that have already been removed from the game 
              > If this number is 0, it is the first move of the game
              > If this number is ODD, the current move belongs to Min
              > If this number is EVEN, the current move belongs to Max
       <list_of_taken_tokens> --> An array of tokens that have already been removed from the game. 
       <depth>                --> The search depth. If the depth is 0, this is the state in which a winner is determined.
       
Once the required values have been extracted, input them into alpha-beta function
```
Example:
```
from alpha_beta_pruning import alpha_beta_pruning
from utilities import generate_output, extract_input

# Extract input from testcase/testcase.txt
filename = "./testcases/testcase.txt"
inputs = extract_input(filename)

# Call Alpha-Beta-Pruning on inputs
ab = [alpha_beta_pruning((x[0], x[1], x[2]), float(
    "-inf"), float("inf"), x[3]) for x in inputs]

# Generate output into results/testcases.txt
generate_output("./results/testcases.txt", ab)
```

**Output:**
The following information will be printed to the console
```
The best move (i.e., the tokens number that is to be taken) for the current player (alpha-beta algorithm)
       • The value associated with the move (alpha-beta algorithm)
       • The total number of nodes visited
       • The number of nodes evaluated (either at end game state or when the specified depth is reached)
       • The maximum depth reached (the root node is at depth 0)
       • The average effective branching factor (average number of successors that are not pruned)
```


## Heuristic Function
```
Return 'Values' as follows:
       • At an end game state where Player A (MAX) wins: 1.0
       • At an end game state where Player B (MIN) wins: -1.0 • Otherwise,

o if it is Player A (MAX)’s turn:
       ▪ If token 1 is not taken yet, return a value of 0
       ▪ If the last move was 1, count the number of the possible successors.
              > If the count is Odd, return 0.5.
              > If the count is Even, return -0.5.
       ▪ If last move is a prime, count the multiples of that prime in all possible successors. 
              > If the count is odd, return 0.7.
              > If the count is Even, return -0.7.
       ▪ If the last move is NOT prime, find the largest prime that can divide last move,
       count the multiples of that prime, including the prime number itself if it hasn’t already been taken, in all the possible successors.
              > If the count is odd, return 0.6.
              > If the count is Even, return -0.6.
o If it is Player B(MIN)’s turn, perform the same checks as above, but return the negation of the values specified above.
```

**Code:**
```
h1(tokens, last_picked_token, is_max, depth):
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
```



## Get Help
To get help or ask questions, Please Contact any of the following students: 
 - **Full Name:** Kamil Geagea\
   **Student ID:** 40052432\
   **Github Username:** kamilgeagea\
   **Email Address:** kamilgeagea8199@gmail.com
   
 - **Full Name:** Marjana Upama\
   **Student ID:** 40058393\
   **Github Username:** Marjanaupama\
   **Email Address:** zana.zinly@gmail.com
   
 - **Full Name:** JC Manikis\
   **Student ID:** 26884466\
   **Github Username:** jmanikis\
   **Email Address:** jmanikis@icloud.com
   
 - **Full Name:** Mair Elbaz\
   **Student ID:** 40004558\
   **Github Username:** mairsarmy32\
   **Email Address:** mairelbaz552@hotmail.com
