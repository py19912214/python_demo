from src.zgy.business.ycshgAi import PigYcshgAi


class BizQueue(PigYcshgAi):
    def groupRunningCount(self):
        data = {
            "moduleList": ["PRODUCTION_OPERATION_ANNUAL_REPORT"]
        }
        response = self.post(
            '/ycshg-ai-platform-produce-hgdz-biz/yk/queue-task/group-running-count',
            data)
        print(response.text)

    def page(self):
        data = {
            "module": "SPEEDY_PERSONAL_TAX",
            "function": "BATCH_DECLARE",
            "status": "SUCCESS",
        }
        response = self.post(
            '/ycshg-ai-platform-produce-hgdz-biz/yk/queue-task/select-page',
            data)
        print(response.text)

    def retryById(self, taskIdList):
        data = {
            "taskIdList": taskIdList
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/business/queue/v1/reportRetryById',
                             data)
        print(response.text)


processService = BizQueue()
# 批量任务队列页面查询参数
# processService.groupRunningCount()
# 分页查询批量任务队列
# processService.page()
# 根据id进行重试
processService.retryById([332379238645760])
