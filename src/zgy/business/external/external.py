from src.zgy.business.external import BaseParent


class ProcessService(BaseParent):
    def getRegisterInfo(self):
        data = {
            "enterpriseId": '2712645583831040001'
        }
        response = self.apiPost(
            "/pig-manager-erp-external/nk/external/individual-tax/v1/get-register-info?tenantId=" + str(
                2712645583831040001),
            data)
        print(response.text)

    def checkPasswordBeforeRegister(self):
        data = {
            "enterpriseId": '2712645583831040001',
            "taxArea": "AREA_CODE151",
            "loginType": "INDIVIDUAL_TAX_PASSWORD",
            "rnAccount": "13843838438",
            "rnPwd": "123456",
            "taxpayer": "123456",
            "password": "123456",
        }
        response = self.apiPost(
            "/pig-manager-erp-external/nk/external/individual-tax/v1/check-password-before-register?tenantId=" + str(
                2712645583831040001),
            data)
        print(response.text)

    def getIndividualUrl(self):
        data = {
            "userId": '2712645583831040001',
            "userName": "AREA_CODE151"
        }
        response = self.apiPost(
            "/pig-manager-erp-external/nk/external/individual-tax/v1/get-individual-url?tenantId=" + str(
                2712645583831040001),
            data)
        print(response.text)


processService = ProcessService()
# processService.getRegisterInfo()
processService.checkPasswordBeforeRegister()
# processService.getIndividualUrl()
