'''
File: Nacci.py
Purpose: Calculates Fibonacci numbers.
How to use: Enter the position of the Fibonacci number you want, e.g. "7" would return 13, the 7th Fibonacci number.
'''
import time #(c) Time package to do basic timing of the iterative and recursive method.

#(a) Recursive method for the Fibonacci sequence
def nacci_rec(n):
    if n == 0: #The number at index 0 is 0
        return 0
    
    elif n == 1: #The number at index 1 is 1
        return 1
    
    else: 
        return nacci_rec(n-1) + nacci_rec(n-2) # Return the sum of 2 previous Fibonacci numbers.

#(b) Iterative method for the Fibonacci sequence
def nacci_iter(n):
    Fibbo = [0, 1] #List with the first two Fibbonaci numbers
    
    for i in range(n-1):  #For n=2, i=[0], for n=3, i=[0,1], etc.
        Fibbo.append((Fibbo[i] + Fibbo[i + 1])) #Append all Fibonacci numbers
    
    return Fibbo[n] #Return the nth Fibonacci number

user = None #Set input to None on program startup.
while user != "exit": #Waits for program termination
    user = input("Please enter which Fibonacci number you'd like to get or exit: ").lower() #Decapitalizes all letters.
    user=user.replace(" ", "") #Removes all spaces user might have put after or before "exit" (or any other string, such as between a multi-digit number)
    
    if user == "exit": # Exits program
        pass #Could do break, but program satisfies condition to break while-loop on its own.
    
    else:
        try: #Error handling to see if input is valid
            n = int(user) #Tries to see if input is an integer
            
            if n<0:
                raise ValueError
                
            else:
                start = time.perf_counter() #(c) Performance counter, calculates processing time.
                print(f"Fibonacci number at index {n} is {nacci_rec(n)}, which took {time.perf_counter() - start:0.5f} seconds to calculate using recursion.") 
                #f-string which calls function and calculates recursive time.
                
                start = time.perf_counter() #same as before but for the iterative method
                print(f"Fibonacci number at index {n} is {nacci_iter(n)}, which took {time.perf_counter()-start:0.5f} seconds to calculate using iteration.")
            
        except ValueError:
            print("Input must be a non-negative integer, try again.")
