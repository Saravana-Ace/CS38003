# Write a function called sort_and_plot(x) that sort the input sequence x and display the sorted sequence in both
# ascending and descending order using matplotlib.pyplot. This visualization shows you the result of sorting.
# Do not create tick marks for x-axis. Include legends for points displayed.
# Note: This part will be manually graded!

import matplotlib.pyplot as plt
import numpy as np

def sort_and_plot(x):
    plt.plot(x, color = "black", label = "Original")
    arr = np.sort(np.array(x))
    plt.plot(arr, color = "blue", label = "Ascending")
    plt.plot(arr[::-1], color = "red", label = "Descending")
    plt.xticks([])
    plt.legend()
    plt.show()

sort_and_plot([5,1,6,3,7,9,2,4,8])
