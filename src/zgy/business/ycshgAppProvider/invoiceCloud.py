from src.zgy.business.ycshgAppProvider import BaseParent

invoiceData = {
    "unifiedAuthId": 3314140699852800000,
    "tpEnterpriseId": 327063837884419,
    "agentCertificateType": "agentCertificateType",
    "agentCertificateCode": "agentCertificateCode",
    "agentInternationCode": "agentInternationCode",
    "agentName": "agentName",
    "agentTaxNo": "agentTaxNo",
    "buyerAddress": "buyerAddress",
    "buyerAddressMobile": "buyerAddressMobile",
    "buyerBankAccount": "buyerBankAccount",
    "buyerBankNo": "buyerBankNo",
    "buyerIdentificationNumber": "buyerIdentificationNumber",
    "buyerName": "buyerName",
    "buyerShowAddrInfo": False,
    "buyerShowBankInfo": False,
    "buyerType": "ENTERPRISE",
    "purchaserCertificateType": "purchaserCertificateType",
    "purchaserCertificateCode": "purchaserCertificateCode",
    "purchaserInternationCode": "purchaserInternationCode",
    "downloadUrl": "",
    "includeTax": False,
    "invoiceType": "QD_ZZS_ZY_FP",
    "payee": "payee",
    "remarks": "remarks",
    "reviewer": "reviewer",
    "drawer": "drawer",
    "sellerAddress": "sellerAddress",
    "sellerAddressMobile": "sellerAddressMobile",
    "sellerBankAccount": "sellerBankAccount",
    "sellerBankNo": "sellerBankNo",
    "sellerIdentificationNumber": "sellerIdentificationNumber",
    "sellerName": "sellerName",
    "sellerShowAddrInfo": False,
    "sellerShowBankInfo": False,
    "taxAmount": "10",
    "amount": "1900",
    "totalAmount": "1910",
    "itemRelInfoList": [
        {
            "businessType": "NORMAL",
            "goodsName": "冰箱1",
            "taxTypeNameShort": "taxTypeNameShort",
            "taxTypeCode": "taxTypeCode",
            "taxSysId": "taxSysId",
            "simpleTaxType": "simpleTaxType",
            "num": "1.00",
            "unitPrice": "970",
            "spec": "spec",
            "unit": "unit",
            "rate": "0.03000000",
            "taxAmount": "30",
            "amount": "970",
            "totalAmount": "1000"
        },
        {
            "businessType": "NORMAL",
            "goodsName": "冰箱2",
            "taxTypeNameShort": "taxTypeNameShort",
            "taxTypeCode": "taxTypeCode",
            "taxSysId": "taxSysId",
            "simpleTaxType": "simpleTaxType",
            "num": "1.00",
            "unitPrice": "970",
            "spec": "spec",
            "unit": "unit",
            "rate": "0.03000000",
            "taxAmount": "30",
            "amount": "970",
            "totalAmount": "1000"
        },
        {
            "businessType": "DISCOUNT",
            "goodsName": "冰箱2",
            "taxTypeNameShort": "taxTypeNameShort",
            "taxTypeCode": "taxTypeCode",
            "taxSysId": "taxSysId",
            "simpleTaxType": "simpleTaxType",
            "num": "1.00",
            "unitPrice": "970",
            "spec": "spec",
            "unit": "unit",
            "rate": "0.03000000",
            "taxAmount": "-50",
            "amount": "-40",
            "totalAmount": "-90"
        }
    ],
    "paymentRelInfoList": [
        {
            "paymentMethod": "WECHAT_PAY",
            "paymentTransactionId": "123"
        },
        {
            "paymentMethod": "ALIPAY",
            "paymentTransactionId": "456"
        }
    ]
}


