input_row = int(input("行数を入力してください:"))
input_column = int(input("列数を入力してください:"))

for i in range(1, input_row+1):
	for j in range(1, input_column+1):
		print(i * j, end=" ")
	print()

