from src.zgy.business.hgdzBiz import PigYcshgAi


class EnterpriseTagService(PigYcshgAi):
    def groupList(self):
        response = self.get('/ycshg-ai-platform-produce-hgdzBiz-biz/yk/enterprise-tag/v1/group/list', {})
        print(response.text)

    def page(self, id):
        data = {
            "id": 0
        }
        response = self.post('/ycshg-ai-platform-produce-hgdzBiz-biz/yk/enterprise-tag/v1/tag/page?id=' + id,
                             data)
        print(response.text)

    def getInfo(self, id):
        response = self.get('/ycshg-ai-platform-produce-hgdzBiz-biz/yk/enterprise-tag/v1/info?id=' + id, {})
        print(response.text)

    def groupAllList(self):
        response = self.get('/ycshg-ai-platform-produce-hgdzBiz-biz/yk/enterprise-tag/v1/all/list', {})
        print(response.text)


processService = EnterpriseTagService()
# 查询列表
processService.groupList()
# 标签分页
processService.page('0')
# 标签分页
processService.getInfo("4")
# 查询所有分组数据
processService.groupAllList()
