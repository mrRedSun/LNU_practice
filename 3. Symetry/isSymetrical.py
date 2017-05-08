import itertools

def output_matrix(matrix):
	for row in matrix:
		for elem in row:
			print(elem, end = " ")
		else:
			print()

def input_matrix():
	matrix = []
	n = int(input("Введіть розмір матриці: "))
	for m in range(n):
		matrix.append([])

	for row in range(len(matrix)):
		for k in range(n):
			print("Елемент {0}-го рядку, {1}-го стовпчика".format(row + 1, k + 1), end = " ")
			matrix[row].append(int(input()))
	return matrix

def perevirka(matrix):
	for x in range(len(matrix)):
		for m in range(len(matrix)):
			if not(matrix[x][m] == matrix[m][x]):
				return False
	else:
		return True

mat = input_matrix()
print("Ваша матриця")
output_matrix(mat)

if perevirka(mat):
	print("Матриця симетрична відносно головної діагоналі")
else:
	permutations = list(itertools.permutations(mat))
	for mat in permutations:
		if perevirka(mat):
			print("Симетрії матриці відносно голоної діагоналі можна досягнути перестановкою рядків")
			break
	else:
		print("Симетрії матриці відносно голоної діагоналі не можна досягнути перестановкою рядків")

