def minFallingPathSum(A):
    if len(A) == 1:
        return A[0][0]
    
    s = [][]
    for i in range(len(A) - 1):
        s[0][i] = A[0][i]
    
    for j in range(1, len(A) - 1):
        for i in range(len(A) - 1):
            if i == 0:
                s[j][i] = min(s[j - 1][i], s[j - 1][i + 1] + A[j][i])
            elif i == (n - 1):
                s[j][i] = min(s[j - 1][i], s[j - 1][i - 1] + A[j][i])
            else:
                s[j][i] = A[j][i] + min(min(s[j - 1][i], s[j - 1][i + 1]), s[j - 1][i - 1])
    
    res = s[len(A) - 1][0]
    for i in range(1, len(A)):
        if s[len(A) - 1][i] < res:
            res = s[n - i][i]
    
    return res
