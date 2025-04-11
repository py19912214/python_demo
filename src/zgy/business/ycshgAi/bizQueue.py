from src.zgy.business.ycshgAi import PigYcshgAi


class BizQueue(PigYcshgAi):
    def getBusinessTaskQueueParam(self):
        data = {}
        response = self.post(
            '/ycshg-ai-platform-produce-hgdz-biz/yk/business-task-queue/v1/get-business-task-queue-param',
            data)
        print(response.text)

    def selectPageBusinessTaskQueue(self):
        data = {
            "taskModule": "SPEEDY_PERSONAL_TAX",
            "taskFunction": "UPDATE_LEVY",
            "taskStatus": "RUNNING",
        }
        response = self.post(
            '/ycshg-ai-platform-produce-hgdz-biz/yk/business-task-queue/v1/select-page-business-task-queue',
            data)
        print(response.text)

    def retryById(self, taskIdList):
        data = {
            "taskIdList": taskIdList
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/business/queue/v1/retryById',
                             data)
        print(response.text)


processService = BizQueue()
# 批量任务队列页面查询参数
# processService.getBusinessTaskQueueParam()
# 分页查询批量任务队列
# processService.selectPageBusinessTaskQueue()
# 根据id进行重试
processService.retryById([331598872772608])
