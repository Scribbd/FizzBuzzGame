""" The for loop is possible on one line as the instruction that is being looped is just one line
    This also is for any other for/while/if kind of statement. So if(something == otherthing): print("Print they are the same!")
 And now for what the stuff after 'in' does in order of execution  
                      \/input waits for an input from. You can use as a string to prompt something
                  \/casts the input to an Integer. Or at least tries to. If you input anything else than a number, it will throw an error and stop the execution
         \/Will create a list from 1 to the given input
 This results in with input 13
  for i in [1,2,3,4,5,6,7,8,9,10,11,12]: """
for i in range(1, int(input("How high should I go?\n"))):
    """This uses a python feature which allows for multiplication of strings
         For example: "one of us. "*3 will result in the string "one of us. one of us. one of us. "
         Or the following: "10"*5 results in "1010101010"
         But the following is also true: "A very long string."*0 results in "". An empty string.
     The next python feature (and of many other languages) is the casting of a boolean to an integer.
         True casts to 1
         False casts to 0
     In reverse this is also true but!!
         0 results in False
         Any other number that is NOT 0 will cast to True
     So the following is happening with something like "Fizz"*(not i%3) is the following in order of execution
        #            \/i%3 will calculate what remains of i when divided by 3. Look up "modulus" for more info. 
        #                   The important thing is when there is no remain so the answer is 0 (False)
        #         \/not will take result of i%3 and negate it. It will make anything that isn't 0 Not True (False) and anything else Not False (True)
        #                   So if there is nothing remaining its result is TRUE, anything else will be FALSE
        #     \/The multiplication of strings happens like described above. When the line above is True "Fizz" will be printed, else it will result in nothing. """
    #print("Fizz"*(not i%3) + "Gozz"*(not i%4) + "Buzz"*(not i%5) + str(i)*bool(i%3 and i%4 and i%5))
    """And now for the stuff at the end                                      /\This is the same as above takes the modulus of all things
        #                                                                 /\This is needed to force a TRUE or FALSE. As the 'and's dont force that. 
        #                                                                       This is needed to prevent that the number is repeated. It could result in "8686"
        #                                                          /\This is to make the number a string for string multiplication or else it could print 0 instead of a fuzz or buzz"""
    
    #The above print statement in a more readable format as it will do the same.
    output = ""
    if i%3 == 0:
        output += "Fizz"
    if i%4 == 0:
        output += "Gozz"
    if i%5 == 0:
        output += "Buzz"
    if not(i%3 == 0 or i%4 == 0 or i%5 == 0):
        output += str(i)
    print(output)