import datetime

from src.zgy.business.ycshgBiz import PigYcshgAi


class ProcessService(PigYcshgAi):

    def syncEnterpriseInfo(self):
        idSuffix = 1
        serNo = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        creditCode = serNo + str(idSuffix).zfill(4) + 'T'
        data = {
            "tenantId": 3286941137960960000,
            "enterpriseId": serNo + str(idSuffix).zfill(1),
            "enterpriseName": "py测试企业（" + serNo + "）",
            "creditCode": creditCode,
            "order": {
                "orderId": 1,
                "orderNo": 1,
                "serviceStart": 202501,
                "serviceEnd": 203501,
                "productId": 1,
                "productName": "商品名称",
                "refundType": 1,
                "operatorId": 1,
                "operatorName": "operatorName"
            },
            "customer": {
                "customerId": 1,
                "serviceStart": 202501,
                "serviceEnd": 203501
            }
        }
        print(data)
        response = self.post('/ycshg-ai-platform-produce-ycshg-biz/feign/biz/enterprise/v1/sync-enterprise-info',
                             data)
        print(response.text)

    def openSystem(self):
        data = {
            "enterpriseId": 338692374052864,
            "serviceType": "ALL",
            "adminName": "小潘",
            "adminPhone": "13982081834"
        }
        response = self.post('/ycshg-ai-platform-produce-ycshg-biz/yk/enterprise/v1/open-system',
                             data)
        print(response.text)

    def editEnterpriseInfo(self):
        data = {
            "enterpriseId": 338692374052864,
            "enterpriseName": "py测试企业（20250520141508）",
            "taxNature": "SMALL_SCALE_TAXPAYER",
            "creditCode": "202505201415080001T",
            "creditCodeStatus": "NOT_THREE_IN_ONE",
            "syncAccountInfo": False
        }
        response = self.post('/ycshg-ai-platform-produce-ycshg-biz/yk/enterprise-detail/v1/edit-enterprise',
                             data)
        print(response.text)


processService = ProcessService()
# 同步企业信息
# processService.syncEnterpriseInfo()
# 编辑企业信息，主要是为了存纳税人性质
# processService.editEnterpriseInfo()
# 开通数字化系统
processService.openSystem()
