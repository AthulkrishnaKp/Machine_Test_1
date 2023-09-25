

first_multiple_input = input("Enter number of row's and column's : ").rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
lst=[]
matrix = []
for i in range(n):
    matrix_item = input("Enter words in matrix : ")
    x=list(matrix_item)
    matrix.append(x)

transpose = [list(row) for row in zip(*matrix)]
newmatrix=[row for row in transpose ]
lst=[]
lst1=[]
for i in range(len(newmatrix)):
    for j in range(7):
        print([newmatrix[i][j],''][newmatrix[i][j] in ['!','@','#','$','%','&',' ']],end='')
        while newmatrix[i][j] in ['!','@','#','$','%','&']:
            print(['',newmatrix[i][j]][newmatrix[i][j] in lst],end='')
            lst.append(newmatrix[i][j])
            break
        while newmatrix[i][j]==' ':
            print(['',' '][newmatrix[i][j+1]==' '],end='')
            break
        while newmatrix[i][j] in ['!','@','#','$','%','&',' ']:
            lst1.append(' ')
            print(['',' '][len(lst1)%2==0],end='')
            break


