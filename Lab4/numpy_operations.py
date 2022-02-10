# create a matrix m1 of size 4x2 by drawing samples from a standard Normal distribution (mean=0, stdev=1). Hint: use np.random.standard_normal function
# create another matrix m2 of size 4x2 by drawing samples from a standard Normal distribution
# Multiply the m1 with the maximum value of matrix m2
# Square all elements of m2 using np.square
# Multiply resulting matrix in 3. with the transpose of the resulting matrix in 4. using matrix multiplication
# Compute and return the eigenvalues of the resulting matrix in 5. using linear algebra (imported as LA)

import numpy as np
from numpy import linalg as LA

def play_with_matrices():
    m1 = np.random.standard_normal(size=(4,2))
    m2 = np.random.standard_normal(size=(4,2))

    m1 = m1 * m2.max()
    m2 = np.square(m2)

    trans_m2 = m2.T
    new_matrix = m1.dot(trans_m2)

    w, v = LA.eig(new_matrix)
    return w

play_with_matrices()
