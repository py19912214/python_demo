from src.zgy.business.qhsPlatform import PigQhs


class IndividualCallBackService(PigQhs):

    def register(self):
        data = {
            "enterpriseId": "342877538418688",
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
                "shxydm": "913301095605540607",
                "zgswj_mc": "国家税务总局成都市武侯区税务局东福大厦",
                "nsrsbh": "913301095605540607",
                "hy_mc": "其他未列明专业技术服务业",
                "cwfzryddh": "",
                "zcdlxdh": ""
            }
        }
        response = self.post('/qhs-platform-manage/yk/individual-tax/register',
                             data)
        print(response.text)


processService = IndividualCallBackService()
# 批量申报
processService.register()
