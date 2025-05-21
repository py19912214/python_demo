from src.zgy.business.gateway import BaseParent


class ProcessService(BaseParent):
    def getSellerInfo(self):
        data = {
        }
        response = self.post(
            "/pig-cloud-gateway/ycshg-ai-app-service/yk/invoice-info/v1/get-seller-info",
            data)
        print(response.text)


processService = ProcessService()

# 销售方信息
processService.getSellerInfo()
