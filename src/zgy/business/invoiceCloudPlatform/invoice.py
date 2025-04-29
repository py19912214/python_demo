from src.zgy.business.ycshgSaasInvididual import InvoiceCloudPlatform


class InvoiceService(InvoiceCloudPlatform):
    def test(self):
        data = {
            "copyPeriod": 1,
            "declarePeriod": 2,
            "name": "91321200141850TEST"
        }
        response = self.apiPost("/invoice-cloud-platform/nk/test/v1/test1",
                                data)
        print(response.text)


processService = InvoiceService()
processService.test()
