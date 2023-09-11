S=input()
if(S==""):
    print("No input!")
pre=S[0]
next=S[0]
flag=0
cnt=0
d={}
for i in range(0,len(S)):
    flag+=1
    if(flag<len(S)):
        next=S[flag]
        if(pre==next):
            if(pre in d):
                d[pre]+=1
            else:
                d[pre]=2
            pre=next
            continue
        else:
            pre=next
            continue
    else:
        if not bool(d):
            print("No")
        else:
            # 打印字典中所有键和对应的值
            print("Yes")
            for key, value in d.items():
                print(f"char: {key}，cnt: {value}")