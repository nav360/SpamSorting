def maxSubSum3(values):
    max_sum = 0
    this_sum = 0
    j = 0
    while (j < len(values)):
        this_sum = this_sum + values[j]
        if (this_sum > max_sum):
            max_sum = this_sum
        else:
            if (this_sum < 0):
                this_sum = 0
        j = j+1
    print(max_sum)
    print(j)
    print(this_sum)
    
print(maxSubSum3([5, -1, -6, 3, 7, -8]))