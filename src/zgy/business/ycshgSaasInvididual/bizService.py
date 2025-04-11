from src.zgy.business.ycshgSaasInvididual import PigYcshgSaasIndividualBiz
from src.zgy.common import HttpUtils


class BizService(PigYcshgSaasIndividualBiz):
    def productionSendDeclare(self):
        data = {
            "companyInfoId": 331414076342276,
            "declarePeriod": 202503,
            "userId": 123213,
            "userName": "张三",
        }
        response = self.post(
            '/ycshg-saas-individual-tax-cronjob/nk/test//v1/productionSendDeclare',
            data)

        print(response.text)

    def get_authorized(self):
        data = {
            "taxAreaCode": "151",
            "password": "123456",
            "taxNo": "91321200141850TEST",
            "loginType": "INDIVIDUAL_TAX_PASSWORD"
        }
        response = self.apiPost("/ycshg-saas-individual-tax-business/nk/external/register/v1/get_authorized",
                                data)
        print(response.text)


processService = BizService()
# processService.productionSendDeclare()
processService.get_authorized()
