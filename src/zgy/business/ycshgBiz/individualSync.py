from src.zgy.business.ycshgBiz import PigYcshgAi


class IndividualProcessService(PigYcshgAi):

    def syncPayrollInfo(self):
        data = {
            "enterpriseId": 132465,
            "payrollStatus": "WAIT_CONFIRM",  # WAIT_CONFIRM CONFIRMED
            "period": 202504,
        }
        response = self.post('/ycshg-ai-platform-produce-ycshg-biz/feign/individual-tax/v1/sync-payroll-info',
                             data)
        print(response.text)

    def syncDeclareInfo(self):
        data = {
            "enterpriseId": 132465,
            "period": 202504,
            "syncType": "CI",  # CI PO
            "declareStatus": "declareStatus",
            "declareMessage": "declareMessage",
            "payStatus": "payStatus",
            "payMessage": "payMessage",
            "taxAmount": 100
        }
        response = self.post('/ycshg-ai-platform-produce-ycshg-biz/feign/individual-tax/v1/sync-declare-info',
                             data)
        print(response.text)


processService = IndividualProcessService()
# 分页查询
processService.syncPayrollInfo()
# 申报确认
# processService.syncDeclareInfo()
# 导出
# individualProcessService.export("C:\\Users\\admin\\Desktop\\发票开具项目信息导入模板123.xlsx")
