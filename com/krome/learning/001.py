# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

candidate = ['1', '2', '3', '4']
count = 0
for i in candidate:
    for j in candidate:
        for k in candidate:
            if i != j and j != k and k != i:
                count += 1
                print(f'{i}{j}{k}')
print(count)


for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != b and b != c and a != c:
                print(a, b, c)
        pass
    pass