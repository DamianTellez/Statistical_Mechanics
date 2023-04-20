import math
import matplotlib.pyplot as plt

def count_microstates(N, n):
    """
    Counts the total number of microstates for a thermodynamics system with N Einstein's solids and n discrete energy levels.
    """
    return math.comb(N + n - 1, n) #combinatory, neglecting those repeated 

#SUBSYSTEM A
N_A = 3  # available spots in A

#SUBSYSTEM B
N_B = 3  # available spots in B

n = 6 # value of n_A + n_B (you can choose your target value for n)

total=0

# From here we'll show the most probable states.

#note that n_A and n_B are the discrete energy values located in A and B, respectively.

for n_A in range (n+1):
    for n_B in range (n+1-n_A): # because n_B has the remaining energy  
        if n_A + n_B == n: # this way we get into the causes of interess: the amount of energy is conserved and the value is n 
            num_microstates = count_microstates(N_A, n_A) * count_microstates(N_B, n_B)
            total += num_microstates # obtain the total of microstates
            print(f"The number of microstates for the system with {N_A + N_B} total available spots and ({n_A}+{n_B}) energy levels in A+B subsystem is {num_microstates}.")
            n_B+=1
        else: 
            continue
    n_A+=1
    
print(f"\nThen, the total number of possible microstates is {total}.")
