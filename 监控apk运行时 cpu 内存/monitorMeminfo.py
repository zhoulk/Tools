# /usr/bin/python
# encoding:utf-8
import csv
import os
import time

# 监控内存资源信息
class MonitoringMeminfoResources(object):
    def __init__(self, count):
        self.counter = count
        self.alldata = [("timestamp", "com.lutongnet.ott.mxly","com.lutongnet.ott.mxly:PluginP01","com.lutongnet.ott.mxly:PluginP02")]
    # 单次执行监控过程
    def monitoring(self):
        result1 = os.popen("adb shell dumpsys meminfo | findstr com.lutongnet.ott.mxly.(")
        result2 = os.popen("adb shell dumpsys meminfo | findstr com.lutongnet.ott.mxly:PluginP01")
        result3 = os.popen("adb shell dumpsys meminfo | findstr com.lutongnet.ott.mxly:PluginP02")
        mxly1 =[]
        mxly2 =[]
        mxly3 =[]
        s1 = result1.readlines()
        a1 = [x.strip() for x in s1 if x.strip() != '']
        s2 = result2.readlines()
        a2 = [x.strip() for x in s2 if x.strip() != '']
        s3 = result3.readlines()
        a3 = [x.strip() for x in s3 if x.strip() != '']
        for x1 in a1:
            if x1 not in mxly1:
                mxly1.append(x1)
        if mxly1 != []:
            mxly_1 = mxly1[0][0:mxly1[0].rfind('kB', 1) + 2]
        else:
            mxly_1 = 0
        for x2 in a2:
            if x2 not in mxly2:
                mxly2.append(x2)
        if mxly2 != []:
            mxly_2 = mxly2[0][0:mxly2[0].rfind('kB', 1) + 2]
        else:
            mxly_2 = 0
        for x3 in a3:
            if x3 not in mxly3:
                mxly3.append(x3)
        if mxly3 !=[]:
            mxly_3 = mxly3[0][0:mxly3[0].rfind('kB', 1) + 2]
        else:
            mxly_3 =0
        currenttime = self.getCurrentTime()
        print("current time is:"+currenttime)
        print(mxly_1+" | "+mxly_2+" | "+mxly_3)
        self.alldata.append([currenttime, mxly_1,mxly_2,mxly_3])
    # 多次执行监控过程
    def run(self):
        while self.counter > 0:
            self.monitoring()
            self.counter = self.counter - 1
            #每次执行间隔时间
            time.sleep(3)
    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        return currentTime
    # 数据的存储
    def SaveDataToCSV(self):
        csvfile = open('meminfo.csv', 'w',encoding='utf8',newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()
if __name__ == "__main__":
    # 监控次数300
    monitoringMEMResources = MonitoringMeminfoResources(30)
    monitoringMEMResources.run()
    monitoringMEMResources.SaveDataToCSV()