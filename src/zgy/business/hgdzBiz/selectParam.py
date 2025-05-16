from src.zgy.business.hgdzBiz import PigYcshgAi


class SelectParam(PigYcshgAi):
    def selectTagTree(self):
        data = {}
        response = self.post('/ycshg-ai-platform-produce-hgdzBiz-biz/yk/select-option/select-tag-tree',
                             data)
        print(response.text)


selectParam = SelectParam()
# 查询标签树
selectParam.selectTagTree()
