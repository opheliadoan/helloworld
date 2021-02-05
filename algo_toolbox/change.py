# Uses python3

def get_change(m):
    changes = 0
    while (m > 0):
    	coin = 0
    	if m >= 10:
    		coin = 10
    	elif 5 <= m < 10:
    		coin = 5
    	else:
    		coin = 1
    	changes += 1
    	m -= coin
    return changes
    

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
