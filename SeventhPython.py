# anthor: zhangwei time:2020/12/3
# 嵌套循环
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, end='\t')
    print()

# 二层循环中的break 和continue只作用于本层循环
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            continue
        print(j, end='\t')
    print()
