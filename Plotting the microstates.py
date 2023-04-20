import math
import matplotlib.pyplot as plt

def count_microstates(N, n):
    return math.comb(N + n - 1, n) 

#SUBSYSTEM A
N_A = 3  # available spots in A

#SUBSYSTEM B
N_B = 3  # available spots in B

n = 6 # value of n_A + n_B (you can choose your target value for n)

total=[]

for n_A in range (n+1):
    for n_B in range (n+1 - n_A):
        
        if n_A + n_B == n:
            
            num_microstates = count_microstates(N_A, n_A) * count_microstates(N_B, n_B)
            
            total.append(num_microstates)
                      
        else: 
            continue
    
print(f"\nTotal possible microstates: {sum(total)}.")

print("\n\nThe chart below show the probability distribution of finding a certain configuration of energy for the given sub-system.")


def plot_microstate_distribution(total):

    # Plot the histogram
    plt.bar(range(len(total)),total )
    plt.xlabel("Energy levels in n_A.")
    plt.ylabel("Total possible microstates.")
    plt.title(f"Microstate probability distribution.")
    plt.show()

plot_microstate_distribution(total)
