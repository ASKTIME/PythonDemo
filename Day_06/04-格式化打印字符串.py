# % 占位符表示格式化一个字符串

# %s --> 字符串占位符
# %d --> 整数的占位符
#  %nd --> 打印时，显示n位，如果不够在前面使用空格补全 - 在右边加空格
# %f --> 浮点数占位符
# %.nf -- > 保留小数点后n位
name = 'Tom'
age = 18
money = 15.2
print('我的名字是%s,年龄是%d,赚了%f' % (name, age, money))

print('%03d' % 6)
print('%6d' % 6)
print('%-3d' % 6)
