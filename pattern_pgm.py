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

for row in range(5):
	for col in range(7):
		if row==0 or col==6 or col==0 or row==4: 
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
print("___________________________")

for row in range(4):
	for col in range(4):
		if row==0 or col==0 or col==3 or row==3:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("_______________________________")


for row in range(5):
	for col in range(5):
		if row==0 or col==0 or row==4 or col==4 or row==col or row+col==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")

	print()

print("______________________________")
for row in range(5):
	for col in range(9):
		if row==4 or col+row==4 or col-row==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("__________________________________")

for row in range(7):
	for col in range(7):
		if row+col==3 or col-row==3 or row-col==3 or row+col==9:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	
	print()

print("____________________________________")

for row in range(13):
	for col in range(11):
		if row==5 or row==12 or col+row==5 or col-row==5  or row>=5 and col==0 or row>=5 and col==10 or row>=8 and col==2 or row>=8 and col==5 or col>=2 and col<=5 and row==8:
 			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("_____________________________")

for row in range(9):
	for col in range(9):
		print("*",end=" ")
	print()

print("______________________________________")

for row in range(8):
	for col in range(15):
		if row+col==7 or col-row==7 or col>=3 and col<=11 and row==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("_________________________________________")

for row in range(7):
	for col in range(5):
		if col==0 or col>=0 and col<=3 and row==0 or row>=1 and row<=2 and col==4 or col>=0 and col<=3 and row==3 or row>=4 and row<=5 and col==4 or col>=0 and col<=3 and row==6:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("____________________________")

for row in range(7):
	for col in range(5):
		if col>=2 and col<=4 and row==0 or col==1 and row==1 or row>=2 and row<=4 and col==0 or col>=2 and col<=4 and row==6 or row==5 and col==1:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("______________________________")

for row in range(8):
	for col in range(7):
		if col==0 or col>=1 and col<=4 and row==0 or col>=1 and col<=4 and row==7 or row==1 and col==5 or row==6 and col==5 or row>=2 and row<=5 and col==6 :
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()
print("__________________________________")

for row in range(7):
	for col in range(5):
		if col==0 or row==0 or row==3 or row==6:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("_________________________________________")

for row in range(7):
	for col in range(6):
		if col>=1 and col<=3 and row==0 or  col>=1 and col<=3 and row==4 or row>=1 and row<=3 and col==0 or col>=2 and col<=5 and row==2 or row>=3 and row<=6 and col==5 :
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("___________________________________")

for row in range(7):
	for col in range(4):
		if col==0 or col==3 or row==3 :
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("______________________________")

for row in range(6):
	for col in range(5):
		if col==0 or row==0 or row==3:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("______________________")


for row in range(7):
	for col in range(6):
		if col>=1 and col<=3 and row==0 or  col>=1 and col<=3 and row==4 or row>=1 and row<=3 and col==0 or col>=2 and col<=5 and row==2 or row>=3 and row<=6 and col==5 :
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("_____________________________")

           
for row in range(7):
	for col in range(4):
		if col==0 or col==3 or row==3 :
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("__________________________")

for row in range(7):
	for col in range(5):
		if col==2 or row==0 or row==6:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("__________________________")

for row in range(7):
	for col in range(5):
		if col==2 or row==0 or row>=5 and row<=6 and col==0 or row==6 and col==1:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("__________________________")

for row in range(7):
	for col in range(5):
		if col==0 or col+row==3 or row-col==3:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("__________________________")

for row in range(7):
	for col in range(5):
		if col==0 or row==6:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("__________________________")

for row in range(6):
	for col in range(5):
		if col==0 or col==4 or  col==1 and row==1 or row==2 and col==2 or col>=3 and col<=3 and row==1:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("__________________________")

for row in range(7):
	for col in range(7):
		if col==0 or col==6 or col-row==0:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("______________________________")

for row in range(6):
	for col in range(6):
		if col>=1 and col<=4 and row==0 or col>=1 and col<=4 and row==5 or row>=1 and row<=4 and col==0 or row>=1 and row<=4 and col==5:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("_______________________________")

for row in range(8):
	for col in range(5):
		if col==0 or col>=0 and col<=3 and row==0 or col>=0 and col<=3 and row==3 or row>=1 and row<=2 and col==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("______________________________")

for row in range(7):
	for col in range(7):
		if col>=1 and col<=4 and row==0 or col>=1 and col<=4 and row==5 or row>=1 and row<=4 and col==0 or row>=1 and row<=4 and col==5 or row==6 and col==6 or  row==5 and col==5 or  row==4 and col==4 or row==3 and col==3:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("___________________________________")

for row in range(8):
	for col in range(5):
		if col==0 or col>=0 and col<=3 and row==0 or col>=0 and col<=3 and row==3 or row>=1 and row<=2 and col==4 or row-col==3:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("_____________________________________")

for row in range(9):
	for col in range(5):
		if col>=1 and col<=4 and row==0 or col>=1 and col<=3 and row==4 or col>=0 and col<=3 and row==8 or row>=1 and row<=3 and col==0 or  row>=5 and row<=7 and col==4 :
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("_________________________________________")
 
for row in range(5):
	for col in range(7):
		if col==3 or row==0:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("_________________________________________")
 
for row in range(6):
	for col in range(5):
		if row>=0 and row<=4 and col==0 or row>=0 and row<=4 and col==4 or col>=1 and col<=3 and row==5:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("___________________________")

for row in range(4):
	for col in range(7):
		if col-row==0 or col+row==6:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("____________________")

for row in range(6):
	for col in range(5):
		if col==0 or col==4 or col==1 and row==4 or col==2 and row==3 or col==3 and row==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("____________________________________")

for row in range(5):
	for col in range(5):
		if col+row==4 or col-row==0:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("____________________________________")

for row in range(5):
	for col in range(5):
		if col+row==4 or col==0 and row==0 or col==1 and row==1:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("____________________________________")

for row in range(5):
	for col in range(5):
		if row==0 or row==4 or row+col==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("________________________________")

for row in range(9):
	for col in range(15):
		if col==0 or col>=0 and col<=4 and row==0 or col>=0 and col<=4 and row==4 or col>=0 and col<=4 and row==8 or row>=1 and row<=3 and col==5 or row>=5 and row<=7 and col==5 or row==3 and  col==6 or  row==4 and  col==7 or row==5 and  col==8 or row==6 and  col==9 or row==7 and  col==10 or row==6 and  col==11 or row==5 and  col==12 or row==4 and col==13 or row==3 and col==14 :
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print() 




