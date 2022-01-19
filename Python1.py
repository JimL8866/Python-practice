def add():
    x = 200
    def multiply():
        print(x * 100)
    return multiply

add_number = add()
add_number()
# 简单的闭包，返回值是函数.
# 函数也是object. 定义一个新函数。执行新函数


def wrapper(func):
    def multiply():
        y = func() * 2
        print(y)
    return multiply

def add():
    x = 10
    y = 20
    return x + y
# 不用print. 因为print在控制台输出，函数的值带不进去

add_number = wrapper(add)
add_number()
# 可以用函数对象的输出形式 或 语法糖
@wrapper
def add():
    x = 300
    y = 100
    return x + y
add()

def wrapper(func):
    def multiply(*args):
        y = func(*args) * 2
        print(y)

    return multiply


def add(x, y):
    return x + y


add_number = wrapper(add)
add_number(30, 40)
# 函数object的参数最后带入。语法糖也可
