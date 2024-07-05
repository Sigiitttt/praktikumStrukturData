def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        baris = []
        for j in range(cols):
            data = int(input(f"Data matriks [{i},{j}] : "))
            baris.append(data)
        matrix.append(baris)
    return matrix

def display_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end="    ")
        print()
    print()

def add_matrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
      print("Error --- size of both matrix is not equal \nError Matrix")
      return None
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

def mul_matrix(a, b):
    if len(a[0]) != len(b):
        print(f"Error --- require {len(a[0])} but found {len(b)}\nError Matrix")
        return None
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result

mat1 = create_matrix(2, 3)
print("\n")
display_matrix(mat1)

mat2 = create_matrix(2, 3)
print("\n")
display_matrix(mat2)

mat3 = create_matrix(3,2)
print("\n")
display_matrix(mat3)

display_matrix(mat1)
display_matrix(mat2)
hasil=add_matrix(mat1,mat2)
if hasil :
  display_matrix(hasil)

display_matrix(mat1)
display_matrix(mat3)
hasil = add_matrix(mat1,mat3)
if hasil :
  display_matrix(hasil)

display_matrix(mat1)
display_matrix(mat3)
hasil=mul_matrix(mat1,mat3)
display_matrix(hasil)

display_matrix(mat1)
display_matrix(mat2)
hasil= mul_matrix(mat1,mat2)
if hasil :
  display_matrix(hasil)