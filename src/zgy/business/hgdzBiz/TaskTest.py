from src.zgy.business.hgdzBiz import PigYcshgAi


class ProcessService(PigYcshgAi):

    def polling(self, id):
        data = {
        }
        response = self.post('/ycshg-ai-platform-produce-hgdzBiz-cronjob/nk/task-test/national/polling?id=' + str(id),
                             data)
        print(response.text)


processService = ProcessService()
# 开通账套
processService.polling(337433927761920)
