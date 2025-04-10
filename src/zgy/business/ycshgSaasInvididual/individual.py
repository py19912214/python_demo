from src.zgy.business.ycshgSaasInvididual import PigYcshgSaasIndividualBiz


class IndividualService(PigYcshgSaasIndividualBiz):
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
    def get_login_url(self):
        data = {
            "userId": "151",
            "userName": "123456",
            "companyId": "331638488268804",
            "natureTaxCode": "0",
            "accessMode": "COMMON",  # "GUEST"
        }
        response = self.apiPost("/ycshg-saas-individual-tax-business/nk/external/login-token/v1/get-login-url",
                                data)
        print(response.text)


processService = IndividualService()
processService.get_authorized()
processService.get_login_url()
