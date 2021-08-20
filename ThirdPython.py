# anthor: zhangwei time:2020/11/23
# 关于input
# present = input('gift is?')
# print(present, type(present))

# input 用户键入的是str类型
# 关于运算符
# + - * / 和 //(整除) %(取余) **(幂运算)

# 一正一负的整除向下取整
# 遵循公式    余数=被除数-除数*商

# 赋值运算符 执行顺序 从右到左
# 支持链式赋值 a=b=c=20
# id 表示在内存中的位置
a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

# += -= *= /= //= %=
# 支持系列解包赋值
d, e, f = 10, 20, 30
# 交换两个变量的值
x, y = 10, 20
print('交换之前', x, y)
x, y = y, x
print('交换之后', x, y)

# 比较运算符 > < >= <= != ==
# 比较运算符的结果是bool类型

# 一个变量由3部分组成，标识，值，类型
# ==比较的是值
# 比较对象的标识使用的是  is

a1 = 10
a2 = 10
print(a == b)  # value 相同
print(a is b)  # id 相同

list1 = [11, 22, 33]
list2 = [11, 22, 33]
print(list1 == list1)
print(list1 is list2)

# 布尔运算符 and or not
# 与C不同  in 和 not in
str1 = 'hello world'
print('w' in str1)
print('k' not in str1)

# 位运算符 ：将数据转成二进制进行计算
print(4 & 8)  # 按位与& 同为1时结果为1
print(4 | 8)  # 按位或| 同为0是结果为0

# 左移<< 右移>>  左移相当于乘2 右移相当于除2 左移高位溢出舍弃，低位补0  右移低位溢出舍弃，高位补0
print(4 << 2)  # 左移两位
print(4 >> 2)

# 运算符的优先级
# 算数>位运算符>比较运算符>布尔运算符>赋值运算符
# ** * / % > (<<) (>>) & | >  (>)(<)(>=)(<=) > and or >  =