print("\n_________________________________________SHAPES_________________________________________________________\n")

print("\n______1.Square_____\n")

for row in range(4):
	for coloumns in range(4):
		print("*",end=" ")
	print()

print("\n______2.Rectangle______\n ")

for row in range(6):
	for coloumns in range(8):
		print("*",end=" ")
	print()

print("\n________3.Right angle traingle_______\n")

for row in range(5):
	for coloumns in range(row+1):
		print("*",end=" ")
	print()

print("\n________4.Left angle traingle________\n")

for row in range(1,5):
	print(" "*(5-row),"*" * row)

print("\n_______5.Empty rectangle_________\n ")

for row in range(5):
	for col in range(7):
		if row==0 or col==6 or col==0 or row==4: 
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n_____6.Empty square________\n")

for row in range(4):
	for col in range(4):
		if row==0 or col==0 or col==3 or row==3:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n______7.Square inside daignol_________\n")

for row in range(5):
	for col in range(5):
		if row==0 or col==0 or row==4 or col==4 or row==col or row+col==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n_______8.Traingle_________\n")

for row in range(5):
	for col in range(9):
		if row==4 or col+row==4 or col-row==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n________9.Rhombus______\n")

for row in range(7):
	for col in range(7):
		if row+col==3 or col-row==3 or row-col==3 or row+col==9:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	
	print()

print("\n______10.House______\n")

for row in range(13):
	for col in range(11):
		if row==5 or row==12 or col+row==5 or col-row==5  or row>=5 and col==0 or row>=5 and col==10 or row>=8 and col==2 or row>=8 and col==5 or col>=2 and col<=5 and row==8:
 			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n_________11.Square_______\n")

for row in range(9):
	for col in range(9):
		print("*",end=" ")
	print()


print("\n_________________________________________ALPHABETS________________________________________________\n")

print("\n___________1.A__________\n")

for row in range(8):
	for col in range(15):
		if row+col==7 or col-row==7 or col>=3 and col<=11 and row==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n___________2.B____________\n")

for row in range(7):
	for col in range(5):
		if col==0 or col>=0 and col<=3 and row==0 or row>=1 and row<=2 and col==4 or col>=0 and col<=3 and row==3 or row>=4 and row<=5 and col==4 or col>=0 and col<=3 and row==6:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n_____________3.C__________\n")

for row in range(7):
	for col in range(5):
		if col>=2 and col<=4 and row==0 or col==1 and row==1 or row>=2 and row<=4 and col==0 or col>=2 and col<=4 and row==6 or row==5 and col==1:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n_________4.D____________\n ")

for row in range(8):
	for col in range(7):
		if col==0 or col>=1 and col<=4 and row==0 or col>=1 and col<=4 and row==7 or row==1 and col==5 or row==6 and col==5 or row>=2 and row<=5 and col==6 :
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()
print("\n________5.E__________\n")

for row in range(7):
	for col in range(5):
		if col==0 or row==0 or row==3 or row==6:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n________6.F______________\n")
for row in range(6):
	for col in range(5):
		if col==0 or row==0 or row==3:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()


print("\n_________7.G__________\n")
for row in range(7):
	for col in range(6):
		if col>=1 and col<=3 and row==0 or  col>=1 and col<=3 and row==4 or row>=1 and row<=3 and col==0 or col>=2 and col<=5 and row==2 or row>=3 and row<=6 and col==5 :
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n_________8.H___________\n")
for row in range(7):
	for col in range(4):
		if col==0 or col==3 or row==3 :
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()


print("\n_________9.I__________\n")

for row in range(7):
	for col in range(5):
		if col==2 or row==0 or row==6:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n________10.J___________\n")

for row in range(7):
	for col in range(5):
		if col==2 or row==0 or row>=5 and row<=6 and col==0 or row==6 and col==1:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n_________11.K___________\n")

for row in range(7):
	for col in range(5):
		if col==0 or col+row==3 or row-col==3:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n_________12.L__________\n")

for row in range(7):
	for col in range(5):
		if col==0 or row==6:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n___________13.M__________\n")

for row in range(6):
	for col in range(5):
		if col==0 or col==4 or  col==1 and row==1 or row==2 and col==2 or col>=3 and col<=3 and row==1:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n___________14.N____________\n")

for row in range(7):
	for col in range(7):
		if col==0 or col==6 or col-row==0:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n__________15.O____________\n")

for row in range(6):
	for col in range(6):
		if col>=1 and col<=4 and row==0 or col>=1 and col<=4 and row==5 or row>=1 and row<=4 and col==0 or row>=1 and row<=4 and col==5:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n__________16.P_________\n")

for row in range(8):
	for col in range(5):
		if col==0 or col>=0 and col<=3 and row==0 or col>=0 and col<=3 and row==3 or row>=1 and row<=2 and col==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n____________17.Q__________\n")

for row in range(7):
	for col in range(7):
		if col>=1 and col<=4 and row==0 or col>=1 and col<=4 and row==5 or row>=1 and row<=4 and col==0 or row>=1 and row<=4 and col==5 or row==6 and col==6 or  row==5 and col==5 or  row==4 and col==4 or row==3 and col==3:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n_____________18.R_______________\n")

for row in range(8):
	for col in range(5):
		if col==0 or col>=0 and col<=3 and row==0 or col>=0 and col<=3 and row==3 or row>=1 and row<=2 and col==4 or row-col==3:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n____________19.S________________\n")

for row in range(9):
	for col in range(5):
		if col>=1 and col<=4 and row==0 or col>=1 and col<=3 and row==4 or col>=0 and col<=3 and row==8 or row>=1 and row<=3 and col==0 or  row>=5 and row<=7 and col==4 :
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n__________20.T______________\n")
 
for row in range(5):
	for col in range(7):
		if col==3 or row==0:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n___________21.U_________________\n")
 
for row in range(6):
	for col in range(5):
		if row>=0 and row<=4 and col==0 or row>=0 and row<=4 and col==4 or col>=1 and col<=3 and row==5:
			print("*",end=" ")
		else:
			print(" ",end=" ")	
	print()

print("\n_____________22.V______________\n")

for row in range(4):
	for col in range(7):
		if col-row==0 or col+row==6:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n_________23.W___________\n")

for row in range(6):
	for col in range(5):
		if col==0 or col==4 or col==1 and row==4 or col==2 and row==3 or col==3 and row==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n___________24.X______________\n")

for row in range(5):
	for col in range(5):
		if col+row==4 or col-row==0:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n__________25.Y______________\n")

for row in range(5):
	for col in range(5):
		if col+row==4 or col==0 and row==0 or col==1 and row==1:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n____________26.Z_____________\n")

for row in range(5):
	for col in range(5):
		if row==0 or row==4 or row+col==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

print("\n_______________27.BV_________________\n")

for row in range(9):
	for col in range(15):
		if col==0 or col>=0 and col<=4 and row==0 or col>=0 and col<=4 and row==4 or col>=0 and col<=4 and row==8 or row>=1 and row<=3 and col==5 or row>=5 and row<=7 and col==5 or row==3 and  col==6 or  row==4 and  col==7 or row==5 and  col==8 or row==6 and  col==9 or row==7 and  col==10 or row==6 and  col==11 or row==5 and  col==12 or row==4 and col==13 or row==3 and col==14 :
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print() 




