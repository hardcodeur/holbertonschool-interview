def minOperations(n) :
    if n <= 1 :
        return 0
    
    steps = 0
    divisor = 2

    while n > 1 :
        while n % divisor == 0 : 
            steps += divisor
            n = divisor
        divisor +=1
    return steps           
