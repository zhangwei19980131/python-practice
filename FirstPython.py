# anthor: zhangwei time:2020/11/14

import tornado.web

message = "Hello python world!"
print(message)

# 方法title()以首字母大写的方式显示每个单词。后面小写

name = "ada lovElace"
print(name.title())

# upper() 全部大写  lower() 全部小写

print(name.upper())
print(name.lower())

# f字符串 f是format(设置格式)的简写，Python通过把花括号内的变量替换为其值来设置字符串的格式
# 还可以使用f字符串来创建消息，再把整条消息赋给变量

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name}{last_name}"
print(full_name)

# 添加制表符 \t  换行符\n

print("language:\n\tPython\n\tC\n\tJavaScript")

# Python能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白，可使用方法rstrip()

favorite_language = ' python '
favorite_language
print(favorite_language)
print(favorite_language.rstrip())

# "" 与 ‘’

print('Albert said "A person who never made a mistake never tried anything new"')

# 书写很大的数时，可使用下划线将其中的数字分组，使其清晰易读

universe_age = 14_000_000_000
print(universe_age)

# 多变量赋值

x, y, z = 0, 0, 0

print(x, y, z)

# 字母全大写来将某个变量视为常量

MAX_CONNECTIONS = 5000

# 不要企图编写完美无缺的代码，而是要编写行之有效的代码

# 列表由一系列按特定顺序排列的元素组成  []表示列表，并用,分隔其中的元素

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # 连同[]一起输出
print(bicycles[0])  # 只返回该元素，不包括[]
print(bicycles[0].title())

# python中，第一个列表元素的索引为0，这里注意 -1是访问最后一个列表元素 -2访问倒数第二个 以此类推

# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表中添加元素
# 末尾添加元素 append

motorcycles.append('ducati')
print(motorcycles)

# insert() 可在列表的任何位置添加新元素 需要指定新元素的索引和值

motorcycles.insert(0, 'ducati')
print(motorcycles)

# 使用del语句删除元素

del motorcycles[0]
print(motorcycles)

# 将数据输出文件 注意：1、指定的盘符存在 2、使用file =
# fp = open('D:/test.txt', 'a+') a+是创建文件夹  如果文件不存在就创建，存在就在文件内容后面继续追加
# print('Hello world', file=fp)
# fp.close()

# \t的使用
print('hello\tworld')
print('helloooo\tworld')
# 到底什么时候重开一个制表位，取决于你的\t之前是否占满制表位，占满重新开一个，不占满不重新开

# \r \b
print('hello\rworld')  # \r 回车 相当于光标回到行头 world 将 hello 进行了覆盖
print('hello\bworld')

print('http://www.baidu.com')
print('http:\\\\www.baidu.com')
print('我说：\'大家好\'')

# 原字符，不希望字符串中的转义字符起作用，就是用原字符，就是在字符串之前加上r或R
print(r'hello\nworld')
# 注意：最后一个不能是 \ 不然报错
#  print(r'hello\nworld\') 会报错
# 但是两个\可以
print(r'hello\nworld\\')
