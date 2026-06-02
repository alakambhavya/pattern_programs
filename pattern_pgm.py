for row in range(4):
	for coloumns in range(4):
		print("*",end=" ")
	print()

print("_________________________")

for row in range(6):
	for coloumns in range(8):
		print("*",end=" ")
	print()

print("________________________")

for row in range(5):
	for coloumns in range(row+1):
		print("*",end=" ")
	print()

print("__________________________")


for row in range(1,5):
	print(" "*(5-row),"*" * row)

print("_________________________")

