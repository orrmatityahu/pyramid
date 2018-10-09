def build_pyramid(input_file_name):
    """
    build a pyramid array from a given input file
    :param input_file_name: input file name - must be in current folder
    :return: an array of arrays that represents pyramid
    """
    with open(input_file_name, "r") as file:
        lines = file.readlines()
    list_tree = []
    for line in lines[0:]:
        list_tree.append([int(n) for n in line.strip().split(" ")])

    return list(list_tree)