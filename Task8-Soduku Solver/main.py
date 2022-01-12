def solve(grid):
    '''
    Solves a Sudoku puzzle.

    Args:
        grid (list): A 9x9 Sudoku puzzle.

    Returns:
        list: A 9x9 Sudoku puzzle.
    '''
    return solve_recursive(grid, 0, 0)

def solve_recursive(grid, row, col):
    '''
    Solves a Sudoku puzzle recursively.

    Args:
        grid (list): A 9x9 Sudoku puzzle.
        row (int): The current row.
        col (int): The current column.

    Returns:
        list: A 9x9 Sudoku puzzle.
    '''
    if row == 9:
        return grid
    if col == 9:
        return solve_recursive(grid, row + 1, 0)
    if grid[row][col] != 0:
        return solve_recursive(grid, row, col + 1)
    for i in range(1, 10):
        if is_valid(grid, row, col, i):
            grid[row][col] = i
            if solve_recursive(grid, row, col + 1):
                return grid
    grid[row][col] = 0
    return None

def is_valid(grid, row, col, num):
    '''
    Checks if a number is valid for a Sudoku puzzle.

    Args:
        grid (list): A 9x9 Sudoku puzzle.
        row (int): The current row.
        col (int): The current column.
        num (int): The number to check.

    Returns:
        bool: True if the number is valid, False otherwise.
    '''
    return not (num in grid[row] or num in [grid[i][col] for i in range(9)] or num in [grid[i][j] for i in range(row // 3 * 3, row // 3 * 3 + 3) for j in range(col // 3 * 3, col // 3 * 3 + 3)] or num == 0)

if __name__ == "__main__":
    grid = list()
    for _ in range(9):
        grid.append([int(i) if i != '_' else 0 for i in input().split()])
    print("Solved Soduku:")
    print("\n".join([" ".join(map(str, row)) for row in solve(grid)]))
