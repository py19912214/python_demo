from src.zgy.business.pigErpManagerTenant import PigErpManagerTenantParent

invoiceData = {
    "invoiceType": 81,
    "shortfallTaxType": 0,
    "buyerType": 0,
    "buyerName": "购买方名称123",
    "buyerIdentificationNumber": "购买方税号",
    "buyerShowBankInfo": 0,
    "buyerBankNo": "购买方银行",
    "buyerBankAccount": "购买方银行账号",
    "buyerShowAddrInfo": 0,
    "buyerAddress": "购买方地址",
    "buyerAddressMobile": "购买方电话",
    "sellerName": "销售方名称",
    "sellerAddressMobile": "销售方电话",
    "sellerIdentificationNumber": "销售方税号",
    "sellerBankNo": "销售方银行",
    "sellerAddress": "销售方地址",
    "sellerBankAccount": "销售方银行账号",
    "sellerShowBankInfo": 0,
    "sellerShowAddrInfo": 0,
    "purchaserCertificateType": 0,
    "purchaserCertificateCode": "自然人补充信息:证件号码",
    "purchaserInternationCode": "自然人补充信息:国籍编码",
    "includeTax": 1,
    "invoiceAmount": 100,
    "taxAmount": 10,
    "totalAmount": 100,
    "itemRelInfoList": [
        {
            "businessType": 0,
            "goodsName": "商品名称",
            "goodsGroupShort": "商品和服务分类简称",
            "num": "1",
            "unitPrice": "1",
            "taxTypeCode": "税收分类编码",
            "taxTypeName": "税收分类名称",
            "simpleTaxType": "商品简易分类1",
            "spec": "规格型号",
            "unit": "单位",
            "rate": 0.15,
            "amount": 10,
            "rateAmount": 10,
            "totalAmount": 10,
            "itemBalanceRelInfoList": [
                {
                    "deductAmount": "1",
                    "invoiceNumber": "发票号码",
                    "voucherNumber": "凭证号码",
                    "invoiceTime": "2025-03-05 11:00:00",
                    "remark": "备注",
                    "invoiceCode": "发票代码",
                    "totalAmount": 10,
                    "voucherType": 0,
                    "digitalTicketNumber": "数电票号码"
                }
            ]
        },
        {
            "businessType": 0,
            "goodsName": "商品名称2",
            "goodsGroupShort": "商品和服务分类简称",
            "num": "1",
            "unitPrice": "1",
            "spec": "规格型号",
            "unit": "单位",
            "taxTypeCode": "税收分类编码",
            "taxTypeName": "税收分类名称",
            "simpleTaxType": "商品简易分类2",
            "rate": 0.18,
            "amount": 10,
            "rateAmount": 10,
            "totalAmount": 10,
            "itemBalanceRelInfoList": [
                {
                    "deductAmount": "1",
                    "invoiceNumber": "发票号码",
                    "voucherNumber": "凭证号码",
                    "invoiceTime": "2025-03-05 11:00:00",
                    "remark": "备注",
                    "invoiceCode": "发票代码",
                    "totalAmount": 10,
                    "voucherType": 0,
                    "digitalTicketNumber": "数电票号码"
                }
            ]
        },
        {
            "businessType": 0,
            "goodsName": "商品名称3",
            "goodsGroupShort": "商品和服务分类简称",
            "num": "1",
            "unitPrice": "1",
            "spec": "规格型号",
            "unit": "单位",
            "taxTypeCode": "税收分类编码",
            "taxTypeName": "税收分类名称",
            "simpleTaxType": "商品简易分类3",
            "rate": 0.17,
            "amount": 10,
            "rateAmount": 10,
            "totalAmount": 10,
            "itemBalanceRelInfoList": [
                {
                    "deductAmount": "1",
                    "invoiceNumber": "发票号码",
                    "voucherNumber": "凭证号码",
                    "invoiceTime": "2025-03-05 11:00:00",
                    "remark": "备注",
                    "invoiceCode": "发票代码",
                    "totalAmount": 10,
                    "voucherType": 0,
                    "digitalTicketNumber": "数电票号码"
                }
            ]
        }
    ],
    "paymentRelInfoList": [
        {
            "paymentTransactionId": "123",
            "paymentMethod": 0
        },
        {
            "paymentTransactionId": "456",
            "paymentMethod": 2
        }
    ],
    "remarks": "备注",
    "payee": "收款人",
    "reviewer": "复核人",
    "agentName": "经办人姓名",
    "agentCertificateCode": "经办人证件号码",
    "agentInternationCode": "经办人国籍编码",
    "agentCertificateType": 0,
    "agentTaxNo": "经办人自然人纳税人识别号"
}


class BlueInvoiceManager(PigErpManagerTenantParent):
    def getSelectParam(self):
        response = self.get('/pig-tenant/yk/blue/invoice-info/v1/get-select-param', {})
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
        data["id"] = 325483168759808
        data["buyerName"] = "购买方名称123123123"
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

    def deleteInvoiceDraft(self, id):
        data = {
            "id": id
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

    def blueInvoiceIssuedCallBack(self):
        data = [{
            "platformTaskId": 325484013912073,
            "taskStatusCode": "FAILED",
            "data": ""
        }]
        response = self.post('/pig-tenant-cronjob/nk/tax-task-callback/v1/blue-invoice-issued', data)
        print(response.text)


blueInvoiceManager = BlueInvoiceManager();
# 获取下拉框数据
# blueInvoiceManager.getSelectParam();
# 分页查询草稿数据
# blueInvoiceManager.pageInvoiceDraft();
# 删除草稿
# blueInvoiceManager.deleteInvoiceDraft(325448196227072);
# 保存草稿数据
# blueInvoiceManager.saveInvoiceDraft()
# 根据id查询草稿数据
blueInvoiceManager.queryInvoiceDraftById(325483168759808);
# 发票开具场景，发票预览-数据转换
# blueInvoiceManager.previewInvoice()
# 申请开发票
# blueInvoiceManager.applyInvoice()
# 开票失败得发票申请，申请重新开发
# blueInvoiceManager.applyInvoiceRetry(325305997344768)
# 根据id查询数据 正式数据
# blueInvoiceManager.queryById(325796619223040)
# 基础配置 获取小规模人的优惠信息
# blueInvoiceManager.getTenantDiscount()
# 回调接口
# blueInvoiceManager.blueInvoiceIssuedCallBack()
