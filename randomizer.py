import random

# List of names in your company
names = [
    " "
]

def randomize_names():
    """
    Generates a new list of names in random order and prints them.
    """
    shuffled_names = random.sample(names, len(names))  # Generates a new shuffled list
    for name in shuffled_names:
        print(name)

if __name__ == "__main__":
    randomize_names()
