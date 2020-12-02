def arithmeticSlices(A, i = 2, total = 0, prevTotal = 0):
    if len(A) <= i:
        return total

    if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
        return arithmeticSlices(A, i + 1, total + 1, prevTotal, prevTotal + 1)
        
    return arithmeticSlices(A, i + 1, total, 0)   