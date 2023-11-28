from collections import deque

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def get_blank_position(board):
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == 0:
                return i, j

def is_valid_move(i, j):
    return 0 <= i < 3 and 0 <= j < 3

def make_move(board, move):
    i, j = get_blank_position(board)
    ni, nj = i + move[0], j + move[1]
    new_board = [row[:] for row in board]
    new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
    return new_board

def get_neighbors(board):
    i, j = get_blank_position(board)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []

    for move in moves:
        ni, nj = i + move[0], j + move[1]
        if is_valid_move(ni, nj):
            neighbors.append(make_move(board, move))

    return neighbors

def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        visited.add(tuple(map(tuple, current_state)))

        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

if __name__ == "__main__":
    initial_board = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    goal_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    solution_path = bfs(initial_board, goal_board)

    if solution_path:
        print("Solution found!")
        for step, board in enumerate(solution_path):
            print(f"Step {step + 1}:")
            print_board(board)
    else:
        print("No solution found.")
