from src.zgy.business.qhs import PigQhs


class IndividualCallBackService(PigQhs):

    def batchDeclare(self):
        data = {
            "enterpriseIds": [
                340474317979648
            ],
            "period": 202503,
            "taxType": [
                "PRODUCTION_OPERATION"
            ],
            "userId": 0,
            "userName": "阿斯东"
        }
        response = self.post('/qhs-platform-manage/yk/individual-tax-declare-detail/batch-declare',
                             data)
        print(response.text)


processService = IndividualCallBackService()
# 批量申报
processService.batchDeclare()
