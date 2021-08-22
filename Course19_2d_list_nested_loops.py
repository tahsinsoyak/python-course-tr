#liste içinde liste yapmak
number_grid =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

#1. sayı satır 2. sayı sütun
print(number_grid[0][2])
print("----------")

#iç içe for kullanarak yazdıralım

for row in number_grid:
    #print(row) bu şekilde direk listemizi yazdırırdık
    for col in row: #her satırdaki sutun için
        print(col)