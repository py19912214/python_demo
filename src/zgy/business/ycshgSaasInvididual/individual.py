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

    def get_company_info_from_jcsk(self):
        data = {
            "taxNo": "91510000734863892D",
            "taxAreaCode": "151",
            "loginType": "INDIVIDUAL_TAX_PASSWORD",
            "password": "123456"
        }
        response = self.apiPost(
            "/ycshg-saas-individual-tax-business/nk/external/register/v1/get_company_info_from_jcsk",
            data)
        print(response.text)

    def get_financial_data(self):
        data = {
            # 注意这里要区分字符串和数字
            "companyInfoId": "331414076342276",
            "declarePeriod": 202312,
            "userName": "潘月",
            "userId": "329774038007808"
        }
        response = self.apiPost("/ycshg-saas-individual-tax-business/nk/external/year/v1/production/get_financial_data",
                                data)
        print(response.text)


processService = IndividualService()
# processService.get_authorized()
# processService.get_login_url()
# processService.get_company_info_from_jcsk()
processService.get_financial_data()
# 365c82e571d32ab83c5be882cb9b655e02b1ac5dc4d433dead3d3ef95a1d50e2
