"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_multiples():
    total = 0
    for n in range(0,1000):
        if not(n%5) or not(n%3):
            total += n
    return total


if __name__ == "__main__":
    print(get_multiples())