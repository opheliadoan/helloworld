# python3

def compute_min_refills(distance, tank, stops):
	cur, refills, max_dist = 0, 0, tank
	while max_dist < distance:
		# impossible to reach the destination if
		# the next stop is beyond the tank capacity
		# i.e no stop in between the last stop and the dest 
		if cur >= len(stops) or stops[cur] > max_dist:
			return -1
		# find the furthest stop that can be reached
		# and increment cur
		# or else cur is preserved and tank must be refilled at stops[cur]
		while cur < len(stops) - 1 and stops[cur + 1] <= max_dist:
			cur += 1
		refills += 1
		# the new maximum point that can be reached
		# will be the next stop 
		max_dist = tank + stops[cur]
		cur += 1
	return refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    print(compute_min_refills(input_d, input_m, input_stops))
   
