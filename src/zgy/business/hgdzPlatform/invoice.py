from src.zgy.business.hgdzPlatform import BaseParent

invoiceData = {
    "customerId": 789456456465465,
    "invoiceType": "QD_ZZS_ZY_FP",  # 发票类型 QD_ZZS_ZY_FP：专票，QD_ZZS_PT_FP：普票
    "buyerType": "PERSON",  # 购买方类型： PERSON：个人 ENTERPRISE：企业
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
    "includeTax": False,
    "payee": "payee",
    "remarks": "remarks",
    "reviewer": "reviewer",
    "sellerAddress": "sellerAddress",
    "sellerAddressMobile": "sellerAddressMobile",
    "sellerBankAccount": "sellerBankAccount",
    "sellerBankNo": "sellerBankNo",
    "sellerIdentificationNumber": "sellerIdentificationNumber",
    "sellerName": "sellerName",
    "itemRelInfoList": [
        {
            "businessType": "NORMAL",
            "goodsName": "冰箱1",
            "taxTypeNameShort": "taxTypeNameShort",
            "taxTypeCode": "taxTypeCode",
            "taxSysId": "taxSysId",
            "simpleTaxType": "simpleTaxType",
            "num": "1.00",
            "unitPrice": "1000",
            "spec": "spec",
            "unit": "unit",
            "rate": "0.03000000",
            "taxAmount": "30",
            "amount": "1000",
            "totalAmount": "1030"
        },
        {
            "businessType": "NORMAL",
            "goodsName": "冰箱2",
            "taxTypeNameShort": "taxTypeNameShort",
            "taxTypeCode": "taxTypeCode",
            "taxSysId": "taxSysId",
            "simpleTaxType": "simpleTaxType",
            "num": "1.00",
            "unitPrice": "1000",
            "spec": "spec",
            "unit": "unit",
            "rate": "0.03000000",
            "taxAmount": "30",
            "amount": "1000",
            "totalAmount": "1030"
        },
        {
            "businessType": "DISCOUNT",
            "goodsName": "冰箱2",
            "taxTypeNameShort": "taxTypeNameShort",
            "taxTypeCode": "taxTypeCode",
            "taxSysId": "taxSysId",
            "simpleTaxType": "simpleTaxType",
            "num": "1.00",
            "unitPrice": "103",
            "spec": "spec",
            "unit": "unit",
            "rate": "0.03000000",
            "taxAmount": "-3",
            "amount": "-100",
            "totalAmount": "-103"
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
            "customerId": 789456456465465
        }
        response = self.post(
            "/ycshg-ai-platform-produce-hgdzBiz-biz/yk/invoice-info/v1/get-seller-info",
            data)
        print(response.text)

    def syncSellerInfo(self):
        data = {
            "customerId": 789456456465465
        }
        response = self.post(
            "/ycshg-ai-platform-produce-hgdzBiz-biz/yk/invoice-info/v1/sync-seller-info",
            data)
        print(response.text)

    def syncGoodsInfo(self):
        data = {
            "customerId": 789456456465465
        }
        response = self.post(
            "/ycshg-ai-platform-produce-hgdzBiz-biz/yk/invoice-info/v1/sync-goods-info",
            data)
        print(response.text)

    def pageGoodsInfo(self):
        data = {
            "customerId": 789456456465465,
            "pageNo": 1,
            "pageSize": 100,
            # "matchGoodsName": "外星人"
        }
        response = self.post(
            "/ycshg-ai-platform-produce-hgdzBiz-biz/yk/invoice-info/v1/page-goods-info",
            data)
        print(response.text)

    def pageSyncRecord(self):
        data = {
            "customerId": 789456456465465,
            "invoiceTaskType": "INVOICE_ISSUED_BASE_INFO",
            # "invoiceTaskType": "INVOICE_PROJECT_INFO",
            # "statusList": ["SUCCESS"],  # SUCCESS, FAILED
            "pageSize": 10
        }
        response = self.post(
            "/ycshg-ai-platform-produce-hgdzBiz-biz/yk/invoice-info/v1/page-sync-record",
            data)
        print(response.text)

    def pageInvoiceInfo(self):
        data = {
            "customerId": 789456456465465,
            "pageSize": 10,
            "pageNo": 1,
            "keyword": "123123",
            "invoiceStatusList": ["NORMAL"],
            "invoiceKindList": ["BLUE"],
            "invoicingStatusList": ["PROCESS"],  # PROCESS SUCCESS
            "minTotalAmount": 1990,
            "maxTotalAmount": 2001,
            "createTimeStart": "2025-05-12 00:00:00",
            "createTimeEnd": "2025-05-20 23:59:00"
        }
        response = self.post(
            "/ycshg-ai-platform-produce-hgdzBiz-biz/yk/invoice-info/blue/v1/page-invoice-info",
            data)
        print(response.text)

    def delete(self, id):
        data = {
            "customerId": 789456456465465,
            "invoiceId": id,
        }
        response = self.post(
            "/ycshg-ai-platform-produce-hgdzBiz-biz/yk/invoice-info/blue/v1/delete",
            data)
        print(response.text)

    def applyInvoice(self):
        data = invoiceData
        response = self.post(
            "/ycshg-ai-platform-produce-hgdzBiz-biz/yk/invoice-info/blue/v1/apply-invoice",
            data)
        print(response.text)

    def queryBlueInvoice(self, invoiceId):
        data = {
            "customerId": 789456456465465,
            "invoiceId": invoiceId
        }
        response = self.post(
            "/ycshg-ai-platform-produce-hgdzBiz-biz/yk/invoice-info/blue/v1/query",
            data)
        print(response.text)

    def getBlueInvoiceSelectParam(self):
        data = {
            "customerId": 789456456465465
        }
        response = self.post(
            "/ycshg-ai-platform-produce-hgdzBiz-biz/yk/invoice-info/blue/v1/get-select-param",
            data)
        print(response.text)


processService = ProcessService()
# 基础配置
# processService.getBlueInvoiceSelectParam()

# 销售方信息
# processService.getSellerInfo()
# processService.syncSellerInfo()

# ai - 匹配商品
# processService.syncGoodsInfo()
# processService.pageGoodsInfo()

# 同步任务分页查询
# processService.pageSyncRecord()

# 发票
# processService.delete(337603169632256)
# processService.pageInvoiceInfo()
processService.applyInvoice()
# processService.queryBlueInvoice(337603633102848)

# ai相关的接口
# processService.batchMatchGoodsAi()
# processService.applyBlueInvoiceAi()
