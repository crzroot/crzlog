#1到49共49个数字，随机开7个不同的数字。里面不含1、2、3、4、5任意一个数的概率是多少？2.13
import random

def gailv():
    i=0
    n=0
    while n < 150:
        n=n+1
        a=random.sample(range(1,49),7)
        b=random.sample(range(1,49),6)
        print(a,"分割线",b,n)
        # a1 = b[0]
        # a2 = b[1]
        # a3 = b[2]
        # a4 = b[3]
        # a5 = b[4]
        a1 = 1
        a2 = 2
        a3 = 3
        a4 = 4
        a5 = 5
        a6 = 6

        if a[0] == a1 or a[1] == a1 or a[2] == a1 or a[3] == a1 or a[4] == a1 or a[5] == a1 or a[6]== a1 or a[0] == a2 or a[1] == a2 or a[2] == a2 or a[3] == a2 or a[4] == a2 or a[5] == a2 or a[6] == a2 or a[0] == a3 or a[1] == a3 or a[2] == a3 or a[3] == a3 or a[4] == a3 or a[5] == a3 or a[6] == a3 or a[0] == a4 or a[1] == a4 or a[2] == a4 or a[3] == a4 or a[4] == a4 or a[5] == a4 or a[6] == a4 or a[0] == a5 or a[1] == a5 or a[2] == a5 or a[3] == a5 or a[4] == a5 or a[5] == a5 or a[6] == a5 or a[0] == a6 or a[1] == a6 or a[2] == a6 or a[3] == a6 or a[4] == a6 or a[5] == a6 or a[6] == a6:

            print("bingo")
            i = i+1
        else:
            print("pass")

    y = (100*n-100*i)*2.5-100*n
    print(i,n,"中的概率是",i/n*100,"%",y)

gailv()




