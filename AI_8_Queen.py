def is_safe(board, row, col):
    for i in range(row):
        # Check if there is a queen in the same column or diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])  # Found a solution
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)

def solve_n_queens(n):
    solutions = []
    solve_n_queens_util([-1] * n, 0, n, solutions)
    return solutions

def print_solution(solution):
    for row in solution:
        print(" ".join("Q" if i == row else "." for i in range(len(solution))))
    print()

if __name__ == "__main__":
    n = 8  # Change this to solve for different board sizes
    solutions = solve_n_queens(n)

    if solutions:
        print(f"Found {len(solutions)} solution(s) for {n}-Queens:\n")
        for solution in solutions:
            print_solution(solution)
    else:
        print(f"No solution found for {n}-Queens.")
