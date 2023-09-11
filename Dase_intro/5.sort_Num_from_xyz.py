d={'x':0,'y':0,'z':0}
print("x:")
d['x']=int(input())
print("y:")
d['y']=int(input())
print("z:")
d['z']=int(input())

# 按照值对字典进行排序，返回一个由元组组成的列表
sorted_items = sorted(d.items(), key=lambda x: x[1])

# 输出排序后的结果
print("\nAfter sorted:\n")
for item in sorted_items:
    print(f'{item[0]}: {item[1]}')
