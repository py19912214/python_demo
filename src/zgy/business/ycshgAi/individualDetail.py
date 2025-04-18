from src.zgy.business.ycshgAi import PigYcshgAi

pageParam = {
    "period": 202503,
    "declareType": "COMPREHENSIVE_INCOME",
    # "declareType": "PRODUCTION_OPERATION",
    # "keyword": "企业名称_01",
    # "taxNatureList": ["SMALL_SCALE_TAXPAYER", "GENERAL_TAXPAYER"],
    # "nsrStatusList": ["NORMAL", "INSPECTION"],
    # "salaryConfirmWayList": ["ACCRUAL_LAST_ISSUED_LAST", "ACCRUAL_NOW_ISSUED_LAST"],
    # "productName": "商品名称",
    # "reportMessage": "商品名称",
    # "declareMessage": "商品名称",
    # "payMessage": "商品名称",
    # "serviceManagerId": [2],
    # "accountIdList": [202504100000002],
    # "contractStopTime": {
    #     "start": 202502,
    #     "end": 202506,
    #     "symbol": "range",
    # },
    # "submissionTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "payrollTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "reportTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "declareTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "payTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "submissionStatusList": ["SUBMIT_SUCCESS", "WAIT_SUBMIT"],
    # "payrollStatusList": ["TASK_ING", "COMPLETED", "NO_UPLOAD"],
    # "reportStatusList": ["NOT_FILLED", "TO_BE_IMPROVED", "FILLED"],
    # # "hasSalaryIncomeFacieList": [False, True],
    # "taxAmountClassify": "BELOW_EQUAL_ONE",
    # "actualTaxAmountClassify": "BELOW_EQUAL_ONE",
    # "declareStatusList": ["WAIT_DECLARE"],
    # "payStatusList": ["WAIT_PAY"],
    # "investorSubmissionClassifyList": ["NONE"],
    # "levyMethodList": ["REGULAR_QUOTA"],
    # "taxIdentificationList": ["OTHERS_INCOME_RATIO"],
    # "taxDeadlineList": ["MONTHLY"],
    # "tagIds": [1, 2],
}


class IndividualDetailService(PigYcshgAi):
    def page(self):
        data = pageParam
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax-declare-detail/select-info-page',
                             data)
        print(response.text)

    def export(self, filePath):
        data = pageParam
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax-declare-detail/export',
                             data)
        with open(filePath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"文件已成功下载到 {filePath}")

    def updateStatus(self):
        data = {
            "enterpriseIds": [202504100000002],
            "period": 202503,
            # "taxType": "PRODUCTION_OPERATION",
            "taxType": "COMPREHENSIVE_INCOME",
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax-declare-detail/update-status',
                             data)
        print(response.text)

    def batchDeclare(self):
        data = {
            "enterpriseIds": [202504100000002],
            "period": 202503,
            # "taxType": "PRODUCTION_OPERATION",
            "taxType": "COMPREHENSIVE_INCOME",
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax-declare-detail/batch-declare',
                             data)
        print(response.text)

    def tagNoneDeclare(self):
        data = {
            "enterpriseIds": [202504100000002],
            "period": 202503,
            # "taxType": "PRODUCTION_OPERATION",
            "taxType": "COMPREHENSIVE_INCOME",
            "syncSalary": True
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax-declare-detail/tag-none-declare',
                             data)
        print(response.text)

    def removeTagNoneDeclare(self):
        data = {
            "enterpriseIds": [202504100000002],
            "period": 202503,
            # "taxType": "PRODUCTION_OPERATION",
            "taxType": "COMPREHENSIVE_INCOME",
            "syncSalary": True
        }
        response = self.post(
            '/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax-declare-detail/remove-tag-none-declare',
            data)
        print(response.text)

    def updateLevyTask(self):
        data = {
            "enterpriseIds": [202504100000002],
            "period": 202504
        }
        response = self.post(
            '/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax-declare-detail/update-levy-task',
            data)
        print(response.text)


processService = IndividualDetailService()
# 分页查询
processService.page()
# 申报确认
# processService.declareConfirm()
# 导出
# processService.export("C:\\Users\\admin\\Desktop\\个税导出1.xlsx")
# 同步状态
# processService.updateStatus()
# 批量申报
# processService.batchDeclare()
# 标记状态为无需申报
# processService.tagNoneDeclare()
# 取消标记状态为无需申报
# processService.removeTagNoneDeclare()
# 更新核定
# processService.updateLevyTask()
