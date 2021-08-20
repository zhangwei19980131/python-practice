# anthor: zhangwei time:2020/11/23
import keyword

print(chr(0b100111001011000))  # 0b表示二进制
print(ord('乘'))  # 20056是十进制

print(keyword.kwlist)

name = '马丽亚'
print('标识', id(name))
print('类型', type(name))
print('值', name)

print('二进制', 0b11001010)  # 0b表示二进制
print('八进制', 0o1234567)  # 0o表示八进制
print('十六进制', 0x123aef)  # 0x表示十六进制

# 使用浮点数进行计算时，可能会出现小数位不确定的情况
#    解决方法： 导入模块 decimal

print(1.1 + 2.2)
print(1.1 + 2.1)  # 这个正常
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))

# 布尔类型可以转化为整数 true 为1  false 为0

f1 = True  # 1
f2 = False  # 0
print(f1, type(f1))
print(f2, type(f2))

print(f1 + 1)
print(f2 + 1)

# 关于字符串  三引号可以多行显示字符串
str1 = ('啦啦啦,啦啦啦')
str2 = ("啦啦啦,啦啦啦")
str3 = ("""啦啦啦,
啦啦啦""")
str4 = ('''啦啦啦,
啦啦啦''')
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))

# 强制类型转换
# str(12) str(198.8) str(False) 与C不同
# str类型转int类型时要注意：str是数字串可以转 str是小数串会报错
# str转int时，字符串必须是整数串
# 关于float
# 字符串中的数据如果是非数字串，则不允许转换

s1 = '191.98'
print(type(s1))
# print(type(int(s1))) 报错
print(type(float(s1))) # 可以

# 关于注释
'''这
也
是
注释，多行注释'''
# 中文编码声明注释，在文件开头加上中文声明注释，用以指定源码文件的编码格式 #coding:gbk
