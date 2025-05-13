from src.zgy.business.etaxUnified import SignalService


class InvoiceBaseService(SignalService):
    def getSellerInfo(self):
        data = {
            "unifiedAuthId": 3314140699852800000
        }
        response = self.post(
            "/invoice-cloud-platform/nk/invoice-info/v1/get-seller-info",
            data)
        print(response.text)

    def syncSellerInfo(self):
        data = {
            "unifiedAuthId": 3314140699852800000,
            "tpEnterpriseId": 327063837884419,
        }
        response = self.post(
            "/invoice-cloud-platform/nk/invoice-info/v1/sync-seller-info",
            data)
        print(response.text)

    def syncGoodsInfo(self):
        data = {
            "unifiedAuthId": 3314140699852800000,
            "tpEnterpriseId": 327063837884419,
        }
        response = self.post(
            "/invoice-cloud-platform/nk/invoice-info/v1/sync-goods-info",
            data)
        print(response.text)

    def pageGoodsInfo(self):
        data = {
            "unifiedAuthId": 3314140699852800000,
            "natureTax": "SMALL",
            "matchGoodsName": "现代服1",
            "analyzerGoodsName": "现代",
            "pageSize": 1
        }
        response = self.post(
            "/invoice-cloud-platform/nk/invoice-info/v1/page-goods-info",
            data)
        print(response.text)

    def pageSyncRecord(self):
        data = {
            "unifiedAuthId": 3314140699852800000,
            # "invoiceTaskType": "INVOICE_ISSUED_BASE_INFO",
            "invoiceTaskType": "INVOICE_PROJECT_INFO",
            "statusList": [],
            "pageSize": 1
        }
        response = self.post(
            "/invoice-cloud-platform/nk/invoice-info/v1/page-sync-record",
            data)
        print(response.text)

    def pageInvoiceInfo(self):
        data = {

            "pageSize": 2,
            "pageNo": 1,
            "unifiedAuthId": 3314140699852800000,
            "keyword": "1",
            "invoiceStatusList": [],
            "invoiceKindList": [],
            "invoicingStatusList": [],
            "minTotalAmount": 0,
            "maxTotalAmount": 100000,
            "createTimeStart": "2025-05-09 00:00:00",
            "createTimeEnd": "2025-05-11 23:59:00"
        }
        response = self.post(
            "/invoice-cloud-platform/nk/invoice-info/v1/page-invoice-info",
            data)
        print(response.text)


processService = InvoiceBaseService()
# processService.getSellerInfo()
# processService.syncSellerInfo()
# processService.pageGoodsInfo()
# processService.syncGoodsInfo()
processService.pageSyncRecord()
# processService.pageInvoiceInfo()
