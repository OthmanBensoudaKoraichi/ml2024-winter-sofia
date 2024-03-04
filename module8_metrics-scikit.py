"""
The program asks the user for input N (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X is treated as the ground truth (correct) class label and Y is treated as the predicted class. Both X and Y are either 0 or 1.

In the end, the program outputs: the Precision and Recall based on the inputs.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks).

"""


import numpy as np
from sklearn.metrics import precision_score, recall_score
from module4 import is_positive_integer


def main():
    # User inputs N (positive integer)
    while True:
        N = input("Please enter a positive integer: ")
        if is_positive_integer(N):
            N = int(N)
            break
        else:
            print("Invalid input. Please enter a positive integer.")

    # Initialize arrays to store x (ground truth) and y (predicted) values
    x = np.zeros(N, dtype=int)
    y = np.zeros(N, dtype=int)

    # Read (x, y) points
    for i in range(N):
        while True:
            try:
                x_input = input(f"Enter ground truth for point {i + 1}: ")
                x[i] = float(x_input)  # Attempt to convert input to float
                break  # Exit the loop if successful
            except ValueError:
                print("Invalid input. Please enter a real number.")

        while True:
            try:
                y_input = input(f"Enter predicted value for point {i + 1}: ")
                y[i] = float(y_input)
                break
            except ValueError:
                print("Invalid input. Please enter a real number.")

    # Calculate Precision and Recall
    precision = precision_score(x, y)
    recall = recall_score(x, y)

    # Output the results
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")


if __name__ == "__main__":
    main()
