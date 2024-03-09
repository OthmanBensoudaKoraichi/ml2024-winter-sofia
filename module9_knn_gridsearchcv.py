"""
The program asks the user for input N (positive integer) and reads it.

Then the program asks the user to provide N (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.

This set of pairs constitutes the training set TrainS = {(x, y)_i}, i = 1..N.

Then the program asks the user for input M (positive integer) and reads it.

Then the program asks the user to provide M (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.

This set of pairs constitutes the test set TestS = {(x, y)_i}, i = 1..M.

In the end, the program outputs: the best k for the kNN Classification method and the corresponding test accuracy. kNN Classifier should be trained on pairs from TrainS, tested on x values from TestS and compared with y values from TestS.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks).

Note: you can try the following range of k: 1 <= k <= 10.

"""

from module4 import is_positive_integer
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def main():
    # Input and validation for the number of training data points
    while True:
        N = input("Please enter the number of training data points: ")
        if is_positive_integer(N):
            N = int(N)
            break
        else:
            print("Invalid input. Please enter a positive integer.")

    train_data = np.zeros((N, 2))
    for i in range(N):
        x_val = float(input(f"Enter x value for training point {i + 1}: "))
        y_val = int(input(f"Enter y class label for training point {i + 1}: "))
        train_data[i] = [x_val, y_val]

    X_train = train_data[:, 0].reshape(-1, 1)
    y_train = train_data[:, 1].astype(int)

    # Input and validation for the number of test data points
    while True:
        M = input("Please enter the number of test data points: ")
        if is_positive_integer(M):
            M = int(M)
            break
        else:
            print("Invalid input. Please enter a positive integer.")

    test_data = np.zeros((M, 2))
    for i in range(M):
        x_val = float(input(f"Enter x value for test point {i + 1}: "))
        y_val = int(input(f"Enter y class label for test point {i + 1}: "))
        test_data[i] = [x_val, y_val]

    X_test = test_data[:, 0].reshape(-1, 1)
    y_test = test_data[:, 1].astype(int)

    # Finding the best k
    best_k = 1
    best_accuracy = 0

    if len(X_train) > 1:
        # Split training data into training and validation sets (50/50 split)
        split_index = len(X_train) // 2
        X_train_part, X_val = X_train[:split_index], X_train[split_index:]
        y_train_part, y_val = y_train[:split_index], y_train[split_index:]

        # Iterate through k values to find the best k using the validation set
        # Taking the min of 10 and the length of train and val set, so that I don't get an error
        min_k = min(10,len(X_train_part),len(X_val))

        for k in range(1, min_k + 1):
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(X_train_part, y_train_part)
            y_pred_val = knn.predict(X_val)
            accuracy = accuracy_score(y_val, y_pred_val)
            print(f"Validation accuracy for k={k}: {accuracy}")
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_k = k
    else:
        # Proceed without a validation set if only one training point is available
        best_k = 1  # Default to 1 as there's no basis to choose otherwise

    # Train a new model with the best k on the entire original training set
    knn_best = KNeighborsClassifier(n_neighbors=best_k)
    knn_best.fit(X_train, y_train)
    y_pred_test = knn_best.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred_test)

    print(f"The best k is {best_k} with test accuracy of {test_accuracy}")


if __name__ == "__main__":
    main()
