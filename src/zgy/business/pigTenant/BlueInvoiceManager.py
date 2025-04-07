from src.zgy.business.pigTenant import PigErpManagerTenantParent

invoiceData = {
    "agentCertificateCode": "",
    "agentInternationCode": "",
    "agentName": "",
    "agentTaxNo": "",
    "buyerAddress": "辽宁省大连市西岗区长江路539号",
    "buyerAddressMobile": "18884354774",
    "buyerBankAccount": "52525458546415661",
    "buyerBankNo": "成都银行",
    "buyerIdentificationNumber": "123412341234",
    "buyerName": "1.12",
    "buyerShowAddrInfo": 0,
    "buyerShowBankInfo": 0,
    "buyerType": 1,
    "downloadUrl": "",
    "includeTax": 0,
    "invoiceAmount": "5831.0700000000",
    "invoiceType": 82,
    "invoicingFailReason": "",
    "payee": "payee",
    "remarks": "remarks",
    "reviewer": "reviewer",
    "sellerAddress": "四川省成都市武侯区一环路西一段130号1栋8层823号",
    "sellerAddressMobile": "18328433002",
    "sellerBankAccount": "640718612",
    "sellerBankNo": "中国民生银行股份有限公司成都锦江支行",
    "sellerIdentificationNumber": "91110108551385082Q",
    "sellerName": "小米科技有限责任公司",
    "sellerShowAddrInfo": 0,
    "sellerShowBankInfo": 0,
    "shortfallTaxType": "02",
    "taxAmount": "168.9300000000",
    "itemRelInfoList": [
        {
            "totalAmount": "6000.00",
            "amount": "5831.07",
            "businessType": 0,
            "goodsGroupShort": "",
            "goodsId": "",
            "goodsName": "冰箱",
            "num": "1.00",
            "rate": "0.03000000",
            "rateAmount": "168.93",
            "spec": "",
            "unit": "",
            "unitPrice": "5831.07",
            "itemBalanceRelInfoList": [
                {
                    "deductAmount": "200.00",
                    "digitalTicketNumber": "55555555555555555555",
                    "invoiceCode": "",
                    "invoiceNumber": "",
                    "invoiceTime": "2025-03-18",
                    "remark": "8449",
                    "totalAmount": "6000.00",
                    "voucherNumber": "",
                    "voucherType": "01"
                }
            ],
            "goodsConfigInfo": {
                "id": "1901534707533815810",
                "creatorId": "298104431951877",
                "creatorName": "杜正伟",
                "createTime": "2025-03-17 15:22:57",
                "updaterId": "298104431951877",
                "updaterName": "杜正伟",
                "updateTime": "2025-03-17 15:22:57",
                "tenantId": "2981044317061120000",
                "goodsName": "冰箱",
                "goodsTypeId": "0",
                "taxTypeCode": "1090421020000000000",
                "taxTypeName": "家用电冰箱用配件",
                "taxTypeNameShort": "家用电器配件",
                "simpleTaxEnable": 0,
                "zeroTaxEnable": 0,
                "taxRate": "0.03000000",
                "unitPrice": "600.00000000",
                "includeTax": 0,
                "unitName": "",
                "modelName": "",
                "simpleCode": "",
                "sourceType": 1,
                "taxSysId": "",
                "taxRateString": "3%"
            },
            "taxTypeNameShort": "家用电器配件"
        }
    ],
    "paymentRelInfoList": [
        {
            "paymentMethod": "02",
            "paymentTransactionId": "12312312"
        }
    ],
    "totalAmount": "6000.0000000000"
}


class BlueInvoiceManager(PigErpManagerTenantParent):
    def getBuyerInfo(self):
        response = self.post('/pig-tenant/yk/customer/v1/page', {
            "pageNo": 1,
            "pageSize": 10,
            "search": "开发",
            "customerType": [2]
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
            "data": '{"downloadUrl":"https://dppt.sichuan.chinatax.gov.cn:8443/v/2_25512000000076601234_2025040309352500Q4K520","invoiceDate":"2025-04-03 09:35:25","invoiceNumber":"25512000000076601234"}'
        }]
        response = self.post('/pig-tenant-cronjob/nk/invoice-task-callback/v1/blue-invoice-issued', data)
        print(response.text)

    def pageGoods(self):
        data = {
            "pageNo": 1,
            "pageSize": 20
        }
        response = self.post('/pig-tenant/yk/invoice-goods-info/v1/page', data)
        print(response.text)

    def importGoodsTemplate(self, filePath):
        data = {
            'file': open(filePath, 'rb')
        }
        response = self.postFile('/pig-tenant/yk/blue/invoice-info/v1/import-goods-template', data)
        print(response.text)

    def getGoodsTemplate(self, filePath):
        response = self.get('/pig-tenant/yk/blue/invoice-info/v1/get-goods-template', {})
        with open(filePath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"文件已成功下载到 {filePath}")


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
# blueInvoiceManager.queryInvoiceDraftById(327277750190080)
# 发票开具场景，发票预览-数据转换
# blueInvoiceManager.previewInvoice()
# 申请开发票
# blueInvoiceManager.applyInvoice()
# 开票失败得发票申请，申请重新开发
# blueInvoiceManager.applyInvoiceRetry(326360560091136)
# 根据id查询数据 正式数据
# blueInvoiceManager.queryById(326561090371584)
# 基础配置 获取小规模人的优惠信息
# blueInvoiceManager.getTenantDiscount()
# 回调接口 第一个参数是tpTaskId
blueInvoiceManager.blueInvoiceIssuedCallBack(330008067457025)
# 分页查询商品
# blueInvoiceManager.pageGoods()
# 导入商品明细
# blueInvoiceManager.importGoodsTemplate("C:\\Users\\admin\\Desktop\\发票开具项目信息导入模板 (10).xlsx")
# 下载导入商品明细
# blueInvoiceManager.getGoodsTemplate("C:\\Users\\admin\\Desktop\\发票开具项目信息导入模板.xlsx")
