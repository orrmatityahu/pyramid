from file_utils import build_pyramid
from math_utils import build_paths, calculate_sum_for_paths, count_duplicates_numbers_in_array, sort_dict


def main():
    file_name = 'input.txt'
    # get pyramid array
    try:
        pyramid = build_pyramid(file_name)
    except IOError:
        print 'File {} does not exist'.format(file_name)
        return

    # get all paths
    paths = list(build_paths(pyramid))

    # calculate all sums and count every sum in dict
    sums = calculate_sum_for_paths(paths)
    counted_sums = count_duplicates_numbers_in_array(sums)

    # sort dict
    final_result = sort_dict(counted_sums)

    # print final table
    print "{} | {}".format('Sum', 'Count')
    for route_sum in final_result:
        print "{} | {}".format(route_sum, counted_sums[route_sum])

if __name__ == "__main__":
    main()