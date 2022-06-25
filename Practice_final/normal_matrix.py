# Description:
# You need to write a function called normalize_matrix, which takes a numpy
# matrix A as argument. It should undertake the following steps to normalize 
# the matrix, A, passed as argument: (1) calculate the mean value of A, denoted
# by m. (2) calculate the variance of A, denoted by v. (3) then for every value
# x in A, x is normalized by (x - m) / sqrt(v + 1e-9) (4) return the normalized
# matrix
#
# Examples:
# > A = np.array([[4], [2]])
# > print(A)
# > [[4]
# [2]]
# > print(normalize_matrix(A))
# > [[ 1.]
# [-1.]]
#
# > A = np.array([[1, 2, 3, 4, 5, 6]])
# > print(A)
# > [[1 2 3 4 5 6]]
# > print(normalize_matrix(A))
# > [[-1.46385011 -0.87831007 -0.29277002 0.29277002 0.87831007 1.46385011]]
#
# > A = np.array([[1, 2, 3], [0, 4, 2]])
# > print(A)
# > [[1 2 3]
# [0 4 2]]
# > print(normalize_matrix(A))
# > [[-0.77459667 0. 0.77459667]
# [-1.54919334 1.54919334 0. ]]
#
# > A = np.array([[1, 2], [0, 0]])
# > print(A)
# > [[1 2]
# [0 0]]
# > print(normalize_matrix(A))
# > [[ 0.30151134 1.50755672]
# [-0.90453403 -0.90453403]]
