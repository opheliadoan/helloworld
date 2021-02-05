# Uses python3
import sys
import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
def min_and_max(i, j):
    minimum = math.inf
    maximum = -math.inf
    for k in range(i, j):
                
        a = evalt(M[i][k], M[k + 1][j], dataset[2 * k + 1])
                
        b = evalt(M[i][k], m[k + 1][j], dataset[2 * k + 1])
                
        c = evalt(m[i][k], m[k + 1][j], dataset[2 * k + 1])
               
        d = evalt(m[i][k], M[k + 1][j], dataset[2 * k + 1])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum

def get_maximum_value(dataset):
    #write your code here
    
    for i in range(dim):
        m[i][i] = int(dataset[2 * i])
        M[i][i] = int(dataset[2 * i])
    #print(M)
    # calcuate subproblems E(i, j) = d_i op_i ... op_{j-1} dj
    #print(dim)
    for s in range(dim):
        for i in range(dim - s - 1):
            j = i + s + 1
            minVal, maxVal = min_and_max(i, j)
                
            m[i][j] = minVal
            M[i][j] = maxVal
    #print(M)
 
    return M[0][dim - 1]


if __name__ == "__main__":
    dataset = input()
    dim = int((len(dataset) + 1)/2)
    m = [[0 for i in range(dim)] for j in range(dim)]
    M = [[0 for i in range(dim)] for j in range(dim)]
   
    print(get_maximum_value(dataset))
    
