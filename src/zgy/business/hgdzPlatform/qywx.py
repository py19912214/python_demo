from src.zgy.business.hgdzPlatform import BaseParent


class ProcessService(BaseParent):
    def selectByType(self):
        data = {
        }
        response = self.get(
            "/ycshg-ai-service-provider/yk/qywx-sidebar-links/v1/select-by-type",
            data)
        print(response.text)

    def loadMenu(self):
        data = {
        }
        response = self.get(
            "/ycshg-ai-service-provider/yk/qywx/user/menu/load-menu",
            data)
        print(response.text)


processService = ProcessService()
# 基础配置
# processService.selectByType()
processService.loadMenu()
