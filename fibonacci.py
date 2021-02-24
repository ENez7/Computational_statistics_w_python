def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def dynamic_fibonacci(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except KeyError:
        res = dynamic_fibonacci(n-1, memo) + dynamic_fibonacci(n-1, memo)
        memo[n] = res
        
        return res

if __name__ == '__main__':
    n = int(input('Number: '))
    res = dynamic_fibonacci(n)
    print(res)