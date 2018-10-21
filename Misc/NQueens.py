#### COPIED #### VERIFIED

def place_node(node, i, j, N, board, column):
    # IF column j is used, or anybody already there in board[i][j], return Fals
    if column[j] == True or board[i][j] == 1:
        return False
    # we are placing from (0, 0), to (0, N) to (1, 0)... (N-1, N-1).
    # So at any point, we need check the upper parts (where i increases)
    l, m = i, j
    while l >= 0 and m >= 0:
        if board[l][m] == 1:
            return False
        l -= 1  # check only in previous rows. No l += 1
        m -= 1

    l, m = i, j
    while l >= 0 and m < N:
        if board[l][m] == 1:
            return False
        l -= 1  # Check only in previous rows. No l += 1
        m += 1

    board[i][j] = 1  # Place the queen
    column[j] = True
    return True

def clear_place(node, i, j, N, board, column):
    board[i][j] = 0
    column[j] = False

def solve_n_queens(N, board, column, next_node, curr_row):
    if next_node >= N:  # Done with N nodes
        return True

    # for i in range(curr_row, N): # No need to loop through row as one queen in one row
    for j in range(N):  # In a row, queen could be placed in any columnt
        if column[j] is True:  # If any queen is placed in a column, no more can be placed there
                continue

            # See if a next_node queen can be placed in position (i, j)
        if place_node(next_node, curr_row, j, N, board, column) is True:
            if solve_n_queens(N, board, column, next_node + 1, curr_row+1) is True:
                return True
            else: # if cannot be placed, clear the position and continue with same node
                clear_place(next_node, curr_row, j, N, board, column)

    return False

def SolveNqueens(N):
    board = [[0 for i in range(N)] for j in range(N)]  # Create board to place Queens
    column = [False for i in range(N)]  # to speed things up a bit
    visited = [0 for i in range(N)]  # No need of this. as we place nodes one after the other

    # Call internal function. Start with placing 0th Queen
    ret = solve_n_queens(N, board, column, 0, 0) # Start placing queens from row0 to row(n-1)
    for i in range(N):
        print(board[i])
    return ret


if __name__ == '__main__':
    print(SolveNqueens(10))