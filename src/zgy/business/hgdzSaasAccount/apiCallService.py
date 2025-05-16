from src.zgy.business.hgdzSaasAccount import PigYcshgSaasAccount


class ExternalService(PigYcshgSaasAccount):
    def get_invoice_info(self):
        data = {
            "period": [202501, 202502, 202503],
            "queryType": 10,
            "accountBookId": 3314140699852800000
        }
        response = self.post(
            "/hgdzBiz-account-book-external/external/individual-fetch-count/v1/get_invoice_info",
            data)
        print(response.text)

    def select_list(self):
        data = {
            "accountBookId": '3314140699852800000',
            "source": 'HGDZ',
            "periodList": [202501]
        }
        response = self.apiPost(
            "/hgdzBiz-account-book-external/nk/external/no-ticket/v1/select-list",
            data)
        print(response.text)
    def get_login_token(self):
        data = {
            "accountBookId": '3314140699852800000',
            "source": 'HGDZ',
            "periodList": [202501]
        }
        response = self.apiPost(
            "/nk/external/login-token/v1/get-login-token",
            data)
        print(response.text)


processService = ExternalService()
# processService.get_invoice_info()
# processService.select_list()
processService.get_login_token()
