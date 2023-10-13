import random
import datetime
import os


def get_word_of_the_day():
    with open(os.path.join(os.path.dirname(__file__), "word_list.txt"), "r") as f:
        words = f.readlines()
        file_length = len(words)
        random.seed(int(datetime.datetime.now().strftime("%Y%m%d")))
        return words[random.randint(1, file_length)].strip().upper()


def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return False


def get_word_list():
    with open(os.path.join(os.path.dirname(__file__), "word_list.txt"), "r") as f:
        return sorted(f.read().split("\n")[1:])


def check_character(guess_character, answer):
    return {
        "char": guess_character,
        "scoring": {
            "in_word": guess_character in answer,
            "correct_idx": guess_character == answer
        }
    }
