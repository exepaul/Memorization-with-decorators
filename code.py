def memo(func):
    memory={}

    def wrapper(x):
        if x not in memory:
            memory[x]=func(x)
        return memory[x]
    return wrapper



def factorial(d):
    if d==0:
        return 0
    elif d==1:
        return 1
    else:
        return factorial(d-1)+factorial(d-2)
factorial=memo(factorial)
for i in range(1,5):
    print(factorial(i))
    
    
    
    # or we could use this :

def memo(func):
    memory={}

    def wrapper(x):
        if x not in memory:
            memory[x]=func(x)
        return memory[x]
    return wrapper

@memo

def factorial(d):
    if d==0:
        return 0
    elif d==1:
        return 1
    else:
        return factorial(d-1)+factorial(d-2)
for i in range(1,5):
    print(factorial(i))