class ProcessService(BaseParent):
    def getSellerInfo(self):
        data = {
        }
        response = self.post(
            "/ycshg-ai-app-service/yk/invoice-info/v1/get-seller-info",
            data)
        print(response.text)

    def syncSellerInfo(self):
        data = {
        }
        response = self.post(
            "/ycshg-ai-app-service/yk/invoice-info/v1/sync-seller-info",
            data)
        print(response.text)

    def syncGoodsInfo(self):
        data = {
        }
        response = self.post(
            "/ycshg-ai-app-service/yk/invoice-info/v1/sync-goods-info",
            data)
        print(response.text)

    def pageGoodsInfo(self):
        data = {
            "pageNo": 1,
            "pageSize": 2,
            "matchGoodsName": "外星人"
        }
        response = self.post(
            "/ycshg-ai-app-service/yk/invoice-info/v1/page-goods-info",
            data)
        print(response.text)

    def pageSyncRecord(self):
        data = {
            # "invoiceTaskType": "INVOICE_ISSUED_BASE_INFO",
            "invoiceTaskType": "INVOICE_PROJECT_INFO",
            # "statusList": ["SUCCESS","FAILED"],
            "pageSize": 1
        }
        response = self.post(
            "/ycshg-ai-app-service/yk/invoice-info/v1/page-sync-record",
            data)
        print(response.text)

    def pageInvoiceInfo(self):
        data = {
            "pageSize": 10,
            "pageNo": 1,
            "keyword": "",
            "invoiceStatusList": [],
            "invoiceKindList": [],
            "invoicingStatusList": ["PROCESS"],
            "minTotalAmount": 1990,
            "maxTotalAmount": 2001,
            "createTimeStart": "2025-05-12 00:00:00",
            "createTimeEnd": "2025-05-20 23:59:00"
        }
        response = self.post(
            "/ycshg-ai-app-service/yk/invoice-info/blue/v1/page-invoice-info",
            data)
        print(response.text)

    def batchMatchGoods(self):
        data = {
            "goodsNameList": ["小众外星人", "大众外星人商品"]
        }
        response = self.post(
            "/ycshg-ai-app-service/yk/invoice-info/v1/batch-match-goods",
            data)
        print(response.text)

    def applyBlueInvoiceAi(self):
        data = {
            "invoiceType": "QD_ZZS_PT_FP",
            "buyerType": "PERSON",
            "buyerName": "buyerName",
            "buyerIdentificationNumber": "buyerIdentificationNumber",
            "itemRelInfoList": [
                {
                    "goodsName": "goodsName",
                    "spec": "spec",
                    "unit": "unit",
                    "num": 1,
                    "unitPrice": 2,
                    "totalAmount": 1000,
                    "rate": 0.03,
                    "goodsConfig": '{"simpleTaxType":"simpleTaxType","taxSysId":"taxSysId","taxTypeCode":"taxTypeCode","taxTypeNameShort":"taxTypeNameShort"}'
                },
                {
                    "goodsName": "goodsName1",
                    "spec": "spec1",
                    "unit": "unit1",
                    "num": 1,
                    "unitPrice": 2,
                    "totalAmount": 1000,
                    "rate": 0.13,
                    "goodsConfig": '{"simpleTaxType":"simpleTaxType","taxSysId":"taxSysId","taxTypeCode":"taxTypeCode","taxTypeNameShort":"taxTypeNameShort"}'
                }
            ],
        }
        response = self.post(
            "/ycshg-ai-app-service/yk/invoice-info/blue/v1/apply-invoice-ai",
            data)
        print(response.text)

    def applyInvoice(self):
        data = invoiceData
        response = self.post(
            "/ycshg-ai-app-service/yk/invoice-info/blue/v1/apply-invoice",
            data)
        print(response.text)

    def queryBlueInvoice(self, invoiceId):
        data = {
            "invoiceId": invoiceId
        }
        response = self.post(
            "/ycshg-ai-app-service/yk/invoice-info/blue/v1/query",
            data)
        print(response.text)

    def getBlueInvoiceSelectParam(self):
        data = {
        }
        response = self.post(
            "/ycshg-ai-app-service/yk/invoice-info/blue/v1/get-select-param",
            data)
        print(response.text)


processService = ProcessService()
# 基础配置
processService.getBlueInvoiceSelectParam()

# 销售方信息
# processService.getSellerInfo()
# processService.syncSellerInfo()

# ai - 匹配商品
# processService.syncGoodsInfo()
# processService.batchMatchGoods()
# processService.pageGoodsInfo()
# processService.pageSyncRecord()

# 发票
# processService.pageInvoiceInfo()
# processService.applyInvoice()
# processService.applyBlueInvoiceAi()
# processService.queryBlueInvoice(337425679269888)
