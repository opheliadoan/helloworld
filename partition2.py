from itertools import product
from sys import stdin


def partition2(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)
    sum = 0
    for i in range(len(values)):
    	sum += values[i]
    if sum % 2 != 0:
    	return 0
    rows = (sum//2) + 1
    cols = len(values) + 1
    p = [[0 for i in range(cols)] for j in range(rows)]
    # i represents the sum
    # j represents the number of items that can be used
    for i in range(0, rows):
    	p[i][0] = 0
    for j in range(0, cols):
    	p[0][j] = 1
    
    for i in range(1, rows):
    	for j in range(1, cols):
    		p[i][j] = p[i][j - 1]
    		# check if the last item is included
    		if (i >= values[j - 1]) and (p[i - values[j - 1]][j - 1] == 1):
    			p[i][j] = 1
    return p[(sum//2)][len(values)]


if __name__ == '__main__':
    input_n = int(input())
    input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    print(partition2(input_values))