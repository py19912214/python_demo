import time
import datetime
from pandas.tseries.offsets import Day
class Util:
    def getElementBycss(self,driver,time,css):
        while True:
            try:
                return driver.find_element_by_css_selector(css)
            except:
                time.sleep(1)
                print('没有获取到节点沉睡一秒再来' + css)
    def getElementsBycss(self,driver,time,css):
        while True:
            try:
                return driver.find_elements_by_css_selector(css)
            except:
                time.sleep(1)
                print('没有获取到节点沉睡一秒再来' + css)
    def getCurDay(self):
        now_time =datetime.datetime.now()#获取当前时间
        cur_time=now_time.strftime("%Y-%m-%d")
        return cur_time.split("-")[2]
    def getDayBySub(self,num):
        now_time =datetime.datetime.now()#获取当前时间
        yes_time = (now_time+num*Day()).strftime('%Y-%m-%d')#格式化
        return yes_time.split("-")[2]
    def selectJiraDate(self,driver,iconfontCalendar,curDay,selectDay):
        #只要选择的时间 比当前大 说明跨月了
        preMonthFlag=False;
        if(curDay<selectDay):
            preMonthFlag=True;
        # 选择开始时间
        iconfontCalendar[0].click();
        time.sleep(1);
        # 昨天是上一个月
        preMonthScript="var e = document.createEvent('MouseEvents');e.initEvent('mousedown', true, true);$('.active').find('.headrow').find('td')[1].dispatchEvent(e);e.initEvent('mouseup', true, true);$('.active').find('.headrow').find('td')[1].dispatchEvent(e);";
        selectDayScript="var e = document.createEvent('MouseEvents');e.initEvent('mousedown', true, true);$('.active').find('.day-"+str(selectDay)+"')[0].dispatchEvent(e);e.initEvent('mouseup', true, true);$('.active').find('.day-"+str(selectDay)+"')[0].dispatchEvent(e);";
        print(selectDayScript)
        if preMonthFlag==True:
            driver.execute_script(preMonthScript);
            time.sleep(1);
        driver.execute_script(selectDayScript);
        time.sleep(1);
        # 选择结束时间
        iconfontCalendar[1].click();
        time.sleep(1);
        # 昨天是上一个月
        if preMonthFlag==True:
            driver.execute_script(preMonthScript);
            time.sleep(1);
        driver.execute_script(selectDayScript);
        time.sleep(1);
    def selectJiraCloseDate(self,driver,iconfontCalendar,curDay,selectDay):
        #只要选择的时间 比当前大 说明跨月了
        preMonthFlag=False;
        if(curDay<selectDay):
            preMonthFlag=True;
        # 选择开始时间
        iconfontCalendar[0].click();
        time.sleep(1);
        # 昨天是上一个月
        preMonthScript="var e = document.createEvent('MouseEvents');e.initEvent('mousedown', true, true);$('.active').find('.headrow').find('td')[1].dispatchEvent(e);e.initEvent('mouseup', true, true);$('.active').find('.headrow').find('td')[1].dispatchEvent(e);";
        selectDayScript="var e = document.createEvent('MouseEvents');e.initEvent('mousedown', true, true);$('.active').find('.day-"+str(selectDay)+"')[0].dispatchEvent(e);e.initEvent('mouseup', true, true);$('.active').find('.day-"+str(selectDay)+"')[0].dispatchEvent(e);";
        print(selectDayScript)
        if preMonthFlag==True:
            driver.execute_script(preMonthScript);
            time.sleep(1);
        driver.execute_script(selectDayScript);
        time.sleep(1);

