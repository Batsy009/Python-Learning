from collections import Counter
def highest_rank(arr):
    if arr:
        c = Counter(arr)
        m = max(c.values())
        return [max(k for k,v in c.items() if v==m)]

a = [1,2,1,2,2,3,2,3,4,2,5,2,5,2,2,2]
print(highest_rank(a))
