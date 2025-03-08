def minimax(board, depth, is_maximizing, ai_strategy):
    if depth == 0 or is_terminal_pos(board):
        if ai_strategy:
            return evaluate_aggressive_ai(board), None
        else:
            return evaluate(board), None
    if is_maximizing:
        best_score = float("-inf")
    else:
        best_score = float("inf")

    best_move = None
    possible_moves = get_moves(board)

    for move in possible_moves:
        i, j = move
        if is_maximizing:
            board[i][j] = "O"
            new_score, _ = minimax(board, depth - 1, False, ai_strategy)
            board[i][j] = ""
            if new_score > best_score:
                best_score = new_score
                best_move = move
        else:
            board[i][j] = "X"
            new_score, _ = minimax(board, depth - 1, True, ai_strategy)
            board[i][j] = ""
            if new_score < best_score:
                best_score = new_score
                best_move = move

    return best_score, best_move


def alpha_beta_pruning(board, depth, is_maximizing, ai_strategy, alpha, beta):
    if depth == 0 or is_terminal_pos(board):
        if ai_strategy:
            return evaluate_aggressive_ai(board), None
        else:
            return evaluate(board), None
    if is_maximizing:
        best_score = float("-inf")
    else:
        best_score = float("inf")

    best_move = None
    possible_moves = get_moves(board)

    for move in possible_moves:
        i, j = move
        if is_maximizing:
            board[i][j] = "O"
            new_score, _ = alpha_beta_pruning(board, depth - 1, False, ai_strategy, alpha, beta)
            board[i][j] = ""

            if new_score > best_score:
                best_score = new_score
                best_move = move

            alpha = max(alpha, best_score)
            if alpha >= beta:
                break # Prune the branch
        else:
            board[i][j] = "X"
            new_score, _ = alpha_beta_pruning(board, depth - 1, True, ai_strategy, alpha, beta)
            board[i][j] = ""

            if new_score < best_score:
                best_score = new_score
                best_move = move

            beta = min(beta, best_score)
            if alpha >= beta:
                break  # Prune the branch

    return best_score, best_move

# Check if the board is in a terminal position
def is_terminal_pos(board):
    if all(board[i][j] != "" for i in range(3) for j in range(3)) or check_winner(board) is not None:
        return True
    return False

# Get all possible moves
def get_moves(board):
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                possible_moves.append((i, j))
    return possible_moves

# Evaluate the board
def evaluate(board):
    winner = check_winner(board)
    if winner == "O":
        return 10
    elif winner == "X":
        return -10
    else:
        return 0

# Evaluate the board for aggressive AI
def evaluate_aggressive_ai(board):
    winner = check_winner(board)
    if winner == "O":
        return 50
    elif winner == "X":
        return -50
    else:
        evaluation = 0

        # Check rows and columns
        for i in range(3):
            evaluation += evaluate_line([board[i][0], board[i][1], board[i][2]])
            evaluation += evaluate_line([board[0][i], board[1][i], board[2][i]])

        # Check diagonals
        evaluation += evaluate_line([board[0][0], board[1][1], board[2][2]])
        evaluation += evaluate_line([board[0][2], board[1][1], board[2][0]])

        return evaluation

def evaluate_line(line):
    if line.count("O") == 2 and line.count("") == 1:
        return 25
    elif line.count("X") == 2 and line.count("") == 1:
        return -25
    elif line.count("O") == 1 and line.count("") == 2:
        return 10
    elif line.count("X") == 1 and line.count("") == 2:
        return -10
    else:
        return 0

# Determine who is the winner
def check_winner(board):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]

    #Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None