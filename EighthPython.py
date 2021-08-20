# anthor: zhangwei time:2020/12/5
# 关于列表 和索引
# 列表里的元素可以是很多种类型
lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))  # 如果列表中有相同元素只返回列表中相同元素的第一个元素的索引
print(lst.index('hello', 1, 4))
# 切片
lst1 = [10, 20, 30, 40, 50, 60]
# start stop step
lst2 = lst1[1:6:1]  # 默认步长为1
print(lst2)
print('原列表', id(lst1))
print('新列表', id(lst2))
print(lst1[4::-1])
