import time

# 记录开始时间
start_time = time.time()

# 程序主体部分
# 在这里写下你希望测量执行时间的代码
cnt=0
for i in range(0,1<<25):
    cnt+=1

# 记录结束时间
end_time = time.time()

# 计算执行时间
execution_time = end_time - start_time

print("程序执行时间：", execution_time, "秒")
