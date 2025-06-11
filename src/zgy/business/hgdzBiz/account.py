from src.zgy.business.hgdzBiz import PigYcshgAi


class AccountService(PigYcshgAi):

    def createAccount(self):
        data = {
            "enterpriseId": "202504100000002",
            "serviceType": "ALL",
            "payrollConfirmType": "ACCRUAL_LAST_ISSUED_LAST",
            # "accountBookCode": "123456",
            "accountBookName": "123456",
            "startPeriod": "202504",
            "currencyCode": "rmb",
            "accountSystem": "SMALL_BUSINESS_ACCOUNT_SYSTEM",
            "taxNature": "SMALL_SCALE_TAXPAYER",
            "tradeStandard": "SM_TYX",
            "industryCategory": "1",
            "industrySubcategory": "1"
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/account/v1/create-account',
                             data)
        print(response.text)


processService = AccountService()
# 开通账套
processService.createAccount()
