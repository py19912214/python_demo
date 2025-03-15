from src.zgy.business.pigTenant import PigErpManagerTenantParent

invoiceData = {
    "invoiceType": 81,
    "buyerType": 1,
    "shortfallTaxType": "02",
    "buyerName": "总账企业科技有限公司1",
    "buyerIdentificationNumber": "913302127910351POD1",
    "buyerShowBankInfo": 0,
    "buyerBankNo": "成都银行",
    "buyerBankAccount": "123456",
    "buyerShowAddrInfo": 1,
    "buyerAddress": "购买方地址",
    "buyerAddressMobile": "13843838438",
    "sellerName": "总账企业科技有限公司",
    "sellerAddressMobile": "18328433002",
    "sellerIdentificationNumber": "913302127910351POD",
    "sellerBankNo": "中国民生银行股份有限公司成都锦江支行",
    "sellerAddress": "四川省成都市武侯区一环路西一段130号1栋8层823号",
    "sellerBankAccount": "640718612",
    "sellerShowBankInfo": 1,
    "sellerShowAddrInfo": 0,
    "purchaserCertificateCode": "",
    "purchaserInternationCode": "",
    "includeTax": 1,
    "invoiceAmount": "100",
    "taxAmount": "20",
    "totalAmount": "120",
    "itemRelInfoList": [
        {
            "totalAmount": "120",
            "amount": "100",
            "businessType": 0,
            "goodsGroupShort": "",
            "goodsId": "",
            "goodsName": "五粮液",
            "num": "2",
            "rate": "0.13000000",
            "rateAmount": "20",
            "simpleTaxType": "01",
            "spec": "123456",
            "unit": "个",
            "unitPrice": "200.00",
            "goodsConfigInfo": {
                "id": "4",
                "tenantId": "2702037874442240000",
                "goodsName": "五粮液",
                "goodsTypeId": "1113",
                "taxTypeCode": "1030300000000000000",
                "taxTypeName": "白酒",
                "taxTypeNameShort": "酒",
                "simpleTaxType": "01",
                "taxRate": "0.13000000",
                "unitPrice": "500.00000000",
                "includeTax": 1,
                "unitName": "个",
                "modelName": "123456",
                "taxSysId": "1",
                "taxRateString": "13%",
                "simpleTaxTypeName": "简易征收"
            },
            "itemBalanceRelInfoList": [{
                "totalAmount": "100",
                "deductAmount": "20",
                "voucherType": "01",
                "digitalTicketNumber": "123456",
                "invoiceTime": "2025-03-15",
            }, {
                "totalAmount": "100",
                "deductAmount": "20",
                "voucherType": "02",
                "invoiceNumber": "123",
                "invoiceCode": "456",
                "invoiceTime": "2025-03-16",
            }, {
                "totalAmount": "100",
                "deductAmount": "20",
                "voucherType": "05",
                "invoiceTime": "2025-03-17",
            }],
            "taxTypeNameShort": "酒"
        }
    ],
    "paymentRelInfoList": [
        {
            "paymentTransactionId": "001122",
            "paymentMethod": "01"
        }
    ],
    "remarks": "备注字段哦，我也不知道啥意思",
    "payee": "收款人",
    "reviewer": "复核人",
    "agentName": "经办人",
    "agentCertificateCode": "123321",
    "agentInternationCode": "156",
    "agentCertificateType": "218",
    "agentTaxNo": "1234654",
    "id": "326419985137664"
}


class BlueInvoiceManager(PigErpManagerTenantParent):
    def getBuyerInfo(self):
        response = self.post('/pig-tenant/yk/customer/v1/page', {
            "pageNo": 1,
            "pageSize": 10,
        })
        print(response.text)

    def getSelectParam(self):
        response = self.get('/pig-tenant/yk/blue/invoice-info/v1/get-select-param', {})
        print(response.text)

    def getSellerInfo(self):
        response = self.get('/pig-tenant/yk/blue/invoice-info/v1/get-seller-info', {})
        print(response.text)

    def queryInvoiceDraftById(self, id):
        response = self.get('/pig-tenant/yk/blue/invoice-info/v1/query-invoice-draft-by-id', {'id': id})
        print(response.text)

    def pageInvoiceDraft(self):
        data = {
            'buyerName': '购买方名称',
            'pageNo': 1,
            'pageSize': 5
        }
        response = self.post('/pig-tenant/yk/blue/invoice-info/v1/page-invoice-draft', data)
        print(response.text)

    def saveInvoiceDraft(self):
        data = invoiceData
        response = self.post('/pig-tenant/yk/blue/invoice-info/v1/save-invoice-draft', data)
        print(response.text)

    def previewInvoice(self):
        data = invoiceData
        response = self.post('/pig-tenant/yk/blue/invoice-info/v1/preview-invoice', data)
        print(response.text)

    def applyInvoice(self):
        data = invoiceData
        response = self.post('/pig-tenant/yk/blue/invoice-info/v1/apply-invoice', data)
        print(response.text)

    def applyInvoiceRetry(self, id):
        data = {
            "id": id
        }
        response = self.post('/pig-tenant/yk/invoice-info/v1/retry', data)
        print(response.text)

    def deleteInvoiceDraft(self, idList):
        data = {
            "idList": idList
        }
        response = self.post('/pig-tenant/yk/blue/invoice-info/v1/delete-invoice-draft', data)
        print(response.text)

    def queryById(self, id):
        data = {
            "id": id
        }
        response = self.get('/pig-tenant/yk/blue/invoice-info/v1/query-by-id', data)
        print(response.text)

    def getTenantDiscount(self):
        data = {
        }
        response = self.get('/pig-tenant/yk/blue/invoice-info/v1/get-tenant-discount', data)
        print(response.text)

    def blueInvoiceIssuedCallBack(self, tpTaskId):
        data = [{
            "platformTaskId": tpTaskId,
            "taskStatusCode": "SUCCESS",
            "data": '{"invoiceNumber":"123","invoiceDate":"2025-03-12 15:00:00","downloadUrl":"https://dppt.sichuan.chinatax.gov.cn:8443/v/2_25512000000055391015_2025031214041000Q4KCD5C"}'
        }]
        response = self.post('/pig-tenant-cronjob/nk/invoice-task-callback/v1/blue-invoice-issued', data)
        print(response.text)


blueInvoiceManager = BlueInvoiceManager()
# 获取下拉框数据
# blueInvoiceManager.getSelectParam()
# 获取客户信息
# blueInvoiceManager.getBuyerInfo()
# 获取销售方信息
# blueInvoiceManager.getSellerInfo()
# 分页查询草稿数据
# blueInvoiceManager.pageInvoiceDraft()
# 删除草稿
# blueInvoiceManager.deleteInvoiceDraft([326006035152896])
# 保存草稿数据
# blueInvoiceManager.saveInvoiceDraft()
# 根据id查询草稿数据
# blueInvoiceManager.queryInvoiceDraftById(326553966346240)
# 发票开具场景，发票预览-数据转换
# blueInvoiceManager.previewInvoice()
# 申请开发票
# blueInvoiceManager.applyInvoice()
# 开票失败得发票申请，申请重新开发
# blueInvoiceManager.applyInvoiceRetry(326360560091136)
# 根据id查询数据 正式数据
blueInvoiceManager.queryById(326561090371584)
# 基础配置 获取小规模人的优惠信息
# blueInvoiceManager.getTenantDiscount()
# 回调接口 第一个参数是tpTaskId
# blueInvoiceManager.blueInvoiceIssuedCallBack(326236316827649)
