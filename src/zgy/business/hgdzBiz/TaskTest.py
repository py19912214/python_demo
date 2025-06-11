from src.zgy.business.hgdzBiz import PigYcshgAi


class ProcessService(PigYcshgAi):

    def polling(self, id):
        data = {
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-cronjob/nk/task-test/national/polling?id=' + str(id),
                             data)
        print(response.text)

    def querySalary(self):
        data = {
            "companyInfoId": 332531006668804,
            "period": 202505
        }
        response = self.post('/ycshg-ai-platform-produce-hgdz-biz/nk/internal/payroll/v1/query-salary',
                             data)
        print(response.text)


processService = ProcessService()
# 开通账套
# processService.polling(337433927761920)
processService.querySalary()
