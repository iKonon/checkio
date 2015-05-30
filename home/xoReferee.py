'''
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3x3 grid. 
The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. 
You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. 
Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).
Output: "X", "O" or "D" as a string.

How it is used: The concepts in this task will help you when iterating data types. 
They can also be used in game algorithms, allowing you to know how to check results.

Precondition:
There is either one winner or a draw. 
len(game_result) == 3
all(len(row) == 3 for row in game_result)
'''

def checkio(game_result):
    match = []
    for i in game_result:
        match.append(list(i))

    for i in match: # rows
        if len(set(i)) == 1 and i[0] != '.':
            return i[0]

    match = list(zip(*match[::-1]))
    for i in match: # columns
        if len(set(i)) == 1 and i[0] != '.':
            return i[0]

    #crossection
    if match[0][0] == match[1][1] == match[2][2] != '.':
        return match[0][0]
    if match[0][2] == match[1][1] == match[2][0] != '.':
        return match[2][0]
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"