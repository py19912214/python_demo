from src.zgy.business.ycshgBiz import PigYcshgAi


class IndividualProcessService(PigYcshgAi):

    def syncPayrollInfo(self):
        data = {
            "enterpriseId": 1,
            "payrollStatus": "CONFIRMED",  # WAIT_CONFIRM CONFIRMED
            "period": 202504,
        }
        response = self.post('/ycshg-ai-platform-produce-ycshg-biz/feign/individual-tax/v1/sync-payroll-info',
                             data)
        print(response.text)

    def syncDeclareInfo(self):
        data = {
            "enterpriseId": 1,
            "period": 202504,
            "syncType": "PO",  # CI PO
            "declareStatus": "ON_DECLARE",
            "declareMessage": "declareMessage",
            "payStatus": "WAIT_PAY",
            "payMessage": "payMessage",
            "taxAmount": 101
        }
        response = self.post('/ycshg-ai-platform-produce-ycshg-biz/feign/individual-tax/v1/sync-declare-info',
                             data)
        print(response.text)
    def syncFaceInfo(self):
        data = {
            "enterpriseId": 1,
            "hasProduction": True,
            "productionFaceTime": "2025-05-14 18:01:02"
        }
        response = self.post('/ycshg-ai-platform-produce-ycshg-biz/feign/individual-tax/v1/sync-face-info',
                             data)
        print(response.text)


processService = IndividualProcessService()
# 分页查询
# processService.syncPayrollInfo()
# 申报确认
processService.syncDeclareInfo()
# 导出
# processService.syncFaceInfo()
