# anthor: zhangwei time:2020/11/26
# 内置函数range()
r = range(10)
print(r)
print(list(r))

r = range(1, 10)  # 不包含10
print(list(r))

r = range(1, 10, 3)
print(list(r))

print(10 in r)
print(7 in r)

# 关于range类型的优点：不管range对象表示的整数序列有多长，所有对象占用的内存空间都是相同的，只需要最多存储3个数据
# 只有当用到range对象时，才会去计算序列中的相关元素