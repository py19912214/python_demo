from src.zgy.business.qhs import PigQhs


class IndividualCallBackService(PigQhs):

    def syncInfo(self):
        data = {
            "tpEnterpriseId": 1,
            "jsonObject": {"jcxx": [{"djzclx_mc": "个体工商户", "zgswj_mc": "主税务机关名称", "nsrzt_dm": "03"}]}
        }
        response = self.post('/qhs-platform-cronjob/nk/individual-tax/v1/sync-info',
                             data)
        print(response.text)


processService = IndividualCallBackService()
# 同步开通信息登陆失败
# processService.syncLoginError()
# 同步个税信息
processService.syncInfo()
