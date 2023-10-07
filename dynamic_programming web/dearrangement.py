import math

def factorial(n):
    k = 1
    for i in range(n, 0, -1):
        k *= i
    return k


def dearrangement(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid input. Please enter a non-negative integer."
    W = [0] * (n + 1)
    for i in range (0,n+1):
        if i == 0:
            W[0] = 1
            continue
        if i == 1:
            W[1] = 0    
            continue
        k = 0
        for j in range(i):
            k += math.comb(i, j) * W[j]
        W[i] = factorial(i) - k   
    return W[n]
    

def main():
    user_input = input("Enter something: ")

    try:
        user_integer = int(user_input)
        print("You entered:", user_integer)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    print(dearrangement(user_input))
    
if __name__ == '__main__':
    main()      