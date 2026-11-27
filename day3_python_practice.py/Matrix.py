# Matrix Traversal
def display_matrix(matrix):

    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


# Matrix Transpose
def transpose_matrix(matrix):
 

    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for i in range(cols):

        new_row = []

        for j in range(rows):
            new_row.append(matrix[j][i])

        transpose.append(new_row)

    return transpose



# Example Matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
display_matrix(matrix)

print("\nTranspose Matrix:")
display_matrix(transpose_matrix(matrix))