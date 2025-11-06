# This function resets all player scores in a game to zero
# It makes a copy of the original dictionary, sets each player’s score to 0
# It the returns the updated version without altering the original data.

# The scores() function accepts a dictionary "game_scores" as a parameter
def reset_scores(game_scores):

    # The .copy() dictionary method is used to create a new copy of the "game_scores"
    new_game_scores = game_scores.copy()

    # The for loop iterates over new_game_scores items, with the player as the key and the score as the value
    for player, score in new_game_scores.items():

        # The dictionary operation to assign a new value to a key is used to reset the grade values to 0
        new_game_scores[player] = 0

    return new_game_scores


# The dictionary is defined
game1_scores = {"Jason": 3, "Tom": 7, "Max": 6}

# Call the "reset_scores" function with the "game1_scores" dictionary
print(reset_scores(game1_scores))