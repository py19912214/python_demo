from src.zgy.business.qhsPlatform import PigQhs


class IndividualCallBackService(PigQhs):

    def createEnterprise(self):
        data = {
            "tenantId": "3109336583045120000",
            "creditCode": "913100002025061210T",
            "enterpriseName": "小潘测试（2025061210）",
            "juridicalPerson": "小潘"
        }
        response = self.post('/qhs-platform-web/yk/enterprise-login/v1/create-enterprise',
                             data)
        print(response.text)

    def buyPackage(self):
        data = {
            "packageType": 1,  # 1:新增 2:续费
            "enterpriseId": 342877538418688,  # 会被请求头的参数 x-tenant-enterprise-id 替换掉
            "packageId": 304654982774784,  # 先用这个 配置在 qhs_agency_bookkeeping_product_detail 表
            "specification": "THREE_YEARS",  # ONE_MONTH ONE_YEAR TWO_YEARS THREE_YEARS PERMANENT
            "serviceStartTime": 202504,
            "serviceStopTime": 209912,
            "amount": 2484.00  # 金额必须要跟配置的保持一致
        }
        # 会被请求头的参数 x-tenant-enterprise-id 替换掉
        self.setTenantEnterpriseId('342877538418688');
        response = self.post('/qhs-platform-applet/yk/applet/my-interface/v1/buy-package',
                             data)
        print(response.text)

    def offlinePayment(self):
        data = {
            "paymentId": 1933088693337489409,  # qhs_order_payment表id
            "paymentMethod": 2,  # 1线上 2线下
            "actualAmount": 2484.0,
            "paymentTime": "2025-06-12 12:00:00",
            "paymentChannel": "OTHER",  # "WECHAT","ALIPAY","BANK_CARD","CASH","OTHER"
            "remark": "备注",
            "wechatOrderNo": "asdasdasd123546"
        }
        # 会被请求头的参数 x-tenant-enterprise-id 替换掉
        self.setTenantEnterpriseId('342877538418688');
        response = self.post('/qhs-platform-manage/yk/order/payment/v1/offline-payment',
                             data)
        print(response.text)

    def openNational(self):
        data = {
            "enterpriseId": 342877538418688,
            "taxArea": "CODE_51",
            "loginType": "AGENCY_LOGIN",
            "identityType": "FDDBR",
            "loginPwd": "123456",
            "agentName": "123456",
            "todoId": 0
        }
        # 会被请求头的参数 x-tenant-enterprise-id 替换掉
        self.setTenantEnterpriseId('342877538418688');
        response = self.post('/qhs-platform-applet/yk/national-tax/open',
                             data)
        print(response.text)

    def importOldAccount(self):
        data = {
        }
        # 会被请求头的参数 x-tenant-enterprise-id 替换掉
        self.setTenantEnterpriseId('342877538418688');
        # select id from qhs_enterprise_to_do where enterprise_id=@enterpriseId and to_do_code='MA1003'
        todoId = '1933091899455086593'
        response = self.post(
            '/qhs-platform-applet/yk/applet/to-do-handling/v1/import-old-account?id=' + todoId + '&fileIds=',
            data)
        print(response.text)

    def createAccountAudit(self):
        data = {
            # select id from qhs_enterprise_create_account_audit where enterprise_id=@enterpriseId
            "id": 342885631459328,
            "auditStatus": "AUDITED",
            "auditMessage": "ok",
            "dealType": "PRODUCT_REFUND",
            "amount": 0.0,
            "settlementAmount": 0.0,
            "accountBookDealStatus": 0,
            "accountBookTaxNature": "SMALL",
            "accountBookName": "123465",
            "startPeriod": 202504,
            "accountBookCurrency": "rmb",
            "accountBookSystem": "SMALL_BUSINESS_ACCOUNT_SYSTEM",
            "accountIndustryCategory": "AGRICULTURE",
            "accountTrade": "SM_TYX",
            "autoSettingNationalStatus": True,
            "autoSettingAccountStatus": True
        }
        # 会被请求头的参数 x-tenant-enterprise-id 替换掉
        self.setTenantEnterpriseId('342877538418688');
        # select id from qhs_enterprise_to_do where enterprise_id=@enterpriseId and to_do_code='MA1003'
        todoId = '1933091899455086593'
        response = self.post(
            '/qhs-platform-manage/yk/enterprise-create-account-audit/v1/create-account-audit',
            data)
        print(response.text)



    def individualOpen(self):
        data = {
            "enterpriseId": "342877538418688",
            "taxArea": "AREA_CODE151",
            "loginType": "INDIVIDUAL_TAX_PASSWORD",
            "password": "123456",
            "rnAccount": "",
            "rnPwd": "",
            "taxpayer": {
                "djzclx_dm": "411",
                "hy_dm": "7499",
                "zcdz": "四川省成都市武侯区一环路西一段130号1栋8层823号",
                "bsryddh": "",
                "jyfw": "",
                "djzclx_mc": "内资个体",
                "dwlsgx_dm": "51",
                "xgrq": "",
                "scjydz": "四川省成都市武侯区一环路西一段130号1栋8层823号",
                "djxh": "10215101000000766331",
                "cyrs": "",
                "zgswskfj_dm": "15101072200",
                "wjcyrs": "",
                "jdxz_dm": "510107001",
                "nsrzt_dm": "03",
                "zgswj_dm": "15101070001",
                "fddbrxm": "吉小梅",
                "zzjg_dm": "",
                "nsrmc": "泸州鸣思网络技术有限公司",
                "fddbryddh": "",
                "zczb": "",
                "djrq": "2021-10-09",
                "kzztdjlx_mc": "",
                "nsrzt_mc": "正常",
                "bsrxm": "",
                "zgswskfj_mc": "国家税务总局成都市武侯区税务局玉林税务所",
                "cwfzrxm": "",
                "shxydm": "913301095605540607",
                "zgswj_mc": "国家税务总局成都市武侯区税务局东福大厦",
                "nsrsbh": "913301095605540607",
                "hy_mc": "其他未列明专业技术服务业",
                "cwfzryddh": "",
                "zcdlxdh": ""
            }
        }
        response = self.post('/qhs-platform-manage/yk/individual-tax/register',
                             data)
        print(response.text)



processService = IndividualCallBackService()
# 巧慧算创建企业流程
# 创建企业
# processService.createEnterprise()
# 购买套餐
# processService.buyPackage()
# 线下收款
# processService.offlinePayment()
# 开通个税
# processService.individualOpen()
# 开通国税
# processService.openNational()
# 处理导入旧账
# processService.importOldAccount()
# 建账审核
# processService.createAccountAudit()
