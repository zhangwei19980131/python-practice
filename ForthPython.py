# anthor: zhangwei time:2020/11/24
# python 一切皆对象，所有对象都有一个布尔值
# 以下对象的布尔值都是False
# False 数值0 None 空字符串 空列表 空元组 空字典 空集合
# 空列表 [] list[] 空元组 () tuple() 空字典 {} dict{} 空集合 set()
# 除了上面的 其它的布尔值均为True
# 输入一个成绩 判断
'''
score = int(input('请输入一个成绩'))
if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score < 90:
    print('B')
elif score >= 70 and score < 80:
    print('C')
elif score >= 60 and score < 70:
    print('D')
'''
# 还可以这样写

score = int(input('请输入一个成绩'))
if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 90:
    print('B')
elif 70 <= score <= 80:
    print('C')
elif 60 <= score <= 70:
    print('D')

# 嵌套if
# 使用条件表达式
num_a = int(input('请输入一个数'))
num_b = int(input('请输入一个数'))
print(str(num_a) + '大于等于' + str(num_b) if num_a >= num_b else str(num_a) + '小于' + str(num_b))

# 关于pass语句 语句什么都不做，只是一个占位符，用在语法需要语句的地方 占一个语句位置，让语法不报错

# 例如：
answer = input('你是会员么?y/n')
if answer == 'y':
    pass
else:
    pass

# 我们可以直接把对象放在if后面进行判断，因为所有对象都是由bool值的
