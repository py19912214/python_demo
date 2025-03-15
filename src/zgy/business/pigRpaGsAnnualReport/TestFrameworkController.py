from src.zgy.business.pigRpaGsAnnualReport import PigRpaGsAnnualReport


class TestFrameworkController(PigRpaGsAnnualReport):
    def deal_msg_single_task(self):
        data = {
        }
        response = self.post('/pig_rpa_gs_task_robot/nk/test/framework/v1/deal_msg_single_task?taskId=645530062556234752', data)
        print(response.text)


testFrameworkController = TestFrameworkController();
# 获取下拉框数据
testFrameworkController.deal_msg_single_task();
