#Initializing a funtion which will take in a list of our socks
#The return value for this function will be the total number of pairs
def matching_socks(socks):
    #Creating a dictionary object to help us calculate the frequency of each color.
    colorsPairs = {}
    
    #Looping through the list of socks
    #checking if the color exists in our dictionary
    #if it exists we increment the value by one
    #if it does not exist we initialize it and then set the value as one
    for sock in socks:
        if sock not in colorsPairs:
            colorsPairs[sock] = 1
        else:
            colorsPairs[sock] += 1
            
    #Initializing a variable to store the total number of pairs
    pairs = 0
    #Looping through the colors in the dictionary
    #While looping through the colors we check add to our 
    #total pair the number of pairs of that color
    #we get the number of pairs for the color by dividing
    #its value by 2
    for pair in colorsPairs:
        pairs += colorsPairs[pair] // 2
    
    return "The total number of pairs in this pile is " + str(pairs) + "."
    
#Initializing the first test which contains 30 elements and 10 pairs
sockspair1 = [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
#Printing the result of our function which is the number of matching socks.
print(matching_socks(sockspair1))

#Initializing the second test which contains 80 elements and 36 pairs
sockspair2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,50,51,52,53,54,55,56,57]
#Printing the result of our function which is the number of matching socks.
print(matching_socks(sockspair2))
