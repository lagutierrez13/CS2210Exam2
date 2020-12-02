def countSubstrings(st):
    return palindromicSubstrings(st, 0, len(st) - 1)

def isPalindrome(st, i, j):
    while(i <= j):
        i += 1
        j -= 1
        if st[i] != st[j]:
            return False
    return True  

def palindromicSubstrings(st, start, end):
    if(start > end):
        return 0

    if(start == end):
        return 1

    totalCount = 0

    if isPalindrome(st, start, end):
        totalCount = 1;

    totalCount += palindromicSubstrings(st, start + 1, end)

    totalCount += palindromicSubstrings(st, start, end - 1)

    totalCount -= palindromicSubstrings(st, start + 1, end - 1)

    return totalCount