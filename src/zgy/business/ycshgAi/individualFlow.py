from src.zgy.business.ycshgAi import PigYcshgAi
from src.zgy.business.ycshgAi.bizQueue import BizQueue
from src.zgy.business.ycshgAi.individualCallBack import IndividualCallBackService
from src.zgy.business.ycshgAi.individualDetail import IndividualDetailService


class IndividualFlowService(PigYcshgAi):

    def normal(self):
        detailService = IndividualDetailService()
        callbackService = IndividualCallBackService()
        bizQueue = BizQueue()
        # 个税申报
        # detailService.batchDeclare()
        # 定时任务应该跑的数据
        # bizQueue.retryById([1])
        # callbackService.syncSubmissionStatus()
        # callbackService.syncReportInfo()
        # callbackService.syncDeclareStatus()


processService = IndividualFlowService()
# 正常流程
processService.normal()
