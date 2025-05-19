from src.zgy.business.ycshgBiz import PigYcshgAi


class ProcessService(PigYcshgAi):

    def syncEnterpriseInfo(self):
        data = {
            "tenantId": 1,
            "enterpriseId": 2025051900001,
            "enterpriseName": "py测试企业（20250519）",
            "creditCode": "202505190000000001T",
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
        response = self.post('/ycshg-ai-platform-produce-ycshg-biz/feign/biz/enterprise/v1/sync-enterprise-info',
                             data)
        print(response.text)

    def openSystem(self):
        data = {
            "enterpriseId": 338482323226624,
            "serviceType": "ALL",
            "adminName": "小潘",
            "adminPhone": "13982081834"
        }
        response = self.post('/ycshg-ai-platform-produce-ycshg-biz/yk/enterprise/v1/open-system',
                             data)
        print(response.text)


processService = ProcessService()
# 同步企业信息
# processService.syncEnterpriseInfo()
# 开通数字化系统
processService.openSystem()
