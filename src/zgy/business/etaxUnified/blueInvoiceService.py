from src.zgy.business.etaxUnified import SignalService

invoiceData = {
    "unifiedAuthId": 3314140699852800000,
    "tpEnterpriseId": 331414105194496,
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
    "buyerShowAddrInfo": True,
    "buyerShowBankInfo": False,
    "buyerType": "ENTERPRISE",
    "purchaserCertificateType": "purchaserCertificateType",
    "purchaserCertificateCode": "purchaserCertificateCode",
    "purchaserInternationCode": "purchaserInternationCode",
    "downloadUrl": "",
    "includeTax": True,
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
    "sellerShowAddrInfo": True,
    "sellerShowBankInfo": False,
    "taxAmount": 177,
    "amount": 5900,
    "totalAmount": 6077,
    "itemRelInfoList": [
        {
            "businessType": "NORMAL",
            "goodsName": "冰箱",
            "taxTypeNameShort": "taxTypeNameShort",
            "taxTypeCode": "taxTypeCode",
            "taxSysId": "taxSysId",
            "simpleTaxType": "simpleTaxType",
            "num": "1.00",
            "unitPrice": "6180",
            "spec": "spec",
            "unit": "unit",
            "rate": "0.03000000",
            "taxAmount": "180",
            "amount": "6000",
            "totalAmount": "6180"
        },
        {
            "businessType": "DISCOUNT",
            "goodsName": "冰箱",
            "taxTypeNameShort": "taxTypeNameShort",
            "taxTypeCode": "taxTypeCode",
            "taxSysId": "taxSysId",
            "simpleTaxType": "simpleTaxType",
            "num": "1.00",
            "unitPrice": "5831.07",
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
        }, {
            "paymentMethod": "ALIPAY",
            "paymentTransactionId": "456"
        },
    ]
}


class InvoiceBaseService(SignalService):
    def getSelectParam(self):
        data = {
        }
        response = self.post(
            "/invoice-cloud-platform/nk/invoice-info/blue/v1/get-select-param",
            data)
        print(response.text)

    def applyInvoice(self):
        data = invoiceData
        response = self.post(
            "/invoice-cloud-platform/nk/invoice-info/blue/v1/apply-invoice",
            data)
        print(response.text)

    def queryById(self, id):
        data = {
            "invoiceId": id
        }
        response = self.post(
            "/invoice-cloud-platform/nk/invoice-info/blue/v1/query",
            data)
        print(response.text)

    def submit(self):
        data = [
            {
                "callBackUrl": "http://dev-erpgateway.joolgo.cn/invoice-cloud-platform/nk/invoice-task-callback/v1/blue-invoice-issued",
                "reqData": "{\"agent\":{\"certificateNo\":\"agentCertificateCode\",\"certificateTypeCode\":\"agentCertificateType\",\"name\":\"agentName\",\"nationality\":\"agentInternationCode\",\"taxpayerCode\":\"agentTaxNo\"},\"buyerAddress\":\"buyerAddress\",\"buyerBank\":\"buyerBankNo\",\"buyerBankAccount\":\"buyerBankAccount\",\"buyerIdentificationNumber\":\"buyerIdentificationNumber\",\"buyerName\":\"buyerName\",\"buyerPhone\":\"buyerAddressMobile\",\"issuedInvoiceType\":\"01\",\"payInfos\":[{\"orderNO\":\"12312312\",\"payChannelCode\":\"10\"}],\"payee\":\"payee\",\"projectInfos\":[{\"amount\":5831.07,\"easyTaxType\":\"simpleTaxType\",\"invoiceLineNature\":0,\"price\":6000,\"projectId\":\"taxSysId\",\"projectName\":\"冰箱\",\"quantity\":1.00,\"serialNo\":1,\"slv\":0.03000000,\"specification\":\"spec\",\"taxAmount\":168.93,\"taxServiceCode\":\"taxTypeCode\",\"taxServiceForShort\":\"taxTypeNameShort\",\"unit\":\"unit\"},{\"amount\":-1,\"easyTaxType\":\"simpleTaxType\",\"invoiceLineNature\":1,\"projectId\":\"taxSysId\",\"projectName\":\"冰箱\",\"serialNo\":2,\"slv\":0.03000000,\"specification\":\"\",\"taxAmount\":-1,\"taxServiceCode\":\"taxTypeCode\",\"taxServiceForShort\":\"taxTypeNameShort\",\"unit\":\"\"}],\"remark\":\"remarks\",\"reviewer\":\"reviewer\",\"sellerAddress\":\"sellerAddress\",\"sellerBank\":\"sellerBankNo\",\"sellerBankAccount\":\"sellerBankAccount\",\"sellerIdentificationNumber\":\"sellerIdentificationNumber\",\"sellerName\":\"sellerName\",\"sellerPhone\":\"sellerAddressMobile\",\"showBuyerAddressInfo\":true,\"showBuyerBankInfo\":false,\"showSellerAddressInfo\":true,\"showSellerBankInfo\":false,\"taxInclusiveLabel\":true,\"toNaturalPerson\":false}",
                "reqId": 337292415516672,
                "taskTypeCode": "BLUE_INVOICE_ISSUED",
                "taskTypeName": "蓝字发票开具",
                "tpCompanyId": 331414105194496}
        ]

        response = self.post(
            "/pig-tax-platform/nk-anon/internal/external/invoice/v1/submit-blue-invoice-issued-task",
            data)
        print(response.text)


processService = InvoiceBaseService()
# processService.getSelectParam()
processService.applyInvoice()
# processService.submit()
# processService.queryById(336669838573568)
