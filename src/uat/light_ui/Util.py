import string
import random
import urllib.request
import urllib.parse
import json
from selenium.webdriver.common.keys import Keys
import time

class Util:
    def randomLetters(self,startStr,length):
        s = string.ascii_letters
        for i in range(length):
            startStr = startStr + str(random.choice(s));
        return startStr
    def randomNum(self):
        return random.randint(111111111, 999999999);
    def post(self,url,params):
        # 这个是百度翻译api的地址
        # 准备一下头
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        # 将字典格式化成能用的形式
        textmod = json.dumps(params).encode(encoding='utf-8')
        # 创建一个request,放入我们的地址、数据、头
        request = urllib.request.Request(url, textmod, headers)
        # 访问
        html = urllib.request.urlopen(request).read().decode('utf-8')
        # 利用json解析包解析返回的json数据 拿到翻译结果
        print(html)
        print(json.loads(html)['code'])
    def checkIsLoading(self,driver,time):
        while True:
            try:
                driver.find_element_by_css_selector('.wal-loading')
            except:
                print('数据操作结束')
                time.sleep(1)
                break;
    def getElementBycss(self,driver,time,css):
        while True:
            try:
                driver.find_element_by_css_selector('.wal-loading')
            except:
                try:
                    return driver.find_element_by_css_selector(css)
                except:
                    time.sleep(1)
                    print('没有获取到节点沉睡一秒再来' + css)
    def getElementsBycss(self,driver,time,css):
        while True:
            try:
                driver.find_element_by_css_selector('.wal-loading')
            except:
                try:
                    return driver.find_elements_by_css_selector(css)
                except:
                    time.sleep(1)
                    print('没有获取到节点沉睡一秒再来'+css)
    def addCommentJs(self,driver):
        driver.execute_script("var new_element = document.createElement('script');new_element.setAttribute('type', 'text/javascript');new_element.setAttribute('src','http://momentjs.cn/downloads/moment.js');document.body.appendChild(new_element);")
        while True:
            try:
                driver.execute_script("moment(1530865066855);")
                print('moment.js加载完成！')
                break;
            except:
                time.sleep(1)
                print('moment.js没有加载完成，请稍后！')

    def clearInput(self, inputElement):
        inputElement.clear();
        inputElement.send_keys('1');
        inputElement.send_keys(Keys.BACK_SPACE);
    #commonUtil.setTreeSelectRandomValue(driver,time,".ant-form-horizontal .ant-select",0)
    def setTreeSelectRandomValue(self, driver,time,css,index):
        #展开tree列表 树型结构的话 相同的值第二次点击就是取消所以要保证第二次点击不能跟第一次一样
        selectComList = self.getElementsBycss(driver, time, css);
        if (len(selectComList) > 0):
            selectComList[index].click();
            #判断列表中的值有多少然后随机选中一个
            while True:
                allCloseButtonList=self.getElementsBycss(driver, time, ".ant-select-tree .ant-select-tree-switcher_close");
                if (len(allCloseButtonList) > 0):
                    for allCloseButton in allCloseButtonList:
                        try:
                            allCloseButton.click();
                        except:
                            continue;

                else:
                    break;
                time.sleep(1)
            allSelectList=self.getElementsBycss(driver, time, ".ant-select-tree .ant-select-tree-node-content-wrapper");
            if (len(allSelectList) > 0):
                time.sleep(1);
                while True:
                    tempSelectLi=allSelectList[random.randint(0, len(allSelectList)-1)];
                    try:
                        oldValue = selectComList[index].find_element_by_css_selector(
                            ".ant-select-selection-selected-value");
                        if (tempSelectLi.text != oldValue.text):
                            try:
                                tempSelectLi.click();
                                break;
                            except:
                                continue;
                    except:
                        tempSelectLi.click();
                        break;

    #commonUtil.setTreeSelectRandomValue(driver,time,".form_search .ant-select",0)
    def setNormalSelectRandomValue(self, driver,time,css,index):
        #展开tree列表
        selectComList=self.getElementsBycss(driver, time,css);
        if(len(selectComList)>0):
            selectComList[index].click();
            #判断列表中的值有多少然后随机选中一个
            dropdownSelectElement = self.getElementsBycss(driver, time, ".ant-select-dropdown")[index];
            allSelectList = self.getElementsBycss(dropdownSelectElement, time, "li");
            time.sleep(1);
            while True:
                try:
                    if (len(allSelectList) > 0):
                        allSelectList[random.randint(0, len(allSelectList)-1)].click();
                        time.sleep(1);
                        break;
                except:
                    if (len(allSelectList) > 0):
                        allSelectList[0].click();
                    print("数组越界就重新选择时间");
    def createIntRandom(self,start,end):
        return str(random.randint(start, end));
    #设置时间的值
    def setDatePickValue(self,driver,time,css,index,selectTodayFlag=False,start=0,end=-1):
        pickComList = self.getElementsBycss(driver, time, css);
        if (len(pickComList) > 0):
            pickComList[index].click();
            if(selectTodayFlag):
                self.getElementBycss(driver, time, ".ant-calendar-today-btn").click();
            else:
                allDaySelectList=self.getElementsBycss(driver, time, ".ant-calendar-tbody td[class='ant-calendar-cell']");
                time.sleep(1);
                if (len(allDaySelectList) > 0):
                    if (end == -1):
                        end = len(allDaySelectList) - 1;
                    allDaySelectList[random.randint(start, end)].click();

    def setDatePickRangeValue(self,driver,time,css,index,start=0,end=0,intervalRangeDay=0,intervalDay=0):
        pickComList = self.getElementsBycss(driver, time, css);
        if (len(pickComList) > 0):
            pickComList[index].click();
            allDaySelectList=self.getElementsBycss(driver, time, ".ant-calendar-tbody td[class='ant-calendar-cell']");
            if (len(allDaySelectList) > 0):
                if(end==0):
                    end=len(allDaySelectList)-1;
                while True:
                    try:
                        time.sleep(1);
                        startDataIndex = random.randint(start, end);
                        allDaySelectList[startDataIndex].click();
                        #传入了明确的间隔天数的话 就直接改值
                        if(intervalDay>0):
                            allDaySelectList[startDataIndex+intervalDay].click();
                        else:
                            if(intervalRangeDay>0):
                                end = startDataIndex + intervalDay;
                            allDaySelectList[random.randint(startDataIndex, end)].click();
                        break;
                    except:
                        allDaySelectList[startDataIndex].click();
                        print("数组越界就重新选择时间");




