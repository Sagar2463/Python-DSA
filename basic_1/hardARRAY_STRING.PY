 #1.Array to String Conversion:

#Write a function that takes an array of characters and converts it to a string. For example, if arr = ['H', 'e', 'l', 'l', 'o'], the function should return "Hello".
#2.Merge Two Arrays:

#Given two sorted arrays, write a function that merges them into a single sorted array. For example, for arr1 = [1, 3, 5] and arr2 = [2, 4, 6], the result should be [1, 2, 3, 4, 5, 6].

#3.Rotate String:
#Write a function that checks if one string is a rotation of another. For example, "abc" is a rotation of "cab", but not a rotation of "acb".
 

#SOLUTIONS

#solution1
name=["s","a","g","a","r"]
def array_to_string(arr):
    new=""
    for i in arr:
        new=new+i
    return new
print(array_to_string(name))
#solution2
arr1=[1,3,5]
arr2=[2,4,6]
def merge_array(arr1,arr2):
    return sorted(arr1+arr2)
print(merge_array(arr1,arr2))
#solution3
def is_rotation(s1,s2):
    if len(s1) != len(s2):
        return False
    return s1 in s2+s2
print(is_rotation("abc","cab"))

