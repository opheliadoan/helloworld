# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    r = len(weights) + 1
    c = capacity + 1
    values = [[0 for i in range(c)] for j in range(r)]
    
    for i in range(1, r):
    	for w in range(1, c):
    		values[i][w] = values[i - 1][w]
    		if weights[i - 1] <= w:
    			val = values[i - 1][w - weights[i - 1]] + weights[i - 1]
    			if values[i][w]  < val:
    				values[i][w] = val
   
    return values[len(weights)][capacity]


if __name__ == '__main__':
    input_capacity, n= list(map(int, input().split()))
    input_weights = list(map(int, input().split()))
    assert len(input_weights) == n
    #print(input_weights)
    print(maximum_gold(input_capacity, input_weights))
