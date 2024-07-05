def create_sparseMat(rows, cols):
    sparse_matrix = {'rows': rows, 'cols': cols}
    elements = int(input("Jumlah elemen: "))
    for i in range(elements):
        valid_input = False
        while not valid_input:
            row = int(input(f"Baris ke-? "))
            col = int(input(f"Kolom ke-? "))
            if 0 <= row < rows and 0 <= col < cols:
              valid_input = True
            else:
              print("Enter the right row and col !!")
        data = int(input(f"Data [{row},{col}] = "))
        sparse_matrix[(row, col)] = data
    return sparse_matrix

def display_sparseMat(sparse_matrix):
    rows = sparse_matrix['rows']
    cols = sparse_matrix['cols']
    for i in range(rows):
        for j in range(cols):
            if (i, j) in sparse_matrix:
                print(sparse_matrix[(i, j)], end="   ")
            else:
                print(0, end="   ")
        print()
    print()

def add_sparse(mat1, mat2):
    if mat1['rows'] != mat2['rows'] or mat1['cols'] != mat2['cols']:
        print("Error --- size of both matrix is not equal \nError Matrix")
        return None
    result = {'rows': mat1['rows'], 'cols': mat1['cols']}
    for key in mat1:
        if key != 'rows' and key != 'cols':
            result[key] = mat1[key]
    for key in mat2:
        if key != 'rows' and key != 'cols':
            if key in mat1:
                result[key] = mat1[key] + mat2[key]
            else:
                result[key] = mat2[key]
    return result

def mul_sparse(mat1, mat2):
    if mat1['cols'] != mat2['rows']:
        print(f"Error --- require {mat1['cols']} but found {mat2['rows']}\nError Matrix")
        return None
    result = {'rows': mat1['rows'], 'cols': mat2['cols']}
    for i in range(mat1['rows']):
        for j in range(mat2['cols']):
            total = 0
            for k in range(mat1['cols']):
              if (i, k) in mat1:
                mat1_value = mat1[(i, k)]
                if (k, j) in mat2:
                  mat2_value = mat2[(k, j)]
                  total += mat1_value * mat2_value
            if total != 0:
                result[(i, j)] = total
    return result




mat1=create_sparseMat(4,6)
print(mat1)
display_sparseMat(mat1)

mat2 = create_sparseMat(4,6)
print(mat2)
display_sparseMat(mat2)

mat3 = create_sparseMat(6,2)
print(mat3)
display_sparseMat(mat3)

display_sparseMat(mat1)
display_sparseMat(mat2)
hasil = add_sparse(mat1, mat2)
display_sparseMat(hasil)

display_sparseMat(mat1)
display_sparseMat(mat3)
hasil = add_sparse(mat1, mat3)
if hasil :
  display_sparseMat(hasil)

display_sparseMat(mat1)
display_sparseMat(mat3)
hasil = mul_sparse(mat1, mat3)
display_sparseMat(hasil)

display_sparseMat(mat1)
display_sparseMat(mat2)
hasil = mul_sparse(mat1, mat2)
if hasil :
  display_sparseMat(hasil)