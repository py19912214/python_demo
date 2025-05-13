from src.zgy.business.hgdz import PigYcshgAi


class IndividualService(PigYcshgAi):
    def checkPasswordBeforeRegister(self):
        data = {
            "enterpriseId": 332530223104000,
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
            "enterpriseId": "202504100000001",
            "taxArea": "AREA_CODE151",
            "loginType": "INDIVIDUAL_TAX_PASSWORD",
            "password": "123456",
            "rnAccount": "",
            "rnPwd": "",
            "taxpayer": {
                "djzclx_dm": "411",
                "hy_dm": "7499",
                "zcdz": "四川省成都市武侯区一环路西一段130号1栋8层823号",
                "bsryddh": "",
                "jyfw": "",
                "djzclx_mc": "内资个体",
                "dwlsgx_dm": "51",
                "xgrq": "",
                "scjydz": "四川省成都市武侯区一环路西一段130号1栋8层823号",
                "djxh": "10215101000000766331",
                "cyrs": "",
                "zgswskfj_dm": "15101072200",
                "wjcyrs": "",
                "jdxz_dm": "510107001",
                "nsrzt_dm": "03",
                "zgswj_dm": "15101070001",
                "fddbrxm": "吉小梅",
                "zzjg_dm": "",
                "nsrmc": "泸州鸣思网络技术有限公司",
                "fddbryddh": "",
                "zczb": "",
                "djrq": "2021-10-09",
                "kzztdjlx_mc": "",
                "nsrzt_mc": "正常",
                "bsrxm": "",
                "zgswskfj_mc": "国家税务总局成都市武侯区税务局玉林税务所",
                "cwfzrxm": "",
                "shxydm": "91510521MA683MPR1U",
                "zgswj_mc": "国家税务总局成都市武侯区税务局东福大厦",
                "nsrsbh": "91510521MA683MPR1U",
                "hy_mc": "其他未列明专业技术服务业",
                "cwfzryddh": "",
                "zcdlxdh": ""
            }
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax/register',
                             data)
        print(response.text)

    def getRegisterInfo(self):
        data = {
            "enterpriseId": 202504100000002
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax/register-info',
                             data)
        print(response.text)

    def updateRegisterInfo(self):
        data = {
            "enterpriseId": 202504100000002,
            "taxArea": "AREA_CODE152",
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
            "enterpriseId": 246702504001544,
            "accessModeCode": 0,
            "whetherAdmin": False
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax/get-individual-url',
                             data)
        print(response.text)

    def unnecessary(self):
        data = {
            "enterpriseId": 202504100000001
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/individual-tax/unnecessary',
                             data)
        print(response.text)


processService = IndividualService()
# 注册开通前的登录密码检查
processService.checkPasswordBeforeRegister()
# 注册
# processService.register()
# 获取注册信息
# processService.getRegisterInfo()
# 更新注册信息
# processService.updateRegisterInfo()
# 获取个税地址
# processService.getIndividualUrl()
# 标记为无需申报
# processService.unnecessary()
