from json import load
from MergeInsertionSort import mergeInsertionSort
import numpy as np
import pandas as pd


def runTest():
    result = []

    with open('data100000.txt', 'r') as file:
        array = load(file)

    for S in range(101):
        copyArray = array.copy()
        result.append(mergeInsertionSort(S, copyArray, 0, len(array) - 1))
        print(f'S: {S}, Key: {result[-1]}')

    pd.DataFrame(np.asarray(result)).to_csv('Result_c_ii.csv', index_label = 'S', header = ['Key Comparison'])


# Do not run unless you are sure you want to overwrite the file
# runTest()