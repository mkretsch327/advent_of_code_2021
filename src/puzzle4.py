import numpy as np
import pandas as pd

"""
Part 1:Read in data for numbers and bingo cards, find out which ones are winning
"""
with open('data/puzzle4a.txt', 'r') as f:
    numbers = f.readline()
    numbers = numbers.split(",")
    drawn_numbers = [int(x) for x in numbers]

# Read in boards
board_list = []
board = []
with open('data/puzzle4.txt', 'r') as f:
    for line in f.readlines():
        numbers = line.replace('\n', '')
        if numbers == '':
            board_list.append(board)
            board = []
            continue
        else:
            split_numbers = numbers.split(" ")
            # Remove superfluous empty string spaces
            split_numbers = [x for x in split_numbers if x != '']
            board.append([int(x) for x in split_numbers])
    # Get one last append
    board_list.append(board)
# Convert board list to board array
array_list = [np.array(x) for x in board_list[1:]]
board_array = np.stack(array_list)

# Now loop over draws, and "Play"
# Indicator array
ind_array = np.zeros_like(board_array, dtype=np.int)
for draw in drawn_numbers:
    # Mark where we've drawn
    ind_array += (board_array == draw).astype(int)
    # check if it's a "winner"
    idx_row_idx, row_idx = (ind_array.sum(axis=1)==5).nonzero()
    idx_col_idx, col_idx = (ind_array.sum(axis=2)==5).nonzero()

    if row_idx.size> 0 or col_idx.size > 0:
        if col_idx.size > 0:
            winning_board_idx = idx_col_idx[0]
        if row_idx.size > 0:
            winning_board_idx = idx_row_idx[0]
        winning_board = board_array[winning_board_idx, :, :]
        break
winning_ind = ind_array[winning_board_idx, : , :]
sum_uncalled = ((-1*(winning_ind - 1))*winning_board).sum()    
print(f" Winningi board id: {winning_board_idx}, product is {draw*sum_uncalled}")


""" Part 2: Find out the last scard to win"""

# Now loop over draws, and "Play"
# Indicator array
ind_array = np.zeros_like(board_array, dtype=int)
winner_list = []
for draw in drawn_numbers:
    # Mark where we've drawn
    ind_array += (board_array == draw).astype(int)
    # check if it's a "winner"
    idx_row_idx, row_idx = (ind_array.sum(axis=1)==5).nonzero()
    idx_col_idx, col_idx = (ind_array.sum(axis=2)==5).nonzero()

    if row_idx.size> 0 or col_idx.size > 0:
        if col_idx.size > 0:
            winners = set(idx_col_idx.tolist())
            
            new_winners = list(winners - set(winner_list))
            winner_list += new_winners
        if row_idx.size > 0:
            winners = set(idx_row_idx.tolist())
            new_winners = list(winners - set(winner_list))
            winner_list += new_winners

last_winner = winner_list[-1]
starting_board = board_array[last_winner, :, :]

for draw in drawn_numbers:
    x,y = np.where(starting_board == draw)
    if starting_board[x,y].size > 0:
        starting_board[x,y] -= draw
    if np.any(starting_board.sum(axis=0) == 0) or np.any(starting_board.sum(axis=1) == 0):
        break

sum_uncalled = starting_board.sum()   
print(f" Winning board id:{last_winner}, product is {draw*sum_uncalled}")
