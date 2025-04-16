from src.zgy.business.ycshgAi import PigYcshgAi


class NationalService(PigYcshgAi):

    def open(self):
        data = {
            "enterpriseId": "202504080000001",
            "taxArea": "CODE_51",
            "loginType": "UNIFIED_LOGIN",
            "identityType": "FDDBR",
            "loginAccount": "123456",
            "loginPwd": "123456",
            "agentIdentificationNo": "350304198303153310",
            "agentName": "张三",
            "agentPwd": "123456",
            "agentNumber": "123456",
            "middleNumber": "18865651234",
            "vipNumber": False,
            "whetherIsEnabled": True,
            "creatorId": "123",
            "creatorName": "123"
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/national-tax/open',
                             data)
        print(response.text)


processService = NationalService()
# 开通国税
processService.open()
