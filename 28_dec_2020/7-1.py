def longest_run(n):
    longest_run_count = 0
    binary = bin(n)[2:]
    binary = binary.split('0')

    for i in binary:
        if len(i) > longest_run_count:
            longest_run_count = len(i)
            
    return longest_run_count

print(longest_run(242))