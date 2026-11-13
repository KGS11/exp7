
import unittest

# Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b


# Unit testing class
class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(20, 20), 40)

    def test_subtract(self):
        self.assertEqual(subtract(20, 20), 0)

    def test_mul(self):
        self.assertEqual(mul(20, 20), 400)


# Student Calculator Application
if __name__ == "__main__":

    print("Student Calculator Application")

    print("Addition:", add(20, 20))
    print("Subtraction:", subtract(20, 20))
    print("Multiplication:", mul(20, 20))

    print("\nExecute Automated Tests")

    unittest.main(argv=['first-arg-ignored'], exit=False)
