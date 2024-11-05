def F1(X):
    return ((0.8823 * 40 + 12 + 5) * X + 2000) * 12

def F2(X):
    return ((0.8823 * 40 + 12 + 6) * X + 2000) * 11

def F3(X):
    return ((0.8823 * 80 + 12 + 7) * X + 2500) * 10

def F4(X):
    return ((0.8823 * 80 + 12 + 8) * X + 2500) * 9

def F5(X):
    return ((0.8823 * 80 + 12 + 9) * X + 2500) * 8

def F6(X):
    return ((0.8823 * 80 + 12 + 10) * X + 2500) * 7

# Function to calculate and print results for all functions
def calculate_all_with_A(new_A):
    X = new_A
    results = [
        F1(X),
        F2(X),
        F3(X),
        F4(X),
        F5(X),
        F6(X)
    ]
    
    # Print all results
    for i, result in enumerate(results, start=1):
        print(f'\033[33mTotal cost for Type {i} = {result}\033[0m')
    
    # Find the minimum result
    min_cost = min(results)
    min_index = results.index(min_cost) + 1  # +1 to match the Type number
    
    print(f'\033[31mThe minimum total cost for Type {min_index} (300 capacity)= {min_cost}\033[0m')

# Example usage
A = 102.48813844421308  # Initial value of C
calculate_all_with_A(A)