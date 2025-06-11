from src.zgy.business.etaxUnified import SignalService


class InvoiceBaseService(SignalService):
    def syncBlueInvoice(self, tpTaskId):
        data = [{
            "platformTaskId": tpTaskId,
            "taskStatusCode": "SUCCESS",
            "data": '{"downloadUrl":"https://dppt.sichuan.chinatax.gov.cn:8443/v/2_25512000000076601234_2025040309352500Q4K520","invoiceDate":"2025-04-03 09:35:25","invoiceNumber":"25512000000076601234"}'
        }]
        response = self.post(
            "/invoice-cloud-platform/nk/invoice-task-callback/v1/blue-invoice-issued",
            data)
        print(response.text)

    def needFaceAuth(self, tpTaskId):
        data = {
            "tpTaskId": tpTaskId,
            "userName": "userName",
            "taxBureauQrCode": "taxBureauQrCode",
            "incomeTaxQrCode": "incomeTaxQrCode"
        }
        response = self.post(
            "/invoice-cloud-platform/nk/invoice-task-callback/v1/need-face-auth",
            data)
        print(response.text)


processService = InvoiceBaseService()
# processService.syncBlueInvoice(336669841080321)
processService.needFaceAuth(341387411832833)
