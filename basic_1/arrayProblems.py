#Array Problems:

#1.Array Sum:
#Write a function that takes an array of numbers as input and returns the sum of all the elements in the array.

#2.Find Maximum and Minimum:
#Given an array of numbers, write a function that returns both the maximum and minimum values in the array.

#3.Reverse an Array:
#Write a function that takes an array and returns a new array that is the reverse of the original.

#4.Array Rotation:
#Write a function that rotates an array to the right by k positions. For example, if arr = [1, 2, 3, 4, 5] and k = 2, the rotated array should be [4, 5, 1, 2, 3].

#5.Check for Duplicate Elements:
#Write a function that checks whether an array contains duplicate elements. If it does, return True; otherwise, return False.

#solution-1
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
def array_sum(arr):
    return sum(arr)
#hard approch 
def array_sum1(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]# another way to right this is sum=sum+arr[i]
    return sum
    
a=array_sum(arr)
print(a)

#solution-2
def max_min(arr):
    return max(arr), min(arr)
print(max_min(arr))
#hard approch
def max_min1(arr):
    max_value = arr[0]
    min_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return max_value, min_value
print(max_min1(arr))

#solution-3
def reverse_arr(arr):
    new_arr=[]
    new_arr=arr[::-1]
    return new_arr
print(reverse_arr(arr))
#hard-approch
def reverse_arr1(arr):
    count= len(arr)-1
    new_arr=[]
    for i in range(len(arr)):
         new_arr.append(arr[count])
         count = count-1
    return new_arr      
print(reverse_arr1(arr))
#solution-4
def rotate(k,arr):#pasign 2 parameters 1 is the index from where u want the rotation in the array
    new_arr=arr[k:]+arr[:k]
    return new_arr
print(rotate(3,arr))
#hard approch
def rotate1(k,arr):
    new_arr=[]
    half_arr=arr[:k]
    second_half_arr=arr[k:]#not hard approch but just clear understanding
    new_arr=second_half_arr+half_arr
    return new_arr
print(rotate1(2,arr))
#solution-5
def check_duplicate(arr):
    tem_arr=arr
    for i in range(len(arr)):
        if tem_arr[i] in arr :
            return True
        
    return False
print(check_duplicate(arr))
#hard approch/ another approch
def check_duplicate1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

print(check_duplicate1(arr))




        




   