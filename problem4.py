def minDeleteSum(s1, s2, i = 0, j = 0):
    if(i == len(s1) and j == len(s2)):
        return 0;
    
    if(i == len(s1)):
        return minDeleteSum(s1, s2, i, j + 1) + chr(s2[j])

    if(j == len(s2)):
        return minDeleteSum(s1, s2, i + 1, j) + chr(s1[i])
    
    if(s1[i] == s2[j]):
        return minDeleteSum(s1, s2, i + 1, j + 1)
    else:
        return min(minDeleteSum(s1, s2, i + 1, j) + chr(s1[i]), minDeleteSum(s1, s2, i, j + 1) + s2[j])