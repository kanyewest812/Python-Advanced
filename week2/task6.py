def all_eq(words):
    m = 0
    
    for s in words:
        if len(s) > m:
            m = len(s)
    
    result = []
    
    for s in words:
        if len(s) < m:
            s = s + "_" * (m - len(s))
        result.append(s)
    
    return result
print(all_eq(["cat", "elephant", "dog"]))
