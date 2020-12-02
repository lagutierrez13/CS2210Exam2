def minFallingPathSum(A):
    optimal = [ [None] * len(A) for x in range(0, len(A)) ]
    
    best_paths = [ A[0][row] + helper(A, optimal, 1, row) for row in range(0, len(A))]

    return min(best_paths);

def helper(A, optimal, col, row):
    if col == len(A):
        return 0;
    
    if optimal[row][col] is None:
        first_row = max(0, row - 1)
        last_row = min(len(A) - 1, row + 1)

        best_paths = [A[col][row] + helper(A, optimal, col + 1, row) for row in range(first_row, last_row + 1)]

        optimal[col][row] =  min(best_paths)

    return min(best_paths)
