import os

#打开指定路径的txt文件 并加入列表 返回数据列表ipdb
def readtxt(lujin):
    iptxt = open(lujin,"r")
    ip = iptxt.readlines()
    iptxt.close()
    ipdb = []
    for temp in ip:
        n = temp.strip("\n")
        ipdb.append(n)
    return ipdb

#ping 成功返回0 不成功返回其他数字
def ipping(lujin):
    ipdbku = readtxt(lujin)
    for temp2 in ipdbku:
        print(temp2)
        m = os.system("ping %s -c 1" % temp2)
        print(m)
        #这里写 成功不为0的 写入数据库


ipping("/Users/crz/crz log/crzlog/day/1.txt")
    

