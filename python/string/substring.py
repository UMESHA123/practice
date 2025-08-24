def substring(s):
    start = 0
    res = 0
    dist = {}
    index = 0
    count = 0
    while start < len(s):
        if s[start] not in dist:
            count = count + 1
            dist[s[start]] = index
            start = start + 1
            index = index + 1
        else:
            count = 0
            
            start = dist[s[start]] + 1
            del dist[s[start-1]]
        res = max(res, count)
    return res

s = "dvdf"
print(substring(s))