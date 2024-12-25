from direct import *
A = [[3, -5, 47, 20],
    [11, 16, 17, 10],
    [56, 22, 11, -18],
    [17, 66, -12, 7]]

b = [18, 26, 34, 82]


resCramer = Cramer_method(A,b)
print("Result with Cramer's Method: ", resCramer)

resGaussian = Gauss_method(A, b)
print("Result with Gaussian Method:", resGaussian)

resJordan = Gauss_jordan(A, b)
print("Result with Gauss Jordan Method", resJordan)
