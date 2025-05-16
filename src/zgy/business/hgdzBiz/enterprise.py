from src.zgy.business.hgdzBiz import PigYcshgAi


class EnterpriseService(PigYcshgAi):
    def selectPage(self):
        data = {

        }
        response = self.post('/ycshg-ai-platform-produce-hgdzBiz-biz/yk/enterprise/v1/select-page', data)
        print(response.text)

    def edit_enterprise(self):
        data = {
            "enterpriseId": 335073566343168,
            "enterpriseName": "py测试公司20250430_03",
            "taxNature": "SMALL_SCALE_TAXPAYER",
            "creditCode": "91511028M202504303T",
            "creditCodeStatus": "THREE_IN_ONE",
            "syncAccountInfo": 1,
        }
        response = self.post('/ycshg-ai-platform-produce-hgdzBiz-biz/yk/enterprise-detail/v1/edit-enterprise', data)
        print(response.text)

    def sync_enterprise_info(self):
        data = {
            "tenantId": 3286941137960960000,
            "enterpriseId": 332522025043003,  # tenantId+ enterpriseId 这个要唯一
            "enterpriseName": "py测试公司20250430_03",
            "creditCode": "91511028M202504303T",  # 正常三证合一是18位 但是 测试数据都是19位 并且以T结尾,每次造数据都要改下
            "customerId": 335072798457856,
            "customer": {
                "customerId": 335072798457856,
                "serviceStart": 202401,
                "serviceEnd": 202512,
            },
            "order": {
                "orderId": 789456456465465,
                "productId": 1234,
                "productName": "测试产品",
                "orderNo": "123456789",
                "operatorId": 123,
                "serviceStart": 202401,
                "serviceEnd": 202512,
                "orderType": 1
            }
        }
        response = self.post('/ycshg-ai-platform-produce-hgdzBiz-biz/feign/biz/enterprise/v1/sync-enterprise-info',
                             data)
        print(response.text)


processService = EnterpriseService()
# 查询列表
# processService.selectPage()
# 创建企业
# processService.sync_enterprise_info()
# 编辑企业
processService.edit_enterprise()
