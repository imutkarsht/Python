row1=['🏵️','🏵️','🏵️']
row2=['🏵️','🏵️','🏵️']
row3=['🏵️','🏵️','🏵️']

print(f"{row1}\n{row2}\n{row3}")
print("Enter the coordinate of row and column where you want to put red flower: ")
r=int(input("row= "))
c=int(input("column= "))
new_list=[row1,row2,row3]
new_list[r-1][c-1]='🌸'
print(f"{row1}\n{row2}\n{row3}")
