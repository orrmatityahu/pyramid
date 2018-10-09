def build_paths(rows, current_row=0, start=0):
    """
    a recursive function to build all paths in rows
    :param rows: an array of array that represents rows in pyramid
    :param current_row: current row  - 0 is default to start from first row
    :param start: from where to start in the row
    :return: array of arrays - every array is path in the pyramid
    """
    # gets the index and number of each number in the row
    for i, num in enumerate(rows[current_row]):
        # Checks if it is within 1 number radius, if not it skips this one.
        if not (0 <= (i - start) < 2):
            continue
        # We are iterating through the last row so simply yield the number as it has no children
        if current_row == len(rows) - 1:
            yield [num]
        else:
            # This is not the last row so get all children of this number and yield them
            for child in build_paths(rows, current_row + 1, i):
                yield [num] + child


def calculate_sum_for_paths(paths):
    """
    calculate sum of each array in paths
    :param paths: all the paths in the pyramid
    :return: an array of all the sums of the pyramid
    """
    sums = []
    for path in paths:
        sums.append(sum(path))
    return sums


def count_duplicates_numbers_in_array(arr):
    """
    count how much time each number is present in arr
    :param arr: array of numbers
    :return: dict of all the numbers and in each value there is the times it present in arr
    """
    counted = {}

    for num in arr:
        if num in counted:
            counted[num] += 1
        else:
            counted[num] = 1

    return counted


def sort_dict(some_dict):
    """
    sort a dict by value of keys
    :param some_dict: dict to sort
    :return: sorted dict
    """
    return sorted(some_dict, key=some_dict.get, reverse=True)