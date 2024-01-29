## Helper functions

# Function to check if input is an integer
def is_integer(X):
    try:
        int(X)
        return True
    except ValueError:
        return False

# Function to check if input is a float
def is_float(X):
    try:
        float(X)
        return True
    except ValueError:
        return False

# Function to check if input is a positive integer
def is_positive_integer(N):
    try:
        # First check if N can be converted to an integer
        if is_integer(N):
            # Then check if it's positive
            return int(N) > 0
        else:
            return False
    except ValueError:
        return False

## Program
# Loop to get a positive integer N
while True:
    N = input("Please enter a positive integer: ")
    if is_positive_integer(N):
        N = int(N)
        break
    else:
        print("Invalid input. Please enter a positive integer.")

numbers = []
i = 0
while i < N:
    Y = input("Please enter a number: ")
    # Check if Y is a number, either int or float
    if is_integer(Y):
        i += 1
        numbers.append(Y)
    elif is_float(Y):
        i += 1
        numbers.append(Y)
    else:
        print("Invalid input. Please enter a number.")

while True:
    X = input("Enter an integer : ")
    if is_integer(X):
        break
    else:
        print("Invalid input. Please enter an integer :")

# Here, I make sure that if X appears more than one time in the numbers list, I print all indices, not just the first one.
if X not in numbers:
    print(-1)
else:
    full_list = []
    for i in range(len(numbers)):
        if numbers[i] == X:
            full_list.append(i)
    print(full_list)




