from src.zgy.business.hgdzBiz import PigYcshgAi

pageParam = {
    "period": 202503,
    # "keyword": "企业名称_01",
    # "taxNature": ["SMALL_SCALE_TAXPAYER", "GENERAL_TAXPAYER"],
    # "salaryConfirmWay": ["ACCRUAL_LAST_ISSUED_LAST", "ACCRUAL_NOW_ISSUED_LAST"],
    # "productName": "商品名称",
    # "serviceManagerIdList": [2],
    # "accountIdList": [1],
    # "contractStopTime": {
    #     "start": 202502,
    #     "end": 202506,
    #     "symbol": "range",
    # },
    # "openTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "payrollTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "ciFacieTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "ciDeclareTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "ciPayTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "poFacieTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "poDeclareTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "poPayTime": {
    #     "start": "2025-04-01",
    #     "end": "2025-04-02",
    #     "symbol": "range",
    # },
    # "openStatusList": ["SUCCESS"],
    # "payrollStatusList": ["TASK_ING", "COMPLETED", "NO_UPLOAD"],
    # "hasCiFacieList": ['null'],
    # "ciTaxAmount": "BELOW_EQUAL_ONE",
    # "ciDeclareStatusList": ["WAIT_DECLARE"],
    # "ciPayStatusList": ["WAIT_PAY"],
    # "hasPoFacieList": [True, False],
    # "poTaxAmount": "ABOVE_ONE",
    # "poDeclareStatusList": ["WAIT_DECLARE"],
    # "poPayStatusList": ["WAIT_PAY"],
    # "tagIds": [1, 2],
}


class IndividualProcessService(PigYcshgAi):
    def page(self):
        data = pageParam
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax-declare-process/select-info-page',
                             data)
        print(response.text)

    def declareConfirm(self):
        data = {
            "enterpriseId": 202504100000002,
            "period": 202503,
            "comprehensiveIncome": {
                "taxAmount": 0,
                "declareStatus": "EXTERNAL_DECLARED",
                "payStatus": "NEED_NOT_PAY",
                "declareScreenshotList": [
                    "https://testrepos.joolgo.com/qhs/tenant/IvNV9ZUBcX1jd6l2NcyM/1.png?Expires=3891061405&OSSAccessKeyId=LTAI4GJnP2MpHxgSNmNKQZFP&Signature=QqY5vADmq3tHNF81tK0jY5U0vQg%3D"
                ],
                "payScreenshotList": [
                    "https://testrepos.joolgo.com/qhs/tenant/I_NV9ZUBcX1jd6l2RMyK/1.png?Expires=3891061409&OSSAccessKeyId=LTAI4GJnP2MpHxgSNmNKQZFP&Signature=A%2FPc29vkbUKbEkRUTONgDyaVPPk%3D"
                ]
            },
            "productionOperation": {
                "taxAmount": 1,
                "declareStatus": "NONE_DECLARE",
                "payStatus": "PAY_SUCCESS",
                "declareScreenshotList": [
                    "https://testrepos.joolgo.com/qhs/tenant/IvNV9ZUBcX1jd6l2NcyM/1.png?Expires=3891061405&OSSAccessKeyId=LTAI4GJnP2MpHxgSNmNKQZFP&Signature=QqY5vADmq3tHNF81tK0jY5U0vQg%3D"
                ],
                "payScreenshotList": [
                    "https://testrepos.joolgo.com/qhs/tenant/I_NV9ZUBcX1jd6l2RMyK/1.png?Expires=3891061409&OSSAccessKeyId=LTAI4GJnP2MpHxgSNmNKQZFP&Signature=A%2FPc29vkbUKbEkRUTONgDyaVPPk%3D"
                ]
            },
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax-declare-process/declare-confirm',
                             data)
        print(response.text)

    def export(self, filePath):
        data = pageParam
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax-declare-process/export',
                             data)
        with open(filePath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"文件已成功下载到 {filePath}")


individualProcessService = IndividualProcessService()
# 分页查询
# individualProcessService.page()
# 申报确认
individualProcessService.declareConfirm()
# 导出
# individualProcessService.export("C:\\Users\\admin\\Desktop\\发票开具项目信息导入模板123.xlsx")
