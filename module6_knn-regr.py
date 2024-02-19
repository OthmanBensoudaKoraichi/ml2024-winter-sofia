"""The program asks the user for input N (positive integer) and reads it.

Then the program asks the user for input k (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one)
and reads all of them: first: x value, then: y value for every point one by one. X and Y are real numbers.

In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.

The basic functionality of data processing (data initialization, data insertion, data calculation) should be done using
Numpy library as much as possible (note: you can combine with OOP from the previous task)."""

### Libraries ### (I import some of the functions that I created in previous assignments)
import numpy as np
import module4

### Helper functions ###

# Loop to get a positive integer
def enter_pos_integer():
    while True:
        N = input("Please enter a positive integer: ")
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


# Distance metrics
def euclidean_distance(points, v):
    # Calculate the Euclidean distance based only on the x values
    distances = np.sqrt((points[:, 0] - v[0])**2)
    return distances

def manhattan_distance(points, v):
    # Calculate the Manhattan distance based only on the x values
    distances = np.abs(points[:, 0] - v[0])
    return distances


# k-NN Regression algorithm
def k_nn_regression(points, v, k, distance_metric="euclidean"):
    # Check if k is greater than the number of points
    if k > len(points):
        return "Error: k should be less than or equal to the number of points (N)."

    # Calculate distances between v and each point
    if distance_metric == "euclidean":
        distances = euclidean_distance(points, v)
    else:
        distances = manhattan_distance(points, v)

    # Sort distances and get indices of the k nearest neighbors
    k_nearest_indices = np.argsort(distances)[:k]

    # Calculate the average Y value of the k nearest neighbors
    avg_y = np.mean(points[k_nearest_indices, 1])

    return avg_y



### Program ###
def main():
    # Loop to get a positive integer N
    N = enter_pos_integer()

    # Loop to get a positive integer k
    k = enter_pos_integer()

    # Collecting N points
    points = enter_points(N)

    # Ask for input X
    x_input = float(input("Enter the value of X: "))

    # Perform k-NN Regression
    result = k_nn_regression(points, np.array([x_input, 0]), k, distance_metric = "euclidean")

    return result


if __name__ == "__main__":
    print(main())
