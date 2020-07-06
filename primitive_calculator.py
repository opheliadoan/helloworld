# Uses python3

def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    min_num_seqs = [0] * (n + 1)
    
    for i in range(1, n + 1):
        min_num_seqs[i] = min_num_seqs[i - 1] + 1
        if i % 3 == 0:
            min_num_seqs[i] = min(min_num_seqs[i], min_num_seqs[i//3] + 1)        
        elif i % 2 == 0:
            min_num_seqs[i] = min(min_num_seqs[i], min_num_seqs[i//2] + 1)
            
    sequence = []
    while n >= 1:
        sequence.append(n)
        if min_num_seqs[n - 1] == min_num_seqs[n] - 1: n = n -1
        elif n % 2 == 0 and min_num_seqs[n//2] == min_num_seqs[n] - 1: n = n//2 
        elif n % 3 == 0 and min_num_seqs[n//3] == min_num_seqs[n] - 1: n = n//3
    return list(reversed(sequence))


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)

