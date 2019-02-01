from channel_manager_test import ChannelManagerTest
from Util import Util
import time
commonUtil = Util();
normalMenuObj = {
    '验证码生成':SalesManList(),
    '建议与反馈':onlineFeedbackShopTest(),
    '频道管理':CrawlingChannelTest(),
    '资讯管理':InformationManage(),
    '消息列表':MessagePushManage(),
    '分类管理':CrawlingConfigUrl()
}
needRefreshWindowMenuObj = {
    '推广渠道':ChannelManagerTest(),
    '验证码统计': SalesManStatic(),
    '广告': AdvertisementManage()
}

class MenuUtil:
    def getCycleCount(self):
        return len(needRefreshWindowMenuObj)+1;
    def openSubMenuNode(self,driver):
        time.sleep(1)
        secondClassMenuElements = commonUtil.getElementsBycss(driver,time,'.ant-menu-root>.ant-menu-submenu')
        for secondClassMenuElement in secondClassMenuElements:
            secondClassMenuElement.click();
            time.sleep(1)
    def runSubMenuNode(self,driver,hashRunList):
        oneClassMenuElements = commonUtil.getElementsBycss(driver,time,'.ant-menu-root li a')
        for oneClassMenuElement in oneClassMenuElements:
            if (hashRunList.count(oneClassMenuElement.text) > 0):
                continue;
            hashRunList.append(oneClassMenuElement.text)
            commonUtil.checkIsLoading(driver, time)
            menuObj=normalMenuObj.get(oneClassMenuElement.text);
            #正常菜单里面没有需要处理后结束
            if(menuObj==None):
                menuObj = needRefreshWindowMenuObj.get(oneClassMenuElement.text);
                if (menuObj == None):
                    continue
                else:
                    oneClassMenuElement.click();
                    menuObj.run(driver);
                    break;
            else:
                oneClassMenuElement.click();
                menuObj.run(driver);


