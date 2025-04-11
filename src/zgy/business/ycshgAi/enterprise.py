from src.zgy.business.ycshgAi import PigYcshgAi


class EnterpriseService(PigYcshgAi):
    def selectPage(self):
        data = {

        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/enterprise/v1/select-page',
                             data)
        print(response.text)


processService = EnterpriseService()
# 查询列表
processService.selectPage()
