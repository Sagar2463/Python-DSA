#program to check odd and even numbers 
x=23
if x%2==0:
    print ("number is even ")
else:
    print("number is odd")  #output: number is odd

#program that print table
for i in range(1,11):
   for j in range (1,11):
      print(i,"*",j,"=",i*j)
#program to cal culate sum of list 
A=[10,20,30,40,50]
print(sum(A))
print(len(A))
b=[1,2,3]
b.append(4)
b.insert(0,0)
b.remove(2)
print(b)