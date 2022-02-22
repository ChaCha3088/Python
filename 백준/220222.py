a = int(input('put some numbers between 0 ~ 99'))
left = 0
right = 0
result = 0

def test(a):
    if a < 10:
        a = str(a)
        result = '0'+ a
    else:
        result = str(a)
    return result

def process(a):
    a = test(a)
    left = a[0]
    right = a[1]
    left = int(left)
    right = int(right)
    result = left + right
    result = test(result)
    right = str(right)
    result = str(result)
    result_right = result[1]
    result = right + result_right
    result = int(result)
    return result

def iteration(a):
    storage = a
    count = 1
    c = process(a)
    while c != storage:
        a = process(c)
        c = a
        count = count + 1
    
    return count

print(iteration(a))