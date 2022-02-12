#def say_hello():
#say_hello()

Cha_Cha={
    'name':'Cha Cha',
    'age':26,
    'korean':True,
}

def say_hello():
    print('hello',Cha_Cha['name'])

say_hello()

#############

def say_hello(who):
    print('hello', who)

say_hello(Cha_Cha['name'])