def divided_differences(x, y):
    n = len(x)
    table = [[0] * n for _ in range(n)]

    # First column is y-values
    for i in range(n):
        table[i][0] = y[i]

    # Calculate divided differences
    for j in range(1, n):  # Column index
        for i in range(n - j):  # Row index
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

    return table

def print_divided_difference_table(table):
    """
    Prints the divided difference table in a readable format.

    Parameters:
    table : list of list of floats
        The divided difference table.
    """
    for row in table:
        print("\t".join(f"{value:.5f}" if value != 0 else "" for value in row))

# Example usage
x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]

div_diff_table = divided_differences(x_points, y_points)
print("Divided Difference Table:")
print_divided_difference_table(div_diff_table)
