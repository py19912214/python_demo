from src.zgy.business.pigKjsc import PigKjsc


class PigKjscMerchantService(PigKjsc):

    def boardTaskCollectInfo(self):
        data = {
            "period": "",
            "type": 1,
            "serviceManagerId": "",
            "deptId": ""
        }
        response = self.post('/kjsc-merchant-service/yk/workbench/v1/board-task-collect-info', data)
        print(response.text)


pigKjscMerchantService = PigKjscMerchantService()
pigKjscMerchantService.boardTaskCollectInfo()
