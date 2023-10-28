def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                # Calculate the value based on the values from the previous row
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))

n = 5
pascal_triangle = generate_pascals_triangle(n)
print_pascals_triangle(pascal_triangle)
