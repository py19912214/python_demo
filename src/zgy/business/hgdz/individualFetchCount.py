from src.zgy.business.hgdz import PigYcshgAi


class IndividualFetchCountService(PigYcshgAi):
    def get_invoice_info(self):
        data = {
            "companyId": 331414076342276,
            "period": [202501, 202502],
            "queryType": 10
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-fetch-count/v1/get_invoice_info',
                             data)
        print(response.text)


processService = IndividualFetchCountService()
# 获取发票信息
processService.get_invoice_info()
