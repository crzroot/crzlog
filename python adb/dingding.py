import os,datetime,time

def dingding():
    os.system("adb shell input keyevent 26")
    time.sleep(5)
    os.system("adb shell monkey -p com.alibaba.android.rimet 1")

while True: 
    if datetime.datetime.now().hour == 18 or datetime.datetime.now().hour == 9:
        time.sleep(5)
        print("打卡时间到了，开始启动钉钉自动打开")
        #dingding()
        #time.sleep(60*60)
        time.sleep(4)
        print("test")
    else:
        print("打卡时间还没到，waiting....") 
    time.sleep(5)

