"""

file: sorts.py
author: Shantanav Saurav << ss9415@g.rit.edu >>
purpose: Compare sorting algorithms and graph the run times of each one to visualize their Big O complexities

"""
import time, random, sys
import matplotlib.pyplot as plt # 'pip install matplotlib' to use this module


import insertion_sort, quick_sort, merge_sort, selection_sort
# To add more: ensure file with sort exists in directory, and add sorting function to list below

SAMPLE_SIZE = int(sys.argv[1]) # Number of iterations to be tested
INITIAL = int(sys.argv[2]) # Initial value 
STEP = int(sys.argv[3]) # Incrementer

RANGE_MIN = 0
RANGE_MAX = 100 # Random number generation range MAX

SORTS = [
    insertion_sort.insertion_sort, 
    quick_sort.quick_sort, 
    merge_sort.merge_sort, 
    selection_sort.selection_sort,
]

def generate_data(sample_size: int, init: int, step: int) -> None:
    """
    Determine the running time of sorting algorithms
    ----Pre Conditions:
    sample_size -> int: Sample size of data
    init -> int: Starting number of elements to sort
    step -> Increment to initial value
    None of the SORTS can be in-place
    ----Post Conditions:
    return -> dict: Dictionary of sort names as keys to list of ordered pairs (size, time)
    """
    results = dict()
    count = 0
    while count < sample_size:
        size = init + (step * count)
        lst = [random.randint(RANGE_MIN, RANGE_MAX) for i in range(size)]
        for fn in SORTS:
            start = time.time()
            fn(lst)
            end = time.time()
            if fn.__name__ in results:
                results[fn.__name__] += [(size, (end - start))]
            else:
                results[fn.__name__] = [(size, (end - start))]    
        count += 1 
    return results


def test(data):
    """
    Pretty print data set
    ----Pre Conditions:
    data -> dict: Dictionary of sort names as keys to list of ordered pairs (size, time)
    ----Post Conditions:
    return -> None
    """
    for key in data:
        print(key + ":")
        for elem in data[key]:
            print("\t" + str(elem[0]) + " --> " + str(elem[1]))


def graph(data):
    """
    Graph results of sorting algorithm times
    ----Pre Conditions:
    data -> dict: Dictionary of sort names as keys to list of ordered pairs (size, time)
    ----Post Conditions:
    return -> None
    """
    plt.title("Sorting Algorithm Times Taken")
    plt.xlabel("List Size (number of elements)")
    plt.ylabel("Time (seconds)")
    for key in data:        
        x, y = list(), list()
        for elem in data[key]:
            x += [elem[0]]
            y += [elem[1]]
        plt.plot(x, y, label=key)
    plt.legend()
    plt.show()


def main():
    """
    Main Function for Run
    ----Pre/Post:
    N/A
    """
    data = generate_data(SAMPLE_SIZE, INITIAL, STEP)
    test(data)
    graph(data)


if __name__ == "__main__":
    main()

