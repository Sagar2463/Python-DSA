#1.String Reversal:
#Write a function that takes a string and returns the string in reverse order. For example, if s = "hello", the function should return "olleh".

#2Palindrome Check:
#Write a function that checks whether a given string is a palindrome. A string is a palindrome if it reads the same forward and backward (ignoring spaces and punctuation). For example, "racecar" is a palindrome.

#3Count Vowels:
#Write a function that counts the number of vowels (a, e, i, o, u) in a given string. For example, if s = "hello world", the output should be 3 (e, o, o).

#4Character Frequency:
#Write a function that takes a string and returns a dictionary that contains the frequency of each character in the string. For example, for s = "hello", the output should be {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

#5String Compression:
#Write a function that compresses a string by converting repeated characters into a single character followed by its count. For example, for s = "aaabbbccc", the function should return "a3b3c3". If the compressed string is not shorter than the original, return the original string.

#solutions

#solution1
s = "sagar kumar"
def reverse(s):
 return s[::-1]
print(reverse(s))

#solution 2
r="racecar"
def pardom(s):
 p= s[::-1]
 if s == p :
  return True
 else:
  return False
print(pardom(r))

#solution 3
def common(s):
 count = 0
 for char in s:
  if char in 'aeiou':
   count += 1
 return count
print(common(s))

def common2(s):
 vowels=""
 count=0
 for i in range(len(s)):
  if s[i]== 'a' or s[i]== 'e' or s[i]== 'i' or s[i]== 'o' or s[i]== 'u':
   count += 1
   vowels+= s[i]
   vowels.split()
 return f"{count},({",".join(vowels)})"
print(common2(s))
#solution 4
def count_dict(s):
 dict={}
 for char in s:
  if char in dict:
   dict[char] += 1
  else:
   dict[char] = 1
 return dict
print(count_dict(s))
#solution 5



