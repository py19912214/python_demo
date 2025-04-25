from src.zgy.business.ycshgAi import PigYcshgAi


# 无票收入
class BankReceiptService(PigYcshgAi):
    def page(self):
        data = {
            "accountBookId": 3325306714030080000,
            "period": 202504
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/yk/bank-receipt/v1/page',
                             data)
        print(response.text)



processService = BankReceiptService()
# 获取一二级分类类别信息
processService.page()
