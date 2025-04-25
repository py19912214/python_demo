from src.zgy.business.ycshgSaasAccount import PigYcshgSaasAccount


class ExternalService(PigYcshgSaasAccount):
    def get_invoice_info(self):
        data = {
            "period": [202501, 202502, 202503],
            "queryType": 10,
            "accountBookId": 3314140699852800000
        }
        response = self.post(
            "/hgdz-account-book-external/external/individual-fetch-count/v1/get_invoice_info",
            data)
        print(response.text)


processService = ExternalService()
processService.get_invoice_info()
