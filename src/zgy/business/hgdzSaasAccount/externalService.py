from src.zgy.business.hgdzSaasAccount import PigYcshgSaasAccount


class ExternalService(PigYcshgSaasAccount):
    def get_invoice_info(self):
        data = {
            "period": [202501, 202502],
            "queryType": "10",
            "accountBookId": "3314140699852800000"  # 开发环境
            # "accountBookId": "3321749622456320000" # 测试环境
        }
        response = self.apiPost(
            "/hgdz-account-book-external/external/individual-fetch-count/v1/get_invoice_info",
            data)
        print(response.text)

    def accountBalanceSheetReportDataAcquisition(self):
        data = {
            "accountBookId": "3314140699852800000"  # 开发环境
            # "accountBookId": "3321749622456320000"  # 测试环境
        }
        response = self.apiPost(
            "/hgdz-account-book-external/nk/report/v1/get-account-balance-sheet-report-data-acquisition",
            data)
        print(response.text)

    def getBalanceSheetReportDataAcquisition(self):
        data = {
            "accountBookId": "3314140699852800000"  # 开发环境
            # "accountBookId": "3321749622456320000"  # 测试环境
        }
        response = self.apiPost(
            "/hgdz-account-book-external/nk/report/v1/get-balance-sheet-report-data-acquisition",
            data)
        print(response.text)


processService = ExternalService()
# processService.get_invoice_info()
processService.accountBalanceSheetReportDataAcquisition()
processService.getBalanceSheetReportDataAcquisition()
