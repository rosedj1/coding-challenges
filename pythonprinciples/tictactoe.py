"""<Brief description>

Author: Dr. Jake Rosenzweig
Date: 2023-11-14

Challenge: Tic tac toe input
Difficulty: 4/10
URL: https://pythonprinciples.com/challenges/Tic-tac-toe-input/

Here's the backstory for this challenge:
imagine you're writing a tic-tac-toe game, where the board looks like this:

1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |

    A   B  C

The board is represented as a 2D list:

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

Imagine if your user enters "C1" and you need to see if there's an X or O in
that cell on the board. To do so, you need to translate from the string "C1"
to row 0 and column 2 so that you can check board[row][column].

Your task is to write a function that can translate from strings of length 2
to a tuple (row, column). Name your function get_row_col; it should take a
single parameter which is a string of length 2 consisting of an uppercase
letter and a digit.

For example, calling get_row_col("A3") should return the tuple (2, 0) because
A3 corresponds to the row at index 2 and column at index 0 in the board.

#=======================#
#=== Lessons Learned ===#
#=======================#
* My solution was basically identical to the example solution!
"""
dct_col = {'A':0, 'B':1, 'C':2}

def get_row_col(spot):
    """Return a 2-tuple (row, col) based on user's input `spot`."""
    # Make sure the input is valid.
    assert spot in "A1 A2 A3 B1 B2 B3 C1 C2 C3".split()
    label_col = spot[0]
    label_row = spot[1]

    correct_col = dct_col[label_col]
    # Since A3 should return (2, 0) and A1 should return (0, 0),
    # then `label_row` is one unit bigger than it needs to be.
    correct_row = int(label_row) - 1
    
    return (correct_row, correct_col)

# Example solution:
def get_row_col_egsoln(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    number = choice[1]
    row = int(number) - 1
    column = translate[letter]
    return (row, column)

if __name__ == "__main__":
    print(f'''Should return tuple (0, 0): {get_row_col("A1")}''')
    print(f'''Should return tuple (1, 0): {get_row_col("A2")}''')
    print(f'''Should return tuple (2, 0): {get_row_col("A3")}''')
    print(f'''Should return tuple (0, 1): {get_row_col("B1")}''')
    print(f'''Should return tuple (1, 1): {get_row_col("B2")}''')
    print(f'''Should return tuple (2, 1): {get_row_col("B3")}''')
    print(f'''Should return tuple (0, 2): {get_row_col("C1")}''')
    print(f'''Should return tuple (1, 2): {get_row_col("C2")}''')
    print(f'''Should return tuple (2, 2): {get_row_col("C3")}''')
