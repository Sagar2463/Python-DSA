a=[1,2,3,4,5,6]
print(a[::2])
print(a[1::2])
print(a[-2::-2])
c=[1,2,3,4,5,6,7,8,9,10]
#print the list in reverse slicing 
print(c[::-1])
#print every second element starting form index 1

print(c[1::2])
#print every third element in reverse element
print(c[::-3])
D=[10,20,30,40,50,60,70,80]
#remove the first 2 elements 
#print(D.remove(10),D.remove(20),D)
#in this approch i am removing but its delting and i think u have some better idead 
#print(D[2:])#this is just printing by not including first 2
# add 90 and 100 in the list
#D.append(90)
#D.append(100)
#print the list in reverse 
#print(D[::-1])
#correct or good version 
D = [10, 20, 30, 40, 50, 60, 70, 80]

# Remove the first 2 elements in place
del D[:2]
print("After removing first 2 elements:", D)

# Add 90 and 100 to the list
D.extend([90, 100])
print("After adding 90 and 100:", D)

# Reverse the list in place
D.reverse()
print("Reversed list:", D)
