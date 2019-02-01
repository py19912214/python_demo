from selenium import webdriver
import time
from Util import Util
from MenuUtil import MenuUtil
commonUtil=Util();
menuUtil=MenuUtil();

driver = webdriver.Chrome()
#登陆
url='http://localhost:3001/#/onlineFeedbackShopList'
driver.get(url)
driver.set_window_size(1410,900)
commonUtil.checkIsLoading(driver, time)
hashRunList = [];
for i in range(0,menuUtil.getCycleCount()):
    menuUtil.openSubMenuNode(driver);
    commonUtil.checkIsLoading(driver, time)
    menuUtil.runSubMenuNode(driver, hashRunList);
