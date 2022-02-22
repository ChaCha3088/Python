def plus(a, b, *args):
    print(args)
    return a + b

# *args는 위치에 맞춰 원하는 만큼 받을 수 있음 - Tuple
# **kwargs는 원하는 만큼 키워드로 받을 수 있음



#무한 계산기
def plus(*args):
    result = 0
    print(args)
    for number in args:
        result += number
    return result

print(plus(1,2,3,4,5))