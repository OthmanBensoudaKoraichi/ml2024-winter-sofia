"""The program asks the user for input N (positive integer) and reads it.

Then the program asks the user for input k (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.

In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.

Additionally, if the program outputs Y, provide the coefficient of determination.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous task).

"""

### Libraries ### (I import some of the functions that I created in previous assignments)
import numpy as np
import module4
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score


### Helper functions ###

# Loop to get a positive integer
def enter_pos_integer(letter):
    while True:
        N = input(f"Please enter a positive integer {letter}: ")
        if module4.is_positive_integer(N):
            return int(N)
        else:
            print("Invalid input. Please enter a positive integer.")

# Function to read N (x, y) points
def enter_points(N):
    points = np.zeros((N, 2))  # Initialize an array to store the points
    for i in range(N):
        while True:
            x = input(f"Enter x value for point {i+1}: ")
            y = input(f"Enter y value for point {i+1}: ")
            if module4.is_real(x) and module4.is_real(y):
                points[i] = [float(x), float(y)]  # Assign the point to the array
                break
            else:
                print("Invalid input. Please enter real numbers for x and y.")
    return points

def enter_real_number(number):
    while True:
        value = input(number)
        if module4.is_real(value):
            return float(value)
        else:
            print("Invalid input. Please enter a real number.")


### Program ###
def main():
    # Loop to get a positive integer N
    N = enter_pos_integer("N")

    # Loop to get a positive integer k and ensure k <= N
    while True:
        k = enter_pos_integer("k")
        if k <= N:
            break
        else:
            print(f"Error: k should be less than or equal to the number of points (N={N}). Please enter a new k.")


    # Collecting N points
    points = enter_points(N)
    # Reshape for sklearn
    X = points[:, 0].reshape(-1, 1)
    y = points[:, 1]

    # Ask for input X to predict Y
    x_input = enter_real_number("Enter the value of X to predict Y: ")
    X_predict = np.array([[x_input]])

    # Perform k-NN Regression
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X, y)
    y_predict = knn.predict(X_predict)

    r2 = None  # Initialize r2 to None (or a suitable default value)

    # Only calculate R^2 if there are enough data points
    if len(y) > 1:
        y_pred_train = knn.predict(X)
        r2 = r2_score(y, y_pred_train)

    print(f"Predicted Y for input X={x_input}: {y_predict[0]}")

    # Conditionally print R^2 if it was calculated
    if r2 is not None:
        print(f"Coefficient of determination (R^2) based on the training data: {r2}")
    else:
        print("Not enough data to calculate R^2.")

    print(f"Predicted Y for input X={x_input}: {y_predict[0]}")
    print(f"Coefficient of determination (R^2) based on the training data: {r2}")


if __name__ == "__main__":
    print(main())
