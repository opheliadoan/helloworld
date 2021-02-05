# Uses python3
import sys
import random

def randomized_quick_sort(a, l, r):
    if r <= l:
        return
    x = a[l]
    m1 = l
    m2 = r
    i = l
    while (i <= m2):
        if a[i] < x: 
            a[m1], a[i] = a[i], a[m1]
            i += 1
            m1 += 1
        elif a[i] > x:
            a[m2], a[i] = a[i], a[m2]
            m2 -= 1
        else:
            i += 1
   
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
