def sumIntervals(x):
    print(x)
    s = []
    sum = 0
    for i in range(len(x)):
        s = s + x[i]
    s.sort()
    s = list(set(s))
    for i in range(len(s)-1):
        if s[i] != s[i+1]-1 or s[i] != s[i+1]+1:
            sum = sum + s[i+1] - s[i]
    print("Result: ", sum, "\n")


sumIntervals([[1, 5], [10, 20], [1, 6], [16, 19], [5, 11], [6, 10]])  # 19
sumIntervals([[0, 3], [6, 11], [0, 6], [11, 12]])  # 12
sumIntervals([[1, 2], [6, 8], [2, 15]])  # 14
sumIntervals([[1, 4], [7, 10]])  # 6
sumIntervals([[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]])  # 19
exit(0)
