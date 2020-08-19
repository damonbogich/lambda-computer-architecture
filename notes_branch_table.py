#Branch Tables (AKA DISPATCH TABLES)

def fun1(x,y):
    print(f'fun1, {x}, {y}')

def fun2(x,y):
    print(f'fun2, {x}, {y}')

def fun3(x,y):
    print(f'fun3, {x}, {y}')

def fun4(x,y):
    print(f'fun4, {x}, {y}')



def better_call_fun(n, x=None, y=None):
    branch_table = {
        1: fun1,
        2: fun2,
        3: fun3,
        4: fun4
    }
    # f = branch_table[n]
    # f(x,y)
    branch_table[n](x,y)

better_call_fun(2, 99, 100)

def call_fun(n, x=None, y=None):
    if n == 1:
        fun1(x,y)
    if n == 2:
        fun2(x,y)
    if n == 3:
        fun3(x,y)
    if n == 4:
        fun4(x,y)