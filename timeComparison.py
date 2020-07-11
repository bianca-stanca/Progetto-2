xfrom DCT import DCT
from scipy import fftpack as fft
import timeit
import numpy as np
from matplotlib import pyplot as plt

def generate_matrix(N):
    """
    Creates a random square matrix of pixels, size NxN.

    Parameters
    ----------
    N: int

    Returns
    ----------
    matrix: ndarray
    """
    matrix = np.random.random_integers(0, 255, (N, N))

    return matrix



def compare_execution_times(executions):
    """
    Runs both proposed DCT and library DCT ten times. Then averages out the
    times and plots the results.
    Parameters
    ----------
    executions: int
            units by which to increment matrix size

    """

    #setup array for graphing execution times. Toggle comments in order to
    #test either home made or library fft
    fftDCTTime = np.zeros(executions+8)


    ourDCTTime = np.zeros(executions+8)

    #declare as global in order for timeit to be able to use it
    global matrix
    n3 = np.zeros_like(ourDCTTime)
    for i in np.arange(8, 8+executions):
        n3[i] = np.power(i, 3)
        matrix = generate_matrix(i)
        print(i)
        setupHomeMade = '''from DCT import DCT
        '''
        setupFFT = '''from scipy import fftpack as fft
        '''
        # homeMadeDCT = np.zeros((i, i))
        fftDCT = np.zeros((i, i))

        ourCode = '''homeMadeDCT = DCT.proposed_DCT(matrix)
        '''

        fftCode = '''fftDCT = fft.dctn(matrix, norm='ortho')
        '''
        ourDCTTime[i] = timeit.timeit(ourCode, setupHomeMade,
        globals = globals(), number=10)/10

        fftDCTTime[i] = timeit.timeit(fftCode, setupFFT,
        globals = globals(), number=10)/10


    library = plt.semilogy(fftDCTTime, label="Library DCT")
    proposed = plt.semilogy(ourDCTTime, label="Proposed DCT")
    n3_plot = plt.semilogy(n3, label="N^3")
    plt.legend()
    plt.xlim(xmin=8, xmax = executions+8)
    plt.xlabel("Matrix dimension")
    plt.ylabel("Execution Time")

    plt.show()
