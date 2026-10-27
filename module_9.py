"""Module 9 zyLab starter: determinants and triangle geometry."""


def validate_square_matrix(matrix):
    if not isinstance(matrix, list) or not matrix:
        raise ValueError("matrix must be a nonempty list of rows")
    size = len(matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) != size:
            raise ValueError("matrix must be square")
        for value in row:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError("matrix entries must be real numbers")
    return size


def det2(matrix):
    """Return the determinant of a 2-by-2 matrix."""
    if validate_square_matrix(matrix) != 2:
        raise ValueError("det2 requires a 2-by-2 matrix")
    return float(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])


def minor_matrix(matrix, row, col):
    """Delete one row and one column without changing the input."""
    size = validate_square_matrix(matrix)
    valid_indices = (isinstance(row, int) and not isinstance(row, bool)
                     and isinstance(col, int) and not isinstance(col, bool)
                     and 0 <= row < size and 0 <= col < size)
    if size < 2 or not valid_indices:
        raise ValueError("minor requires valid indices in a matrix of size at least 2")
    return [[matrix[r][c] for c in range(size) if c != col]
            for r in range(size) if r != row]


def det3(matrix):
    """Return a 3-by-3 determinant by first-row cofactor expansion."""
    if validate_square_matrix(matrix) != 3:
        raise ValueError("det3 requires a 3-by-3 matrix")
    total = 0.0
    for col in range(3):
        if col % 2 == 0:
            sign = 1
        else:
            sign = -1
        smaller = minor_matrix(matrix, 0, col)
        total += sign * matrix[0][col] * det2(smaller)
    return total


def determinant_cofactor(matrix):
    """Return a determinant using expansion along the first row."""
    size = validate_square_matrix(matrix)
    if size == 1:
        return float(matrix[0][0])
    if size == 2:
        return det2(matrix)
    if size == 3:
        return det3(matrix)
    total = 0.0
    for col in range(size):
        if col % 2 == 0:
            sign = 1
        else:
            sign = -1
        smaller = minor_matrix(matrix, 0, col)
        total += sign * matrix[0][col] * determinant_cofactor(smaller)
    return total


def is_invertible(matrix, tolerance=1e-10):
    """Use the determinant criterion for a square matrix."""
    if (isinstance(tolerance, bool)
            or not isinstance(tolerance, (int, float)) or tolerance < 0):
        raise ValueError("tolerance must be nonnegative")
    return determinant_cofactor(matrix) != 0



def triangle_report(points, tolerance=1e-10):
    """Return area, orientation, and collinearity for three planar points."""
    if (isinstance(tolerance, bool)
            or not isinstance(tolerance, (int, float)) or tolerance < 0):
        raise ValueError("tolerance must be nonnegative")
    if not isinstance(points, list) or len(points) != 3:
        raise ValueError("exactly three points are required")
    for point in points:
        if not isinstance(point, list) or len(point) != 2:
            raise ValueError("each point must have two coordinates")
        for value in point:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError("coordinates must be real numbers")
    matrix = [[point[0], point[1], 1] for point in points]
    # Level 3: Use the determinant of matrix as signed double area.
    signed_double_area = determinant_cofactor(matrix)
    absval = abs(signed_double_area)
    area = absval / 2
    if absval <= tolerance:
        orientation = "collinear"
    elif signed_double_area > 0:
        orientation = "counterclockwise"
    else:
        orientation = "clockwise"
    
    return {"area": abs(signed_double_area) / 2.0,
            "orientation": orientation,
            "collinear": orientation == "collinear"}


def main():
    matrix = [[2, 1, 0], [0, 3, 1], [1, 0, 2]]
    print("Level 1 determinant:", det3(matrix))
    larger = [[1, 2, 0, 0], [0, 2, 1, 0],
              [3, 0, 1, 1], [0, 0, 0, 2]]
    print("Level 2 determinant:", determinant_cofactor(larger))
    print("Level 2 invertible:", is_invertible(matrix))
    print("Level 3:", triangle_report([[1, 1], [4, 1], [2, 3]]))


if __name__ == "__main__":
    main()
