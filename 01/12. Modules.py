#전부 import
import math

#일부 import
#from math import ceil, fsum...
#from math import ceil as sexy 등으로 바꿀수 있음
#다른 파일에서 정의한 것도 import 할 수 있음

a=float(input('올림할 숫자 입력'))
a_result=math.ceil(a)
print(a_result)

b=float(input('절대값 할 숫자 입력'))
b_result=math.fabs(b)
print(b_result)

c=[int(x) for x in input('공백으로 구분').split()]
c_result=math.fsum(c)
print(c_result)

from 'C:\Users\cmh\OneDrive - konkuk.ac.kr\바탕 화면\작업\동계\코딩\Python\08. Code Challenge' import plus
d_result=plus(a, b)
print(d_result)