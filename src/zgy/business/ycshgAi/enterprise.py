from src.zgy.business.ycshgAi import PigYcshgAi


class EnterpriseService(PigYcshgAi):
    def selectPage(self):
        data = {

        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/enterprise/v1/select-page', data)
        print(response.text)

    def sync_enterprise_info(self):
        data = {
            "tenantId": 3211194104545280000,
            "enterpriseId": 146702504001010,  # tenantId+ enterpriseId 这个要唯一
            "enterpriseName": "py测试下单公司_10",
            "creditCode": "91511028MA65G01H10T",  # 正常三证合一是18位 但是 测试数据都是19位 并且以T结尾,每次造数据都要改下
            "productId": 1234,
            "productName": "测试产品",
            "contractStart": 202401,
            "contractEnd": 202512,
            "customerId": 789456456465465,
            "customer": {
                "customerId": 789456456465465,
                "serviceStart": 202401,
                "serviceEnd": 202512,
            },
            "order": {
                "orderId": 789456456465465,
                "operatorId": 123,
                "serviceStart": 202401,
                "serviceEnd": 202512,
                "orderType": 1
            }
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/feign/biz/enterprise/v1/sync-enterprise-info',
                             data)
        print(response.text)


processService = EnterpriseService()
# 查询列表
# processService.selectPage()
# 创建企业
processService.sync_enterprise_info()
