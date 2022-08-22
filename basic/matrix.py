matrix = []

ROW = int(input("Emter the hoe much row u want"))
COLUMNS = int(input("Emter the hoe much row u want"))

for i in range(ROW):
    a = []
    for j in range(COLUMNS):
        a.append(int(input()))
    matrix.append(a)

for i in range(ROW):
    for j in range(COLUMNS):
        print(matrix[i][j], end=" ")
    print()



