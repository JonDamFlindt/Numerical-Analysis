'''
File: Babylon.py
Purpose: Calculates square roots using the Babylonian square root.
How to use: Enter the square and the starting guess separated by a comma, e.g. "82,5" would guess that 5 is the square root of 82 (or that 82 is the square of 5).
Note that this program is designed to run in the terminal/command prompt.
'''

class ComplexError(Exception): #Custom error for a<0.
    pass

class LoopError(Exception): #Custom error for infinite loops.
    pass

def babylon_sqrt(a, x, n=0, max_n=1000): #Recursive method for the Babylonian square root.
    fx = 0.5*(a/x + x)
    
    if abs(fx-x) < 1.0e-10: # Criteria for stopping the recursive loop.
        if fx.is_integer(): # Checks if the float is an integer
            return int(fx), n # If it is, return in integer form
        return fx, n # Otherwise return in float form
    
    if n < max_n:
        n+=1 #Criteria not met correct, increase counter.
        return babylon_sqrt(a, fx, n) #Iterate
    else:
        raise LoopError

while True: #Program keeps running until terminated by user.
    user = input("Please enter a number and your guess for its root, respectively, seperated by a comma. To exit, hit CTRL+C: ")

    try: #Error handling
        a, x = user.replace(" ", "").split(",") #Remove spaces and split at the comma
        
        if float(a) < 0: #Only roots for reals can be found.
            raise ComplexError
            
        else:
            sqrt, i = babylon_sqrt(float(a),float(x)) # Call the function
            print(f"The square root of {a} is {sqrt}, which took {i} iterations with the starting guess {x}.")
            
    except ValueError: #Error raised when comma is missing or text/one number is given.
        print("Two numbers not given, try again.")

    except ComplexError:
        print("This program cannot calculate complex roots. If you have another number you want the square root of, try again.")
    
    except LoopError:
        print("The program could not find a good approximation of the root after 1000 iterations.")
