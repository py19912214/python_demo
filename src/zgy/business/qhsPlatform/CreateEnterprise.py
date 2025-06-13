import json
import time

from src.zgy.CommonUtils import CommonUtils
from src.zgy.business.mysql import Database
from src.zgy.business.qhsPlatform import PigQhs


class IndividualCallBackService(PigQhs):

    def createEnterprise(self, customerTenantId, creditCode, enterpriseName):
        data = {
            # 是个人租户id 在 qhs_customer_management表的id 保存的企业数据 租户id 是qhs_customer_management 表的 ope_tenant_id
            "tenantId": customerTenantId,
            "creditCode": creditCode,
            "enterpriseName": enterpriseName,
            "juridicalPerson": "小潘"
        }
        response = self.loopSubmit('/qhs-platform-web/yk/enterprise-login/v1/create-enterprise', data)

        print('创建企业成功')
        return json.loads(response.text)['data']['id']

    def buyPackage(self, enterpriseId):
        data = {
            "packageType": 1,  # 1:新增 2:续费
            "enterpriseId": enterpriseId,  # 会被请求头的参数 x-tenant-enterprise-id 替换掉
            "packageId": 304654982774784,  # 先用这个 配置在 qhs_agency_bookkeeping_product_detail 表
            "specification": "THREE_YEARS",  # ONE_MONTH ONE_YEAR TWO_YEARS THREE_YEARS PERMANENT
            "serviceStartTime": 202504,
            "serviceStopTime": 209912,
            "amount": 2484.00  # 金额必须要跟配置的保持一致
        }
        # 会被请求头的参数 x-tenant-enterprise-id 替换掉
        self.setTenantEnterpriseId(enterpriseId);
        self.loopSubmit('/qhs-platform-applet/yk/applet/my-interface/v1/buy-package', data)
        print("购买商品成功")

    def offlinePayment(self, enterpriseId):
        paymentId = databaseProcess.queryFirstColumns(connection,
                                                      "select id from `qhs_platform`.qhs_order_payment where enterprise_id='" + str(
                                                          enterpriseId) + "'")
        print('paymentId: ' + str(paymentId))
        data = {
            "paymentId": paymentId,  # qhs_order_payment表id
            "paymentMethod": 2,  # 1线上 2线下
            "actualAmount": 2484.0,
            "paymentTime": "2025-06-12 12:00:00",
            "paymentChannel": "OTHER",  # "WECHAT","ALIPAY","BANK_CARD","CASH","OTHER"
            "remark": "备注",
            "wechatOrderNo": "asdasdasd123546"
        }
        # 会被请求头的参数 x-tenant-enterprise-id 替换掉
        self.setTenantEnterpriseId(enterpriseId);
        self.loopSubmit('/qhs-platform-manage/yk/order/payment/v1/offline-payment', data)
        print('线下收款开通成功')

    def openNational(self, enterpriseId):
        data = {
            "enterpriseId": enterpriseId,
            "taxArea": "CODE_51",
            "loginType": "AGENCY_LOGIN",
            "identityType": "FDDBR",
            "loginPwd": "123456",
            "agentName": "123456",
            "todoId": 0
        }
        # 会被请求头的参数 x-tenant-enterprise-id 替换掉
        self.setTenantEnterpriseId(enterpriseId);
        self.loopSubmit('/qhs-platform-applet/yk/national-tax/open', data)
        print('国税开通成功')

    def importOldAccount(self, enterpriseId):
        todoId = databaseProcess.queryFirstColumns(connection,
                                                   "select id from `qhs_platform`.qhs_enterprise_to_do where enterprise_id='" + str(enterpriseId) + "' and to_do_code='MA1003'")
        print('todoId: ' + str(todoId))
        data = {
        }
        # 会被请求头的参数 x-tenant-enterprise-id 替换掉
        self.setTenantEnterpriseId(enterpriseId);
        self.loopSubmit(
            '/qhs-platform-applet/yk/applet/to-do-handling/v1/import-old-account?id=' + str(todoId) + '&fileIds=', data)
        print('导入处理成功')

    def createAccountAudit(self, enterpriseId):
        while True:
            accountAuditId = databaseProcess.queryFirstColumns(connection,
                                                               "select id from `qhs_platform`.qhs_enterprise_create_account_audit where enterprise_id='" + str(
                                                                   enterpriseId) + "'")
            if accountAuditId == None:
                print("暂时没有获取到：accountAuditId，等待重试")
                time.sleep(5)
                continue
            print('accountAuditId: ' + str(accountAuditId))
            break
        data = {
            # select id from qhs_enterprise_create_account_audit where enterprise_id=@enterpriseId
            "id": accountAuditId,
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
        self.setTenantEnterpriseId(enterpriseId);
        self.loopSubmit('/qhs-platform-manage/yk/enterprise-create-account-audit/v1/create-account-audit', data)

    def individualOpen(self, enterpriseId):
        data = {
            "enterpriseId": enterpriseId,
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
        self.setTenantEnterpriseId(enterpriseId);
        self.loopSubmit('/qhs-platform-manage/yk/individual-tax/register', data)
        print('个税开通成功')

    def loopSubmit(self, url, data):
        while True:
            try:
                response = self.post(url, data)
                print(response.text)
                if self.checkReqSuccess(response):
                    return response
            except Exception as err:
                print(f"处理异常: '{err}'")
            time.sleep(10)


processService = IndividualCallBackService()
databaseProcess = Database()
commonUtils = CommonUtils()
# 初始化参数
creditCode = commonUtils.createTaxNo();
enterpriseName = commonUtils.createEnterpriseName();
customerTenantId = '3109336583045120000'
# 巧慧算创建企业流程
connection = databaseProcess.initConnection('qhs_test')
# 重置上下文租户id 租户id是 根据个人租户id去取的
print('creditCode: ' + str(creditCode))
opeTenantId = databaseProcess.queryFirstColumns(connection,
                                                "select ope_tenant_id from `qhs_platform`.qhs_customer_management where id='" + customerTenantId + "'")
processService.setTenantId(opeTenantId)

#  ***************************  业务开始 *****************
# 1.创建企业
processService.createEnterprise(customerTenantId, creditCode, enterpriseName)
# 查询企业id
# creditCode = '913120250613100410T'
enterpriseId = databaseProcess.queryFirstColumns(connection,
                                                 "select id from `qhs_platform`.qhs_enterprise where credit_code='" + creditCode + "'")
print('enterpriseId: ' + str(enterpriseId))
# 2.购买套餐
processService.buyPackage(enterpriseId)
# 3.线下收款
processService.offlinePayment(enterpriseId)
# 4.开通个税
processService.individualOpen(enterpriseId)
# 5.开通国税
processService.openNational(enterpriseId)
# 6.处理导入旧账
processService.importOldAccount(enterpriseId)
# 7.建账审核 需要国税开通成功后 才可以
processService.createAccountAudit(enterpriseId)
