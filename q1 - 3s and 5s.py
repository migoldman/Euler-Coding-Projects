#Declare a new int list
sumlist = [0];

#We want the multiples of 3 to 999
for i in range(1,334):
    #Add the product to the sumlist
    sumlist.append(i*3);

#We want the multiples of 5 to 995
for j in range(1,200):
    #Store the value and check to see if we already have it in the list
    temp = 5*j;
    #If the sum is divisible by 3, then it has been counted and do nothing
    if temp%3 != 0:
        #If it isn't, add it to the list
        sumlist.append(temp);

#Print the sum of the list
print(sum(sumlist));