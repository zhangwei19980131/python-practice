# anthor: zhangwei time:2020/11/28
# 关于while
# 4步循环法
'''
    1、初始化变量
    2、条件判断
    3、条件执行体
    4、改变变量

'''
sum = 0
a = 0
while a < 101:
    sum += a
    a += 2
print(sum)

# for in 循环

for a in 'Python':
    print(a)

for i in range(10):
    print(i)

for _ in range(5):
    print('啦啦啦')

print('使用for输出100到999的水仙花数')
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            i = a * 100 + b * 10 + c
            if i == a * a * a + b * b * b + c * c * c:
                print('水仙花数为\n', i)

# 另一种方法
for i in range(100, 999):
    gewei = i % 10
    shiwei = i // 10 % 10
    baiwei = i // 100
    if gewei ** 3 + shiwei ** 3 + baiwei ** 3 == i:
        print(i)

# continue 结束当前循环 break 跳出循环
# 使用continue打印输出1-50之间5的倍数

for i in range(1, 51):
    if i % 5 != 0:
        continue
    print(i)

# 关于else
for i in range(3):
    pwd = input('请输入密码')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误，请重新输入')

else:
    print('对不起，3次都错误')
