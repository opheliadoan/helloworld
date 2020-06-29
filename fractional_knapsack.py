# Uses python3

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    unit_value = []
    for i in range(len(weights)):
    	unit_value.append(values[i]/weights[i])
    
    while (len(unit_value) > 0 and capacity > 0):
    	max_index = unit_value.index(max(unit_value))
    	unit_value.pop(max_index)
    	fraction = 0
    	if(weights[max_index] <= capacity):
    		fraction = 1
    	else :
    		fraction =  capacity/weights[max_index]
    		
    	value += values[max_index] * fraction
    	capacity = int(capacity - weights[max_index] * fraction)
    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n = data[0]
    capacity = data[1]
    weights = []
    values = [] 
    for i in range(n):
    	data = list(map(int, input().split()))
    	weights.append(data[1])
    	values.append(data[0])
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
