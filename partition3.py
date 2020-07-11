from itertools import product
from sys import stdin


def partition3(values):
    sum = 0
    for i in range(len(values)):
    	sum += values[i]
    if sum % 3 != 0 or len(values) < 3:
    	return 0
    # check if there exists 2 subsets both with sum of sum // 3
    rows = len(values) + 1
    cols = (sum // 3) + 1
    p = [[0 for j in range(cols)] for i in range(rows)]
    # i stands for items used
    # j stands for the sum of subset
    for j in range(1, cols):
    	for i in range(1, rows):
    		p[i][j] = p[i - 1][j]
    		if ((values[i - 1] <= j) and p[i - 1][j - values[i - 1]]) or (values[i - 1] == j):
    			if p[i - 1][j] == 0:
    				p[i][j] = 1
    			else:
    				p[i][j] = 2
    
    if p[len(values)][sum//3] == 2:
    	return 1
    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))