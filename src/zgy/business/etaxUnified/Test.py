from src.zgy.business.etaxUnified import SignalService


class InvoiceBaseService(SignalService):
    def blueInvoiceIssuedRetry(self, id):
        data = {
        }
        response = self.get(
            "/invoice-cloud-platform/yk/blueInvoiceIssuedRetry?id=" + str(id),
            data)
        print(response.text)

    def invoiceCollectRetry(self, id):
        data = {
        }
        response = self.get(
            "/invoice-cloud-platform/yk/invoiceCollectRetry?id=" + str(id),
            data)
        print(response.text)

    def invoiceProjectInfoRetry(self, id):
        data = {
        }
        response = self.get(
            "/invoice-cloud-platform/yk/invoiceProjectInfoRetry?id=" + str(id),
            data)
        print(response.text)


processService = InvoiceBaseService()
# 发票开具
# processService.blueInvoiceIssuedRetry(123)
# 采集基本信息重试
processService.invoiceCollectRetry(337422296563712)
# 采集基本信息重试
# processService.invoiceProjectInfoRetry(123)
