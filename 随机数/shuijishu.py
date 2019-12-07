#1到49共49个数字，随机开7个不同的数字。里面不含1、2、3、4、5任意一个数的概率是多少？2.13
import random

def gailv(qs,pl):
    i=0
    n=0
    while n < qs:
        n=n+1
        a=random.sample(range(1,49),7)
        #b=random.sample(range(1,49),5)
        b = [2,12,22,32,42]
        print(a,"分割线",b,n)
        print(len(set(a)&set(b)))
        if  len(set(a)&set(b)) != 0 :
            print("bingo")
            i = i+1
        else:
            print("pass")

    #中的
    y = i*pl*100-n*100

    print(i,n,"中的概率是",i/n*100,"%",y)
    return  y
k = []
e = 0
f = 0
while True:
    k.append(gailv(150,1.8))
    print(k)
    e = e + 1
    if e > 100:
        break
for i in k :
    if i < 0:
        f = f + 1
        print(i,f)