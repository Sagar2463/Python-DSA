# find the gcf(greated common factor)
def gcf(num1,num2):
    gcf1=1
    for i in range(1,min(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0 :
            gcf1=i
    return gcf1
        

print(gcf(12,8))
#square of number equal to length of input numbers
def size(num):
    for i in range(10**(num-1)):
        if num == len(str(i**2)):
            return i

print(size(6))

#find the longest repeated pattern

def strcount(input_str):
    max_pattern = ""
    length = len(input_str)

    # Loop through all possible starting positions
    for i in range(length):
        # Loop through all possible lengths of substrings
        for j in range(i + 2, length + 1):  # at least 2 characters long
            substring = input_str[i:j]
            # Check if this substring repeats
            if input_str.count(substring) > 1:
                # Check if it's the longest we've found
                if len(substring) > len(max_pattern):
                    max_pattern = substring

    if max_pattern:
        return "yes", max_pattern
    else:
        return "no", "null"

# Test the function with the provided example
print(strcount("aaccbbaabbccbbb"))  #bb Expected output should show the longest repeated pattern

#count the words in string 

def challange(word):
    fake=" "
    counting=word.count(fake)
    return counting+1
print(challange("hello world sagar"))
    
  
#factorial by recursion

def recursion_challange(num):
    if num == 1:
        return 1
    else:
        return num * recursion_challange(num-1)

print(recursion_challange(8))
