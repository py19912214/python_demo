from src.zgy.business.ycshg import PigYcshg


class IndividualService(PigYcshg):
    def checkPasswordBeforeRegister(self):
        data = {
            "enterpriseId": 1,
            "taxArea": "AREA_CODE151",
            "loginType": "INDIVIDUAL_TAX_PASSWORD",
            "rnAccount": "13843838438",
            "rnPwd": "123456",
            "taxpayer": "123456",
            "password": "123456",
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax/check-password-before-register',
                             data)
        print(response.text)

    def register(self):
        data = {
            "enterpriseId": 1,
            "taxArea": "AREA_CODE151",
            "loginType": "INDIVIDUAL_TAX_PASSWORD",
            "rnAccount": "13843838438",
            "rnPwd": "123456",
            "taxpayer": "123456",
            "password": "123456",
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax/register',
                             data)
        print(response.text)

    def registerInfo(self):
        data = {
            "enterpriseId": 1
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax/register-info',
                             data)
        print(response.text)

    def updateRegisterInfo(self):
        data = {
            "enterpriseId": 1,
            "taxArea": "AREA_CODE151",
            "loginType": "INDIVIDUAL_TAX_PASSWORD",
            "rnAccount": "13843838438",
            "rnPwd": "123456",
            "taxpayer": "123456",
            "password": "123456",
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax/update-register-info',
                             data)
        print(response.text)

    def getIndividualUrl(self):
        data = {
            "enterpriseId": 1,
            "accessModeCode": 0,
            "whetherAdmin": False
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax/get-individual-url',
                             data)
        print(response.text)

    def updateStatus(self):
        data = {
            "enterpriseIds": [1],
            "period": 202504,
            "taxType": "COMPREHENSIVE_INCOME",
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax-declare-detail/update-status',
                             data)
        print(response.text)


processService = IndividualService()
# 注册开通前的登录密码检查
# processService.checkPasswordBeforeRegister()
# 注册
# processService.register()
# 获取注册信息
# processService.registerInfo()
# 更新注册信息
# processService.updateRegisterInfo()
# 获取个税地址
# processService.getIndividualUrl()
