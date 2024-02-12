from module5_mod import NumberCollection

def main():
    # Create an instance of NumberCollection
    number_collection = NumberCollection()

    # Input loop for a positive integer N
    while True:
        n = input("Please enter a positive integer: ")
        if NumberCollection.is_positive_integer(n):
            n = int(n)
            break
        else:
            print("Invalid input. Please enter a positive integer.")

    # Input loop for N numbers
    i = 0
    while i < n:
        y = input("Please enter a number: ")
        if number_collection.insert_data(y):
            i += 1
        else:
            print("Invalid input. Please enter a number.")

    # Input loop for the integer to search
    while True:
        x = input("Enter an integer: ")
        if NumberCollection.is_integer(x):
            break
        else:
            print("Invalid input. Please enter an integer.")

    # Search for the integer and print the result
    result = number_collection.search_data(x)
    if result == [-1]:
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    main()