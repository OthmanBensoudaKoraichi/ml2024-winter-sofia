
class NumberCollection:
    def __init__(self):
        # Initialize an empty list to store numbers
        self.numbers = []

    @staticmethod
    def is_integer(x):
        """Check if the input x can be converted to an integer."""
        try:
            int(x)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_float(x):
        """Check if the input x can be converted to a float."""
        try:
            float(x)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_positive_integer(n):
        """Check if the input n is a positive integer."""
        return NumberCollection.is_integer(n) and int(n) > 0

    def insert_data(self, y):
        """Insert data into the collection if it is an integer or a float."""
        if NumberCollection.is_integer(y) or NumberCollection.is_float(y):
            self.numbers.append(y)
            return True
        else:
            return False

    def search_data(self, x):
        """Search for an integer in the collection and return its indices or -1 if not found."""
        if x not in self.numbers:
            return [-1]
        else:
            return [i for i, number in enumerate(self.numbers) if number == x]
