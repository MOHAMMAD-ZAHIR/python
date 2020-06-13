def linearsearch(A, key):
    flag = False
    i = 0
    while i < len(A) and not flag:
        if A[i] == key:
            flag = True
        else:
            i = i + 1
    return flag
A = [10, 20, 30, 40, 22, 1, 45, 64, 25, 12, 14]
find = linearsearch(A, 14)
print(find)