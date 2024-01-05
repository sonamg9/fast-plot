import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

######################################################

def plot_columns_2d_array(array_2d, vector_1d, nCols, offset , title='', xlabel='', ylabel=''):

    '''
    array_2d : 2d numpy array
    vector_1d : 1D xaxis
    nCols     : number of columns to be plotted
    offset    : offset to be appended, set to 0 for no offset
    title string,
    xlabel string,
    ylabel string
    '''


    if not isinstance(array_2d, np.ndarray) or not isinstance(vector_1d, np.ndarray):
        raise ValueError("Both inputs must be NumPy arrays.")

    if array_2d.ndim != 2 or vector_1d.ndim != 1:
        raise ValueError("The first input should be a 2D NumPy array, and the second input should be a 1D NumPy array.")

    if array_2d.shape[0] != vector_1d.shape[0]:
        raise ValueError("Number of rows in the 2D array must match the length of the 1D array.")

    # generate colors (rainbow)
    color = iter(cm.rainbow(np.linspace(0, 1, nCols)))

    for i in range(nCols):
        col = next(color)
        plt.plot(vector_1d, array_2d[:,i] + (i * offset) , c=col )

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()
    plt.show()

######################################################
