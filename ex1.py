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



sumIntervals([[1, 5], [11, 18], [0, 6], [16, 19], [5, 11], [6, 10]])  # 19
sumIntervals([[0, 6], [5, 17], [7, 12]])  # 17
sumIntervals([[10, 20]])  # 10
exit(0)
