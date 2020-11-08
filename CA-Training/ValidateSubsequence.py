def isValidSubsequence(array, sequence):
    arrayIdx = 0
    seqIdx = 0
    while arrayIdx < len(array) and seqIdx < len(sequence):
        if array[arrayIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrayIdx += 1
    return len(sequence) == seqIdx

print(isValidSubsequence([5,1,22,25,6,-1,8,10],[1,6,-1,10]))