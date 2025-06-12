from src.zgy.business.hgdzPlatform import BaseParent


class ProcessService(BaseParent):
    def finish(self, id):
        data = {
            "id": id
        }
        response = self.post(
            "/ycshg-ai-service-provider/yk/production/order/task/v1/finish",
            data)
        print(response.text)


processService = ProcessService()
ids = [342827961974797,342827961974810,342827961974823,342827961974835,342827961974836,342827961974848,342827961974861,342827961974874,342827961974880]
for id in ids:
    processService.finish(id)
