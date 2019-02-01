from selenium import webdriver
import time
from src.uat.common.Util import Util

#需要自己填写的参数  3个字段  以后好修改 使用也方便
summary='鸭嘴兽风险分析--------jira自动化代码编写';
needTimes='8h';
#填当前今天的 工时  默认填昨天的 0 是今天 -1 就是昨天
curTimeWorkIndex=-1;

commonUtil = Util();
options = webdriver.ChromeOptions()
options.binary_location = r"C:/Program Files (x86)/ChromeCore/ChromeCore.exe"
# options.binary_location = r"C:/Program Files (x86)/ChromeCore/ChromeCoreLauncher.exe"
chromeDriverPath=r'C:/Users/yue.pan3/AppData/Local/Programs/Python/Python37/chromedriver.exe'
url='https://jira.56qq.cn/browse/DEMO-6001'
#结果展示的url
resultUrl='https://jira.56qq.cn/secure/TimesheetWW!default.jspa'
# url='https://jira.56qq.cn/browse/LOAN-7587'
driver = webdriver.Chrome(chromeDriverPath,chrome_options =options)
driver.maximize_window();
driver.get(url)
# driver.set_window_size(1410,900)
# 设置用户名  密码  login-form-username  login-form-password  login-form-submit
username=commonUtil.getElementBycss(driver,time,"#login-form-username");
username.send_keys('');
password=commonUtil.getElementBycss(driver,time,"#login-form-password");
password.send_keys('');
submit=commonUtil.getElementBycss(driver,time,"#login-form-submit");
driver.execute_script("$('#login-form-submit').trigger('click')");
#更多按钮
opsbarOperationsMore=commonUtil.getElementBycss(driver,time,"#opsbar-operations_more");
opsbarOperationsMore.click()
#创建子任务
createSubtask=commonUtil.getElementBycss(driver,time,"#create-subtask");
createSubtask.click()
summaryElement=commonUtil.getElementBycss(driver,time,"#summary");
summaryElement.send_keys(summary)
#指派给我
assignToMeTrigger=commonUtil.getElementBycss(driver,time,"#assign-to-me-trigger");
assignToMeTrigger.click()
# 需要时间
timetrackingOriginalestimate=commonUtil.getElementBycss(driver,time,"#timetracking_originalestimate");
timetrackingOriginalestimate.send_keys(needTimes);
iconfontCalendar=commonUtil.getElementsBycss(driver,time,".aui-iconfont-calendar");
#jira时间组件选择
commonUtil.selectJiraDate(driver,iconfontCalendar,int(commonUtil.getCurDay()),int(commonUtil.getDayBySub(curTimeWorkIndex)))
# # 新建按钮 触发时间
createIssueSubmit=commonUtil.getElementBycss(driver,time,"#create-issue-submit");
createIssueSubmit.click()
time.sleep(2)
opsbarOperationsMore=commonUtil.getElementsBycss(driver,time,".issue-link");
hasSubWork=False;
for s in opsbarOperationsMore:
    if s.text==summary:
        print(s.text)
        s.click();
        hasSubWork=True;
        break;
if hasSubWork==True:
    time.sleep(2)
    startIssue=commonUtil.getElementBycss(driver,time,"#action_id_4");
    startIssue.click();
    time.sleep(2)
    closeIssue=commonUtil.getElementBycss(driver,time,"#action_id_311");
    closeIssue.click();
    issueUseTime=commonUtil.getElementBycss(driver,time,"#log-work-time-logged");
    issueUseTime.send_keys(needTimes);
    closeIssueCalendar=commonUtil.getElementsBycss(driver,time,".aui-iconfont-calendar");
    commonUtil.selectJiraCloseDate(driver,closeIssueCalendar,int(commonUtil.getCurDay()),int(commonUtil.getDayBySub(curTimeWorkIndex)))
    issueWorkflowTransitionSubmit=commonUtil.getElementBycss(driver,time,"#issue-workflow-transition-submit");
    issueWorkflowTransitionSubmit.click();
time.sleep(1)
#结束 去结果界面 看是否填写完成
driver.get(resultUrl)
