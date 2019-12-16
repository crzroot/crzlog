#三肖：1到49共49个数字，随机开7个数字后，再开3组4个数，7个数内包含3组数一样的概率是多少？ 赔率：12

import random
qs = 100
pl = 12
# qs == 期数（随机次数）  pl == 赔率  
def gailv(qs,pl):
    i=0
    n=0
    while n < qs:
        n=n+1
        a=random.sample(range(1,49),7)
        #b=random.sample(range(1,49),1)
        b = [2,14,26,38]
        c = [3,15,27,39]
        d = [4,16,28,40]
        print(a,"分割线",c,b,d,n)
        #对比两组是否有一样的数据 有则为1 否为0
        #print(len(set(a)&set(b)))
        if  len(set(a)&set(b)) != 0 and len(set(a)&set(c)) != 0 and len(set(a)&set(d)) != 0:
            print("bingo")
            i = i+1
        else:
            print("pass")

    #中的 y = 中的次数 * 赔率 - 期数
    y = i * pl - n
    print(i,n,"中的概率是",i/n*100,"%","结果：",y)
    return  y
 
#gailv(150,42)

gailv_list = []
g = 0
while True :
    gailv_list.append(gailv(qs,pl))
    g = g + 1
    if g == 100 :
        break

print(gailv_list)

q = 0
for x in gailv_list :
    if x > 0 :
        q = q +1
print("100次测试的赢的概率为",q,"%")




        