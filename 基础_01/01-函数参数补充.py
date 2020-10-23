# 1.命名关键字参数(了解)
# 定义函数时，*后定义的参数，如下所示，称之为关键字参数
# 特点:

# 1.命名关键字实参，必须按照key=value形式为其传值
# 2.
def func(x, y, *, a, b):  # a,b 称之为命名关键字参数
    print(x, y)
    print(a, b)


# 通过关键字形式的命名传递实参
func(1, 2, a=1, b=3)
