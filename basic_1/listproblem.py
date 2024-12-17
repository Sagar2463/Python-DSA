#Create a new list containing only the even numbers from numbers.
#Create a new list containing the squares of all the odd numbers.
#Replace every even number in the original list with the word "even".
numbers=[1,2,3,4,5,6,7,8,9,10]
#solution of 1
even=[]
for num in numbers:
    if num % 2 == 0:
      even.append(num)
print(even)
#solution of 2
odd=[]
for num in numbers:
   if num % 2 != 0:
      square=num**2
      odd.append(square)
print(odd)
#solution of 3
for i in range(len(numbers)):
   if numbers[i] % 2 == 0:
      numbers[i]="even"
print(numbers)

matrix = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]
#Print the matrix row by row.
#Print all the elements in the matrix one by one (using nested loops).
#Calculate the sum of each row and print it.
#solution 1
for row in matrix:
   print(row)
 
#solution of 2
for row in matrix:
   for num in row:
      print(num,end=" ")
   print()
#solution of 3
for row in matrix:
   print(sum(row))

#Problem: Given a 2D matrix, print the transpose of the matrix.
#The transpose of a matrix is obtained by swapping its rows and columns
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

#solution 
Tmatrix =[]
for col in range(len(matrix2[0])):
   trow=[]
   for row in range(len(matrix2)):
      trow.append(matrix1[row][col])
   Tmatrix.append(trow)

for row in Tmatrix:
   print(row)
# lets understand by third one
matrix3 = [
    [10, 20, 30],
    [40, 50, 60]
]
#solution 3
test=[]
for col in range(len(matrix3[0])):
   prow=[]
   for row in range(len(matrix3)):
      prow.append(matrix3[row][col])
   test.append(prow) 
      
   

   
    
     






      

    



