import os
import requests
import sys
import requests

################################################함수부

def inputa():
  print('Please write a URL or URLs you want to check. (separated by comma)')
  return input()

def check_URL():
    ok = []
    if input1.count(',') >= 1:
        input2 = input1.split(',')

        for x in input2:
            if x.count('.') < 1:
                print(f'{x} is not a valid URL.')
                ok.append('1')
            else: 
              if x.count('http') < 1:
                URL.append(('http://'+x.strip()).lower())
              else:
                URL.append((x.strip()).lower())

        if ok.count('1') >=1:
            return 1

    else:
        if input1.count('.') < 1:
            print(f'{input1} is not a valid URL.')
            return 1
        else:
            if input1.count('http') < 1:
              URL.append(('http://'+input1.strip()).lower())
            else:
              URL.append((input1.strip()).lower())
            return 0

def again():
  b = 1
  while b != 0:
    b=(input('Do you want to start over? y/n ')).lower()
    if b == 'y':
      b=0
      return 1
    elif b == 'n':
      b = 0
      return 0
    else:
      print('That\'s not a valid answer')

def bye():
  print('k. bye!')

def valid():
  for x in URL:
    try:
      r = requests.get(x)
      if r.status_code == 200:
        print(f'{x} is up!')
      else:
        print(f'{x} is down!')
    except:
      print(f'{x} is down!')

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')



######################################################실행부

a = 1
b = 1
while a != 0:
  URL = []
  input1 = ''
  input1 = inputa()
  if check_URL() != 1:
    valid()
  a = again()
  if a == 1:
      clearConsole()
bye()