import numpy as np
import scipy as sp


class DCT:

    @staticmethod
    def proposed_DCT(matrix):
        """ Calculates DCT on given matrix or array.
        """
        if(type(matrix)!=np.ndarray):
            try:
                matrix = np.ndarray(matrix)
            except Exception:
                raise Exception("Cannot convert to numpy ndarray")
        if(len(matrix.shape) == 1):
            return DCT.__proposed_DCT1(matrix)
        elif(len(matrix.shape) == 2):
            n = matrix.shape[0]
            m = matrix.shape[1]

            dct = np.zeros(matrix.shape)
            for i in range(n):
                dct[i] = DCT.__proposed_DCT1(matrix[i])
            for j in range(m):
                dct[:, j] = DCT.__proposed_DCT1(dct[:, j])
            return dct
        else:
            raise Exception("Only 1D and 2D arrays accepted")

    @staticmethod
    def proposed_IDCT(matrix):
        if(type(matrix)!=np.ndarray):
            try:
                matrix = np.ndarray(matrix)
            except Exception:
                raise Exception("Cannot convert to numpy ndarray")
        if(len(matrix.shape) == 1):
            return DCT.__proposed_IDCT1(matrix)
        elif(len(matrix.shape) == 2):
            n = matrix.shape[0]
            m = matrix.shape[1]
            idct = np.zeros(matrix.shape)
            for i in range(n):
                idct[i] = DCT.__proposed_IDCT1(matrix[i])
            for j in range(m):
                idct[:, j] = DCT.__proposed_IDCT1(idct[:, j])
            return idct
        else:
            raise Exception("Only 1D and 2D arrays accepted")

    @staticmethod
    def __proposed_DCT1(array):
        length = array.shape[0]
        dct = np.zeros(length)
        alpha = DCT.__alpha_factor(length)
        for i in range(length):
            sum = 0
            for j in range(length):
                sum += array[j]*np.cos((np.pi*i*(2*j+1))/(2*length))
            dct[i] = alpha[i]*sum
        return dct

    @staticmethod
    def __proposed_IDCT1(array):
        length = array.shape[0]
        idct = np.zeros(length)
        alpha = DCT.__alpha_factor(length)
        for i in range(length):
            for j in range(length):
                idct[i] += array[j]*alpha[j]*np.cos((np.pi*j*(2*i+1))/(2*length))
        return idct

    @staticmethod
    def __alpha_factor(N):
        alpha = np.zeros(N)
        alpha[0] = np.sqrt(1/N)
        alpha[1:] = np.sqrt(2/N)
        return alpha
