import os
import json

cwd_path = os.getcwd()
file_path = "files"


def read_data(file_name, key="ordered_numbers"):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, str), sequential data
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(os.path.join(cwd_path, file_path, file_name), mode="r") as json_file:
        seqs = json.load(json_file)

    return seqs[key]


def binary_search(seq, number):
    """
    Function performs binary search on !!ordered!! sequence and stores position of match if found.
    :param seq: (list): list of numbers
    :param number: (int): number to match within sequence
    :return: (int, None): index of match if found, None otherwise
    """
    left, right = (0, len(seq) - 1)

    while left <= right:
        middle = (right + left) // 2

        if number < seq[middle]:
            right = middle - 1
        elif number > seq[middle]:
            left = middle + 1
        else:
            return middle
    return None


def recursive_binary_search(seznam, hledana_hodnota, left, right):

    middle = (left + right) // 2


    if hledana_hodnota not in seznam:
        return None
    elif hledana_hodnota == seznam[middle]:
        return middle
    elif seznam[middle] < hledana_hodnota:
        return recursive_binary_search(seznam, hledana_hodnota, middle + 1, right)
    elif seznam[middle] > hledana_hodnota:
        return recursive_binary_search(seznam, hledana_hodnota, left, middle - 1)


def main(file_name, number):
    sequence = read_data(file_name=file_name, key="ordered_numbers")

    # iterative binary search
    binary_search(sequence, number=number)
    left = 0
    right = len(sequence) - 1
    print(recursive_binary_search(sequence, my_number, left, right))

if __name__ == "__main__":
    my_file = "sequential.json"
    my_number = 14
    main(my_file, my_number)
