# Add two 2D matrices together.

def add_two_matrices(matrix_1, matrix_2):

    # Condition to check if both matrices are valid for addition.
    if len(matrix_1) != len(matrix_2):
        return "Invalid Matrix. Addition can not be performmed."
    for index, element in enumerate(matrix_1):
        if len(element) != len(matrix_2[index]):
            return "Invalid Matrix. Addition can not be performmed."
        
    # When matrices are valid and ready to be added.
    final_matrix = []
    for i in range(len(matrix_1)):
        internal_list = []
        for j in range(len(matrix_1[i])):
            internal_list.append(matrix_1[i][j] + matrix_2[i][j])
        final_matrix.append(internal_list)

    return final_matrix

print(add_two_matrices([[2, 4], [6,1]], [[8,1], [6,6]]))