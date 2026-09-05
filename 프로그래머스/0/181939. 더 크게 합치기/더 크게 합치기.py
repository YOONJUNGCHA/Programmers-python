def solution(a, b):
    answer = 0
    
    c = str(a)
    d = str(b)
    e = c+d
    f = d+c
    
    if int(e) >= int(f):
        return int(e)
    else: return int(f)

    return answer