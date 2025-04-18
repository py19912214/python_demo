from src.zgy.business.ycshgAi import PigYcshgAi


class IndividualCallBackService(PigYcshgAi):
    def syncLoginError(self):
        data = {
            "tpCompanyIdList": [331414076342276],
            "msg": "错误信息123123"
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-tax/v1/sync-login-error',
                             data)
        print(response.text)

    def syncInfo(self):
        data = {
            "tpEnterpriseId": 332527594602500,
            "jsonObject": {"jcxx": [{"djzclx_mc": "个体工商户", "zgswj_mc": "主税务机关名称", "nsrzt_dm": "03"}]}
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-tax/v1/sync-info',
                             data)
        print(response.text)

    def syncSubmissionStatus(self):
        data = {
            "tpEnterpriseId": 331059305594882,
            "submissionStatus": "SUBMIT_SUCCESS"
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-tax/v1/sync-submission-status',
                             data)
        print(response.text)

    def syncDeclareStatus(self):
        data = {
            "period": 202805,
            "type": "COMPREHENSIVE_INCOME",
            "tpEnterpriseId": 331059305594882,
            "enterpriseId": 1,
            "declareStatus": "DECLARE_SUCCESS",
            "declareMessage": "申报成功原因",
            "payStatus": "PAY_SUCCESS",
            "payMessage": "缴款成功原因",
            "actualTaxAmount": 100,
            "syncSource": 1,
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-tax/v1/sync-declare-status',
                             data)
        print(response.text)

    def syncReportInfo(self):
        data = {
            "tpEnterpriseId": 331059305594882,
            "type": "COMPREHENSIVE_INCOME",  # 代扣代缴 场景走这个分支
            "period": 202504,
            "enterpriseId": 1,
            "reportStatus": "FILLED",
            "submissionCount": 3,
            "personnelCount": 2,
            "incomeAmount": 4,
            "costExpense": 3,
            "profitAmount": 2,
            "insuredPersonnelCount": 2,
            "insuredIncomeAmount": 2,
            "pafPersonnelCount": 2,
            "pafPersonnelAmount": 2,
            "taxAmount": 100,
            "taxPayable": 101,
            "actualTaxPaid": 102,
            "revenueTotalAmount": 102,
            "costAmount": 103,
            "nationalDebtInterestIncome": 104,
            "totalProfit": 105,
            "payTaxesIncrease": 106,
            "payTaxesDecrease": 107,
            "payTaxesIncome": 108,
            "redeemAmount": 109
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-tax/v1/sync-report-info',
                             data)
        print(response.text)

    def syncLogInsert(self):
        data = {
            "period": 202504,
            "tpEnterpriseId": 331059305594882,
            "type": "UPDATE_LEVY_INFO",
            "content": "新增日志内容",
            "whetherAnnual": False,
            "userId": 1,
            "userName": "userName"
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-tax/v1/sync-record-insert',
                             data)
        print(response.text)

    def syncDutyPaidProof(self):
        data = {
            "period": 202504,
            "tpEnterpriseId": 331059305594882,
            "dutyPaidProofUrl": "https://dutypaidproof.hggh.gov.cn",
            "reportType": 1
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-tax/v1/sync-duty-paid-proof',
                             data)
        print(response.text)

    def syncLevyInfo(self):
        data = {
            "companyId": 1,
            "period": 202504,
            "taxDeadline": "MONTHLY",
            "method": "REGULAR_QUOTA",
            "taxIdentification": "OTHERS_INCOME_RATIO"
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-tax/v1/production/sync-levy-info',
                             data)
        print(response.text)

    def syncProductionDeclareStatus(self):
        data = {
            "period": 202504,
            # PRODUCTION_OPERATION :生产经营 PRODUCTION_OPERATION_ANNUAL_B ：生产经营年度汇算
            "type": "PRODUCTION_OPERATION_ANNUAL_B",
            "tpEnterpriseId": 331059305594882,
            "enterpriseId": 1,
            "declareStatus": "DECLARE_SUCCESS",
            "declareMessage": "申报成功原因",
            "payStatus": "PAY_SUCCESS",
            "payMessage": "缴款成功原因",
            "actualTaxAmount": 100,
            "syncSource": 1,
        }
        response = self.post(
            '/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-tax/v1/production/sync-declare-status',
            data)
        print(response.text)

    def syncProductionReportInfo(self):
        data = {
            "tpEnterpriseId": 331059305594882,
            # PRODUCTION_OPERATION :生产经营 PRODUCTION_OPERATION_ANNUAL_B ：生产经营年度汇算
            "type": "PRODUCTION_OPERATION_ANNUAL_B",
            "period": 202504,
            "enterpriseId": 1,
            "reportStatus": "FILLED",
            "submissionCount": 3,
            "personnelCount": 2,
            "incomeAmount": 4,
            "costExpense": 3,
            "profitAmount": 2,
            "insuredPersonnelCount": 2,
            "insuredIncomeAmount": 2,
            "pafPersonnelCount": 2,
            "pafPersonnelAmount": 2,
            "taxAmount": 100,
            "taxPayable": 101,
            "actualTaxPaid": 102,
            "revenueTotalAmount": 102,
            "costAmount": 103,
            "nationalDebtInterestIncome": 104,
            "totalProfit": 105,
            "payTaxesIncrease": 106,
            "payTaxesDecrease": 107,
            "payTaxesIncome": 108,
            "redeemAmount": 109
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-tax/v1/production/sync-report-info',
                             data)
        print(response.text)

    def syncProductionDutyPaidProof(self):
        data = {
            "period": 202504,
            "tpEnterpriseId": 331059305594882,
            "dutyPaidProofUrl": "https://dutypaidproof.hggh.gov.cn",
            "reportType": 2  # 1:生产经营 2：生产经营年度汇算
        }
        response = self.post(
            '/ycshg-ai-platform-produce-hgdz-cronjob/nk/individual-tax/v1/production/sync-duty-paid-proof',
            data)
        print(response.text)


processService = IndividualCallBackService()
# 同步开通信息登陆失败
processService.syncLoginError()
# 同步个税信息
# processService.syncInfo()
# 同步人员送报信息
# processService.syncSubmissionStatus()
# 同步报表申报缴款状态
# processService.syncDeclareStatus()
# 同步报表信息
# processService.syncReportInfo()
# 同步新增日志
# processService.syncLogInsert()
# 同步完税证明
# processService.syncDutyPaidProof()
# # 同步核定信息
# processService.syncLevyInfo()
# 生产经营同步报表申报缴款状态
# processService.syncProductionDeclareStatus()
# 生产经营同步报表信息
# processService.syncProductionReportInfo()
# 生产经营同步完税证明
# processService.syncProductionDutyPaidProof()
