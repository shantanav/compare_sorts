"""

file: selection_sort.py
author: Ripped from https://www.geeksforgeeks.org/python-program-for-selection-sort/
purpose: Selection Sort

"""
def selection_sort(A):
    """
    Selection Sort Algorithm
    ----Pre Conditions:
    A -> list: List of values to be sorted
    ----Post Conditions:
    return -> List: List of sorted values
    """
    for i in range(len(A)):  
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j         
        A[i], A[min_idx] = A[min_idx], A[i]
    return A 