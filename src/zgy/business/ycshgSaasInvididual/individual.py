from src.zgy.business.ycshgSaasInvididual import PigYcshgSaasIndividualBiz


class IndividualService(PigYcshgSaasIndividualBiz):
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
processService.get_login_url()
