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
      