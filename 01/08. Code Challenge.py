#사칙연산 def로 함수 정의하기

def plus(a, b):
    return float(a)+float(b)

def minus(a, b):
    return float(a)-float(b)

def multi(a, b):
    return float(a)*float(b)

def div(a, b):
    return float(a)/float(b)

def moks(a, b):
    return float(a)//float(b)

def remain(a, b):
    return float(a)%float(b)



al=input('첫번째 숫자')
be=input('두번째 숫자')
result=minus(al,be)
print(result)