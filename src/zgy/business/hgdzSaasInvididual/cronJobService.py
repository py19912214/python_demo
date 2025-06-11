from src.zgy.business.hgdzSaasInvididual import PigYcshgSaasIndividualCronJob


class CronJobService(PigYcshgSaasIndividualCronJob):
    def testBatchDeclareTask(self, id):
        data = {
        }
        response = self.post(
            '/ycshg-saas-individual-tax-cronjob/nk/test/v1/batchDeclareTask?id=' + id,
            data)
        print(response.text)

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

    def getAuthorized(self):
        data = {
            "taxAreaCode": "151",
            "password": "123456",
            "taxNo": "91321200141850TEST",
            "loginType": "INDIVIDUAL_TAX_PASSWORD"
        }
        response = self.post(
            '/ycshg-saas-individual-tax-cronjob/nk/test/v1/get_authorized',
            data)

        print(response.text)


processService = CronJobService()
processService.testBatchDeclareTask('342507630821376')
# processService.productionSendDeclare()
# processService.getAuthorized()
