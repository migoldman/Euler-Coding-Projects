def findPalindrome():
    #Set up variables
    topPalindrome = 0;
    lasti = 0;
    lastj = 0;
    endHuh = False;

    #Set up two for loops that each will decrease by 1
    for i in range (999, 99, -1):
        #We set j = i and not 999 because we will have already checked the max*max-1 in the previous iteration
        #eg: don't need to check 998*999 since we would have already checked 999*998 previously
        for j in range (i, 99, -1):
            #set the product equal to temp
            temp = i*j;
            #check to see if temp is a palindrome
            if palindromeHuh(temp):
                print("We found a palindrome: %s * %s = %s" % (i,j,temp));
                #If it is a palindrome, check if the previous i and previous j are higher than the current i and j
                #respectively
                if ((lasti > i) & (lastj > j)):
                    print("Last palindrome components (%s and %s) are larger than %s and %s respectively" % (lasti,lastj,i,j));
                    print("We will only find smaller palindromes than %s. Ending program." % topPalindrome);
                    #If it is, then all remaining palindrome products will be lower than the one we already found with
                    #the previous i and previous j. End the program.
                    endHuh = True;
                #Check to see if the new palindrome is higher than the previous palindrome
                if temp > topPalindrome:
                    #If so, set variables to new i, j, and new highest palindrome
                    lasti = i;
                    lastj = j;
                    topPalindrome = temp;
                    print("New highest palindrome number: %s" % temp)
                    #This is the top palindrome for this i, so we should break and start the next loop
                    break
            #Check if we should end the program
            if endHuh:
                break
        if endHuh:
            break
    #return top product
    print("");
    return topPalindrome;

#Palindrom helper
def palindromeHuh(num):
    #turn the number into a string, then compare it to its reverse
    return str(num) == str(num)[::-1]

#call and print function
print("Largest palindrome: %s" % findPalindrome());