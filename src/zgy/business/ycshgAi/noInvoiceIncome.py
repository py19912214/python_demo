from src.zgy.business.ycshgAi import PigYcshgAi


# 无票收入
class NoInvoiceIncomeService(PigYcshgAi):
    def selectThisMonthPage(self):
        data = {
            "period": 202503,
            "year": 2025,
            "month": 2,
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/no-invoice-income/v1/this-month-page',
                             data)
        print(response.text)


processService = NoInvoiceIncomeService()
# 更新注册信息
processService.selectThisMonthPage()
