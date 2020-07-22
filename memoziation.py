def fibonacci(n,d):
    if n in d:
        print(f'here {n} from dictionary {d}')
        return d[n]
    elif n == 0:
        ans = 0
    elif n == 1:
        ans = 1
    else:
        print(f'last call')
        ans = fibonacci(n-1, d) + fibonacci(n-2,d)
    d[n]=ans
    print(f'here n is {n} from dictionary & answer is {ans}')
    return ans

print(fibonacci(3,{0:0,1:1}))