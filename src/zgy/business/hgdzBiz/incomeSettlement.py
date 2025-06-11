from src.zgy.business.hgdzBiz import PigYcshgAi

pageParam = {
    "year": 2024,
    # "keyword": "企业名称_01",
    # "taxNatureList": ["SMALL_SCALE_TAXPAYER", "GENERAL_TAXPAYER"],
    # "nsrStatusList": ["NORMAL", "INSPECTION"],
    # "productName": "商品名称",
    # "reportMessage": "reportMessage",
    # "declareMessage": "declareMessage",
    # "payMessage": "payMessage",
    # "serviceManagerIdList": [2],
    # "accountIdList": [202504100000002],
    # "contractStopTime": {
    #     "start": 202502,
    #     "end": 202506,
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
    # "openStatusList": ["SUCCESS", "ABNORMAL"],
    # "levyMethodList": ["REGULAR_QUOTA"],
    # "investorSubmissionClassifyList": ["PARTIAL"],
    # "reportStatusList": ["NOT_FILLED"],
    # "taxAmountClassify": "ABOVE_ONE",
    # "actualTaxAmountClassify": "ABOVE_ONE",
    # "declareStatusList": ["WAIT_DECLARE"],
    # "payStatusList": ["WAIT_PAY"],
    # "tagIds": [1, 2],
}


class IncomeSettlementProcessService(PigYcshgAi):
    def page(self):
        data = pageParam
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/business-income-settlement/v1/select-info-page',
                             data)
        print(response.text)

    def updateLevy(self):
        data = {
            "enterpriseIds": [202504100000002],
            "year": 2024,
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/business-income-settlement/v1/update-levy',
                             data)
        print(response.text)

    def fetchCount(self):
        data = {
            "enterpriseIds": [202504100000002],
            "year": 2023,
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/business-income-settlement/v1/fetch-count',
                             data)
        print(response.text)

    def batchDeclare(self):
        data = {
            "enterpriseIds": [202504100000002],
            "year": 2024,
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/business-income-settlement/v1/batch-declare',
                             data)
        print(response.text)

    def tagNoneDeclare(self):
        data = {
            "enterpriseIds": [202504100000002],
            "year": 2025,
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/business-income-settlement/v1/tag-none-declare',
                             data)
        print(response.text)

    def removeTagNoneDeclare(self):
        data = {
            "enterpriseIds": [202504100000002],
            "year": 2025,
        }
        response = self.post(
            '/ycshg-ai-platform-produce-hgdz-biz/yk/business-income-settlement/v1/remove-tag-none-declare',
            data)
        print(response.text)

    def updateStatus(self):
        data = {
            "enterpriseIds": [202504100000002],
            "year": 2024,
        }
        response = self.post(
            '/ycshg-ai-platform-produce-hgdz-biz/yk/business-income-settlement/v1/update-status',
            data)
        print(response.text)

    def export(self, filePath):
        data = pageParam
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/business-income-settlement/v1/export',
                             data)
        with open(filePath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"文件已成功下载到 {filePath}")


processService = IncomeSettlementProcessService()
# 分页查询
processService.page()
# 更新核定
# processService.updateLevy()
# 获取财务数据
# processService.fetchCount()
# 批量申报
# processService.batchDeclare()
# 标记状态为无需申报
# processService.tagNoneDeclare()
# 取消标记状态为无需申报
# processService.removeTagNoneDeclare()
# 更新状态
# processService.updateStatus()
# 导出
# processService.export("C:\\Users\\admin\\Desktop\\incomeSettlement.xlsx")
