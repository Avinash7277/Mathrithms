# Psudo code 
# List of integers
#  take a variable to check the length of array
# create a new  blank list to hold the sorted value
#intilaize i= 0 for index
# use a while loop to check the ever integers in the list
#using min we would retreive the minimum value from the list (a)
#You store this  suceeding minimum number in your new list (new_a) 
# Now you have to delete that minimum number from the list a
# Take i += 1 This starts the whole process again.
# then print the new list


# code in Python

array     = [83,1,45,95,45,52,11,47,0,45,67,82]
kk    = len(a)
new_a = []
i     = 0

while i < kk:
    xx = min(array)      
    new_a.append(xx) 
    array.remove(xx)     
    i += 1          
print(new_a)
