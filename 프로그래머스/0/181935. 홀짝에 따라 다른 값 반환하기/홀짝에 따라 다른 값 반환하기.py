def solution(n):


    if n % 2 == 1:
        return sum(range(1, n+1, 2))
        
    else:  
        a = 0
        for k in range(2, n+1, 2):
                a = a + k ** 2
        return a
    
   